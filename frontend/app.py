from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
from config import Config
from services import api_client
import io

app = Flask(__name__)
app.config.from_object(Config)

def is_logged_in():
    return "access_token" in session

@app.route("/")
def index():
    if is_logged_in():
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        response = api_client.login(email, password)
        if response.status_code == 200:
            try:
                data = response.json()
                session["access_token"] = data["access_token"]
                return redirect(url_for("dashboard"))
            except ValueError:
                flash("Erro interno do servidor (Resposta inválida)", "danger")
        else:
            try:
                error_data = response.json()
                flash(error_data.get("detail", "E-mail ou senha incorretos"), "danger")
            except ValueError:
                flash("Erro na comunicação com o servidor", "danger")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        
        if password != confirm_password:
            flash("As senhas não coincidem", "warning")
            return render_template("register.html")
            
        response = api_client.register(name, email, password)
        if response.status_code == 200:
            flash("Cadastro realizado com sucesso. Faça login.", "success")
            return redirect(url_for("login"))
        else:
            try:
                error_data = response.json()
                flash(error_data.get("detail", "Erro ao cadastrar"), "danger")
            except ValueError:
                flash(f"Erro do servidor (Código: {response.status_code}). Verifique se o backend está rodando.", "danger")
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if not is_logged_in():
        return redirect(url_for("login"))
    
    user_response = api_client.get_me()
    if user_response.status_code != 200:
        session.clear()
        return redirect(url_for("login"))
    
    user = user_response.json()
    papers_response = api_client.list_papers()
    papers = papers_response.json() if papers_response.status_code == 200 else []
    
    return render_template("dashboard.html", user=user, papers=papers)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if not is_logged_in():
        return redirect(url_for("login"))
    
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            flash("Nenhum arquivo selecionado", "warning")
            return redirect(request.url)
        
        response = api_client.upload_paper(file)
        if response.status_code == 200:
            flash("Paper enviado com sucesso. A análise foi iniciada.", "success")
            return redirect(url_for("dashboard"))
        else:
            error_data = response.json()
            flash(error_data.get("detail", "Erro no upload"), "danger")
            
    return render_template("upload.html")

@app.route("/analysis/<int:paper_id>")
def analysis_detail(paper_id):
    if not is_logged_in():
        return redirect(url_for("login"))
    
    paper_response = api_client.get_paper_detail(paper_id)
    if paper_response.status_code != 200:
        flash("Paper não encontrado", "danger")
        return redirect(url_for("dashboard"))
    
    paper = paper_response.json()
    result_response = api_client.get_analysis_result(paper_id)
    result = result_response.json() if result_response.status_code == 200 else None
    
    return render_template("analysis_detail.html", paper=paper, result=result)

@app.route("/download/<int:paper_id>/<type>")
def download(paper_id, type):
    if not is_logged_in():
        return redirect(url_for("login"))
    
    response = api_client.download_result(paper_id, type)
    if response.status_code == 200:
        filename = response.headers.get("Content-Disposition", "").split("filename=")[-1].strip('"')
        return send_file(
            io.BytesIO(response.content),
            download_name=filename,
            as_attachment=True
        )
    else:
        flash("Erro ao baixar resultado", "danger")
        return redirect(url_for("analysis_detail", paper_id=paper_id))

@app.route("/analysis/<int:paper_id>/logs")
def analysis_logs(paper_id):
    if not is_logged_in():
        return redirect(url_for("login"))
    
    logs_response = api_client.get_analysis_logs(paper_id)
    logs = logs_response.json() if logs_response.status_code == 200 else []
    
    paper_response = api_client.get_paper_detail(paper_id)
    paper = paper_response.json() if paper_response.status_code == 200 else {"id": paper_id, "original_filename": "Unknown"}
    
    return render_template("analysis_logs.html", paper=paper, logs=logs)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
