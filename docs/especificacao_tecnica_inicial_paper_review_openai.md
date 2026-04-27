# Especificação Técnica Final — Aplicação Web para Análise Automatizada de Papers Científicos com OpenAI

## 1. Visão Geral

Esta especificação consolida a versão inicial da aplicação, baseada em frontend Flask e backend FastAPI, com a versão atualizada que integra o pipeline de análise de papers à API da OpenAI.

A aplicação tem como objetivo permitir que usuários autenticados façam upload de arquivos `paper.pdf` e recebam automaticamente uma análise crítica estruturada do artigo científico. O processo utiliza duas skills internas, armazenadas no backend:

- `skill1.md` — **Paper Review Comments**
- `skill2.md` — **Program Committee Review Comments**

A análise será executada pelo backend por meio de chamadas à API da OpenAI. O backend será responsável por autenticação, autorização, persistência, organização dos arquivos, orquestração do pipeline, chamada à OpenAI, armazenamento dos resultados e controle de acesso por usuário.

Cada usuário poderá visualizar somente seus próprios papers, suas próprias análises e seus próprios arquivos gerados.

---

## 2. Objetivos da Aplicação

A aplicação deverá:

1. Permitir cadastro de novos usuários.
2. Permitir login de usuários cadastrados.
3. Usar autenticação baseada em JWT.
4. Permitir upload de arquivos PDF contendo papers científicos.
5. Armazenar os arquivos enviados em diretórios privados por usuário.
6. Manter as skills padrão no backend.
7. Integrar o backend com a API da OpenAI.
8. Enviar o `paper.pdf` para leitura e análise pela OpenAI.
9. Usar `skill1.md` e `skill2.md` como instruções do pipeline.
10. Gerar resumo preliminar do paper.
11. Gerar `Comments to Authors.txt`.
12. Gerar `Comments to Committee.txt`.
13. Gerar resumos finais de até 5000 caracteres para cada conjunto de comentários.
14. Salvar os artefatos gerados em disco.
15. Persistir metadados e resultados no banco SQLite.
16. Exibir ao usuário logado o histórico de papers analisados.
17. Permitir visualização e download dos resultados.
18. Garantir isolamento completo dos dados por usuário.

---

## 3. Arquitetura Geral

A aplicação será organizada em dois serviços principais:

1. **Frontend Web**
   - Flask
   - HTML
   - CSS
   - Bootstrap 5.3
   - JavaScript

2. **Backend API**
   - FastAPI
   - SQLite
   - SQLAlchemy
   - JWT
   - OpenAI SDK/API
   - Armazenamento local de arquivos

### 3.1 Visão Arquitetural

```text
┌──────────────────────────────────────────────┐
│                Frontend Web                  │
│ Flask + HTML + CSS + Bootstrap + JavaScript  │
└───────────────────────┬──────────────────────┘
                        │ HTTP/REST
                        ▼
┌──────────────────────────────────────────────┐
│                 Backend API                  │
│ FastAPI + JWT + SQLAlchemy + OpenAI Client   │
└───────────────────────┬──────────────────────┘
                        │
        ┌───────────────┴────────────────┐
        ▼                                ▼
┌───────────────────────┐      ┌───────────────────────┐
│        SQLite          │      │      OpenAI API        │
│ Users, Papers, Results │      │ PDF + Skills + Prompts │
└───────────────────────┘      └───────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────┐
│              Backend File Storage            │
│ skills/, uploads/, outputs/, temp/           │
└──────────────────────────────────────────────┘
```

---

## 4. Tecnologias

### 4.1 Frontend

| Tecnologia | Finalidade |
|---|---|
| Flask | Renderização das páginas web e comunicação com o backend |
| HTML | Estrutura das páginas |
| CSS | Estilização complementar |
| Bootstrap 5.3 | Layout responsivo e componentes visuais |
| JavaScript | Interações no dashboard, upload e atualização de status |
| Jinja2 | Templates HTML no Flask |

### 4.2 Backend

| Tecnologia | Finalidade |
|---|---|
| FastAPI | API REST da aplicação |
| SQLite | Banco de dados local |
| SQLAlchemy | ORM para persistência |
| Pydantic | Validação de schemas |
| JWT | Autenticação baseada em token |
| bcrypt/passlib | Hash seguro de senhas |
| OpenAI SDK | Comunicação com a API da OpenAI |
| Python Multipart | Recebimento de upload de arquivos |
| Uvicorn | Servidor ASGI do backend |

---

## 5. Componentes Principais

## 5.1 Frontend Web

O frontend será responsável por:

- exibir telas de login e cadastro;
- armazenar temporariamente o token JWT na sessão Flask;
- enviar requisições autenticadas ao backend;
- permitir upload de papers;
- listar papers enviados pelo usuário;
- exibir status de processamento;
- exibir resultados resumidos;
- permitir download dos artefatos gerados.

O frontend não deve conter nenhuma chave da OpenAI nem lógica sensível do pipeline.

---

## 5.2 Backend API

O backend será responsável por:

- cadastrar usuários;
- autenticar usuários;
- gerar tokens JWT;
- validar tokens JWT;
- receber uploads de PDF;
- criar registros de papers;
- salvar arquivos em diretórios privados por usuário;
- carregar as skills locais;
- enviar o PDF à OpenAI;
- executar o pipeline de análise;
- salvar os arquivos gerados;
- persistir resultados no SQLite;
- controlar status da análise;
- garantir que cada usuário acesse apenas seus próprios recursos.

---

## 5.3 Banco de Dados

O SQLite armazenará:

- usuários;
- papers enviados;
- status das análises;
- metadados do upload;
- identificador do arquivo na OpenAI;
- caminhos dos arquivos gerados;
- textos resumidos para exibição;
- informações de auditoria da execução.

---

## 5.4 File Storage

A aplicação deverá manter os arquivos organizados no backend.

```text
backend/storage/
│
├── skills/
│   ├── skill1.md
│   └── skill2.md
│
├── uploads/
│   └── user_1/
│       └── paper_10/
│           └── paper.pdf
│
├── outputs/
│   └── user_1/
│       └── paper_10/
│           ├── Paper_Summary.txt
│           ├── Comments to Authors.txt
│           ├── Comments to Committee.txt
│           ├── Comments to Authors - Summary 5000 chars.txt
│           └── Comments to Committee - Summary 5000 chars.txt
│
└── temp/
```

---

## 6. Fluxo Geral da Aplicação

```text
Usuário acessa a aplicação
        │
        ▼
Realiza cadastro ou login
        │
        ▼
Frontend recebe JWT
        │
        ▼
Usuário acessa dashboard
        │
        ▼
Usuário faz upload de paper.pdf
        │
        ▼
Backend salva o paper localmente
        │
        ▼
Backend cria registro no banco
        │
        ▼
Backend carrega skill1.md e skill2.md
        │
        ▼
Backend envia paper.pdf para OpenAI
        │
        ▼
OpenAI lê o paper.pdf
        │
        ▼
OpenAI gera resumo preliminar
        │
        ▼
OpenAI gera Comments to Authors
        │
        ▼
OpenAI gera Comments to Committee
        │
        ▼
OpenAI resume cada comentário para até 5000 caracteres
        │
        ▼
Backend valida, salva e persiste os resultados
        │
        ▼
Frontend exibe resultados ao usuário
```

---

## 7. Pipeline de Análise com OpenAI

## 7.1 Entradas

```text
paper.pdf
skill1.md
skill2.md
```

## 7.2 Saídas Intermediárias

```text
Paper_Summary.txt
Comments to Authors.txt
Comments to Committee.txt
```

## 7.3 Saídas Finais

```text
Comments to Authors - Summary 5000 chars.txt
Comments to Committee - Summary 5000 chars.txt
```

## 7.4 Estratégia de Execução

O pipeline deverá ser executado em chamadas sequenciais à API da OpenAI. Essa estratégia facilita rastreabilidade, reprocessamento, depuração e persistência de resultados intermediários.

```text
Chamada 1 → Enviar paper.pdf para OpenAI
Chamada 2 → Gerar Paper_Summary.txt
Chamada 3 → Gerar Comments to Authors.txt
Chamada 4 → Gerar Comments to Committee.txt
Chamada 5 → Resumir Comments to Authors.txt para até 5000 caracteres
Chamada 6 → Resumir Comments to Committee.txt para até 5000 caracteres
```

---

## 8. Fluxo Técnico do Pipeline

```text
run_openai_analysis_pipeline(user_id, paper_id)
        │
        ▼
1. Buscar paper no banco usando paper_id + user_id
        │
        ▼
2. Validar propriedade do paper
        │
        ▼
3. Atualizar status para "processing"
        │
        ▼
4. Carregar arquivo paper.pdf
        │
        ▼
5. Carregar skill1.md
        │
        ▼
6. Carregar skill2.md
        │
        ▼
7. Enviar paper.pdf para OpenAI
        │
        ▼
8. Receber openai_file_id
        │
        ▼
9. Gerar Paper_Summary.txt
        │
        ▼
10. Gerar Comments to Authors.txt usando:
        ├── paper.pdf
        ├── Paper_Summary.txt
        └── skill1.md
        │
        ▼
11. Gerar Comments to Committee.txt usando:
        ├── paper.pdf
        ├── Paper_Summary.txt
        ├── Comments to Authors.txt
        └── skill2.md
        │
        ▼
12. Gerar resumo de Comments to Authors
        └── limite máximo: 5000 caracteres
        │
        ▼
13. Gerar resumo de Comments to Committee
        └── limite máximo: 5000 caracteres
        │
        ▼
14. Validar tamanho dos resumos
        │
        ▼
15. Salvar arquivos em outputs/user_id/paper_id/
        │
        ▼
16. Persistir metadados e textos resumidos no SQLite
        │
        ▼
17. Atualizar status para "completed"
```

Em caso de erro:

```text
Erro no pipeline
        │
        ▼
Registrar log técnico
        │
        ▼
Salvar mensagem resumida de erro
        │
        ▼
Atualizar status para "failed"
        │
        ▼
Retornar erro controlado ao frontend
```

---

## 9. Regras do Pipeline

### 9.1 Resumo Preliminar

O resumo preliminar deverá identificar:

1. Tema central.
2. Objetivo principal.
3. Problema de pesquisa.
4. Hipótese, questão de pesquisa ou motivação.
5. Metodologia.
6. Dados, corpus, participantes ou artefatos analisados.
7. Técnicas, ferramentas ou modelos utilizados.
8. Principais resultados.
9. Contribuições declaradas.
10. Limitações reconhecidas.
11. Pontos mais importantes.

### 9.2 Comments to Authors

O arquivo `Comments to Authors.txt` deverá ser produzido com base em:

```text
paper.pdf + Paper_Summary.txt + skill1.md
```

Deverá conter comentários técnicos, críticos, respeitosos e úteis aos autores.

### 9.3 Comments to Committee

O arquivo `Comments to Committee.txt` deverá ser produzido com base em:

```text
paper.pdf + Paper_Summary.txt + Comments to Authors.txt + skill2.md
```

Deverá conter comentários técnicos, críticos e confidenciais ao comitê.

### 9.4 Resumos Finais

Os arquivos finais deverão conter no máximo 5000 caracteres cada:

```text
Comments to Authors - Summary 5000 chars.txt
Comments to Committee - Summary 5000 chars.txt
```

O backend deverá validar localmente o tamanho final. Caso a saída ultrapasse o limite, o backend deverá solicitar nova redução à OpenAI ou aplicar corte controlado como último recurso.

---

## 10. Modelo de Dados

## 10.1 User

Representa um usuário cadastrado.

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | Integer | Identificador único |
| `name` | String | Nome do usuário |
| `email` | String | E-mail único |
| `password_hash` | String | Senha criptografada |
| `is_active` | Boolean | Indica se o usuário está ativo |
| `created_at` | DateTime | Data de criação |
| `updated_at` | DateTime | Data de atualização |

---

## 10.2 Paper

Representa um paper enviado por um usuário.

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | Integer | Identificador único |
| `user_id` | Integer | Dono do paper |
| `original_filename` | String | Nome original do arquivo |
| `stored_filename` | String | Nome interno salvo |
| `file_path` | String | Caminho local do PDF |
| `openai_file_id` | String | ID do arquivo enviado à OpenAI |
| `title` | String | Título extraído/inferido, quando disponível |
| `status` | String | Status da análise |
| `analysis_started_at` | DateTime | Início do pipeline |
| `analysis_finished_at` | DateTime | Fim do pipeline |
| `error_message` | Text | Mensagem resumida de erro |
| `created_at` | DateTime | Data de upload |
| `updated_at` | DateTime | Data de atualização |

Status possíveis:

```text
uploaded
processing
completed
failed
```

---

## 10.3 AnalysisResult

Representa os resultados produzidos para um paper.

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | Integer | Identificador único |
| `paper_id` | Integer | Paper analisado |
| `user_id` | Integer | Dono da análise |
| `paper_summary_path` | String | Caminho do `Paper_Summary.txt` |
| `comments_authors_path` | String | Caminho do `Comments to Authors.txt` |
| `comments_committee_path` | String | Caminho do `Comments to Committee.txt` |
| `comments_authors_summary_path` | String | Caminho do resumo dos autores |
| `comments_committee_summary_path` | String | Caminho do resumo do comitê |
| `comments_authors_summary_text` | Text | Texto resumido para exibição |
| `comments_committee_summary_text` | Text | Texto resumido para exibição |
| `model_used` | String | Modelo OpenAI usado |
| `prompt_tokens` | Integer | Tokens de entrada, quando disponíveis |
| `completion_tokens` | Integer | Tokens de saída, quando disponíveis |
| `total_tokens` | Integer | Total de tokens |
| `openai_response_metadata` | Text/JSON | Metadados da execução |
| `created_at` | DateTime | Data de criação |
| `updated_at` | DateTime | Data de atualização |

---

## 10.4 Relacionamentos

```text
User 1 ──── N Paper
User 1 ──── N AnalysisResult
Paper 1 ─── 1 AnalysisResult
```

---

## 11. Banco de Dados — SQL Conceitual

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at DATETIME,
    updated_at DATETIME
);

CREATE TABLE papers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    original_filename VARCHAR(255) NOT NULL,
    stored_filename VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    openai_file_id VARCHAR(255),
    title VARCHAR(500),
    status VARCHAR(50) NOT NULL,
    analysis_started_at DATETIME,
    analysis_finished_at DATETIME,
    error_message TEXT,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE analysis_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    paper_id INTEGER NOT NULL,
    paper_summary_path TEXT,
    comments_authors_path TEXT,
    comments_committee_path TEXT,
    comments_authors_summary_path TEXT,
    comments_committee_summary_path TEXT,
    comments_authors_summary_text TEXT,
    comments_committee_summary_text TEXT,
    model_used VARCHAR(100),
    prompt_tokens INTEGER,
    completion_tokens INTEGER,
    total_tokens INTEGER,
    openai_response_metadata TEXT,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(paper_id) REFERENCES papers(id)
);
```

---

## 12. Estrutura de Pastas

```text
paper-review-app/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   │
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth_routes.py
│   │   │   ├── paper_routes.py
│   │   │   └── analysis_routes.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── jwt.py
│   │   │
│   │   ├── db/
│   │   │   ├── database.py
│   │   │   └── models.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── auth_schema.py
│   │   │   ├── user_schema.py
│   │   │   ├── paper_schema.py
│   │   │   └── analysis_schema.py
│   │   │
│   │   ├── services/
│   │   │   ├── auth_service.py
│   │   │   ├── user_service.py
│   │   │   ├── paper_service.py
│   │   │   ├── file_service.py
│   │   │   ├── skill_service.py
│   │   │   ├── openai_service.py
│   │   │   └── analysis_pipeline.py
│   │   │
│   │   └── utils/
│   │       ├── validators.py
│   │       └── text_utils.py
│   │
│   └── storage/
│       ├── skills/
│       │   ├── skill1.md
│       │   └── skill2.md
│       ├── uploads/
│       ├── outputs/
│       └── temp/
│
├── frontend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── .env.example
│   │
│   ├── services/
│   │   ├── api_client.py
│   │   └── auth_service.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── upload.html
│   │   ├── analysis_detail.html
│   │   └── error.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
│
└── README.md
```

---

## 13. Serviços do Backend

## 13.1 `auth_service.py`

Responsável por:

- criar usuário;
- validar credenciais;
- gerar hash de senha;
- verificar hash de senha;
- criar JWT;
- recuperar usuário autenticado.

Funções sugeridas:

```python
create_user(name, email, password)
authenticate_user(email, password)
create_access_token(user_id, email)
get_current_user(token)
```

---

## 13.2 `paper_service.py`

Responsável por:

- criar registro do paper;
- listar papers do usuário;
- buscar paper por `paper_id` e `user_id`;
- atualizar status;
- registrar início e fim da análise;
- registrar erro de execução.

Funções sugeridas:

```python
create_paper_record(user_id, original_filename, stored_filename, file_path)
list_user_papers(user_id)
get_user_paper(user_id, paper_id)
update_paper_status(paper_id, user_id, status)
set_openai_file_id(paper_id, user_id, openai_file_id)
set_analysis_error(paper_id, user_id, error_message)
```

---

## 13.3 `file_service.py`

Responsável por:

- validar PDF;
- criar diretórios;
- salvar upload;
- salvar arquivos de saída;
- ler arquivos de resultado;
- compactar resultados em `.zip`.

Funções sugeridas:

```python
validate_pdf_file(file)
create_user_paper_directory(user_id, paper_id)
create_user_output_directory(user_id, paper_id)
save_uploaded_pdf(file, destination_path)
save_text_output(output_dir, filename, content)
read_text_file(path)
create_results_zip(output_dir)
```

---

## 13.4 `skill_service.py`

Responsável por carregar as skills padrão.

Funções sugeridas:

```python
load_skill1()
load_skill2()
load_all_skills()
```

Diretório esperado:

```text
backend/storage/skills/
```

Arquivos obrigatórios:

```text
skill1.md
skill2.md
```

---

## 13.5 `openai_service.py`

Responsável pela comunicação com a API da OpenAI.

Funções sugeridas:

```python
upload_file_to_openai(file_path: str) -> str

generate_paper_summary(
    openai_file_id: str,
    model: str
) -> str

generate_comments_to_authors(
    openai_file_id: str,
    paper_summary: str,
    skill1_content: str,
    model: str
) -> str

generate_comments_to_committee(
    openai_file_id: str,
    paper_summary: str,
    comments_to_authors: str,
    skill2_content: str,
    model: str
) -> str

summarize_review_text(
    text: str,
    max_chars: int,
    model: str
) -> str
```

---

## 13.6 `analysis_pipeline.py`

Responsável por orquestrar o pipeline completo.

Função principal:

```python
run_openai_analysis_pipeline(
    db,
    user_id: int,
    paper_id: int
)
```

Responsabilidades:

1. Buscar o paper.
2. Validar propriedade.
3. Atualizar status para `processing`.
4. Carregar skills.
5. Enviar PDF à OpenAI.
6. Gerar resumo preliminar.
7. Gerar comentários aos autores.
8. Gerar comentários ao comitê.
9. Gerar resumos finais.
10. Validar limite de caracteres.
11. Salvar arquivos.
12. Persistir resultados.
13. Atualizar status para `completed`.
14. Em caso de falha, atualizar status para `failed`.

---

## 14. Endpoints do Backend

## 14.1 Autenticação

### `POST /api/auth/register`

Cadastra um novo usuário.

Entrada:

```json
{
  "name": "Nome do Usuário",
  "email": "usuario@email.com",
  "password": "senha123"
}
```

Saída:

```json
{
  "id": 1,
  "name": "Nome do Usuário",
  "email": "usuario@email.com"
}
```

---

### `POST /api/auth/login`

Realiza login e retorna token JWT.

Entrada:

```json
{
  "email": "usuario@email.com",
  "password": "senha123"
}
```

Saída:

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

---

### `GET /api/auth/me`

Retorna dados do usuário autenticado.

Header:

```http
Authorization: Bearer <token>
```

Saída:

```json
{
  "id": 1,
  "name": "Nome do Usuário",
  "email": "usuario@email.com"
}
```

---

## 14.2 Papers

### `POST /api/papers/upload`

Faz upload do paper e inicia o pipeline.

Header:

```http
Authorization: Bearer <token>
Content-Type: multipart/form-data
```

Entrada:

```text
file=paper.pdf
```

Saída:

```json
{
  "paper_id": 10,
  "status": "processing",
  "message": "Paper uploaded successfully. OpenAI analysis pipeline started."
}
```

---

### `GET /api/papers`

Lista papers do usuário autenticado.

Header:

```http
Authorization: Bearer <token>
```

Saída:

```json
[
  {
    "id": 10,
    "original_filename": "paper.pdf",
    "title": "Título extraído ou inferido",
    "status": "completed",
    "created_at": "2026-04-26T10:30:00"
  }
]
```

---

### `GET /api/papers/{paper_id}`

Retorna detalhes do paper do usuário autenticado.

Header:

```http
Authorization: Bearer <token>
```

Saída:

```json
{
  "id": 10,
  "original_filename": "paper.pdf",
  "title": "Título extraído ou inferido",
  "status": "completed",
  "analysis_started_at": "2026-04-26T10:30:00",
  "analysis_finished_at": "2026-04-26T10:35:00",
  "created_at": "2026-04-26T10:30:00",
  "updated_at": "2026-04-26T10:35:00"
}
```

---

## 14.3 Análises

### `GET /api/analyses/{paper_id}`

Retorna os resultados resumidos da análise.

Header:

```http
Authorization: Bearer <token>
```

Saída:

```json
{
  "paper_id": 10,
  "status": "completed",
  "comments_authors_summary": "Resumo dos comentários aos autores...",
  "comments_committee_summary": "Resumo dos comentários ao comitê...",
  "model_used": "modelo_configurado",
  "created_at": "2026-04-26T10:35:00"
}
```

---

### `GET /api/analyses/{paper_id}/download/authors-summary`

Baixa o arquivo:

```text
Comments to Authors - Summary 5000 chars.txt
```

---

### `GET /api/analyses/{paper_id}/download/committee-summary`

Baixa o arquivo:

```text
Comments to Committee - Summary 5000 chars.txt
```

---

### `GET /api/analyses/{paper_id}/download/all`

Baixa todos os artefatos em `.zip`.

Arquivos incluídos:

```text
Paper_Summary.txt
Comments to Authors.txt
Comments to Committee.txt
Comments to Authors - Summary 5000 chars.txt
Comments to Committee - Summary 5000 chars.txt
```

---

## 15. Telas do Frontend

## 15.1 Login

Rota:

```text
/login
```

Campos:

- e-mail;
- senha.

Ações:

- enviar credenciais ao backend;
- receber JWT;
- salvar token na sessão Flask;
- redirecionar para dashboard.

---

## 15.2 Cadastro

Rota:

```text
/register
```

Campos:

- nome;
- e-mail;
- senha;
- confirmação de senha.

Ações:

- validar campos;
- enviar dados ao backend;
- redirecionar para login.

---

## 15.3 Dashboard

Rota:

```text
/dashboard
```

Elementos:

- saudação ao usuário;
- botão para novo upload;
- tabela de papers enviados;
- status da análise;
- data do upload;
- ações de visualizar e baixar resultados.

Tabela sugerida:

| Paper | Status | Data | Ações |
|---|---|---|---|
| paper1.pdf | completed | 26/04/2026 | Ver resultados |
| paper2.pdf | processing | 26/04/2026 | Atualizar |

---

## 15.4 Upload

Rota:

```text
/upload
```

Campos:

- seletor de arquivo PDF.

Regras:

- aceitar apenas `.pdf`;
- exibir mensagem de envio;
- redirecionar para dashboard após upload.

---

## 15.5 Detalhes da Análise

Rota:

```text
/analysis/<paper_id>
```

Conteúdo:

1. Informações do paper.
2. Status da análise.
3. Resumo dos comentários aos autores.
4. Resumo dos comentários ao comitê.
5. Botões de download.

---

## 16. Segurança

## 16.1 Autenticação

A autenticação será baseada em JWT.

Payload sugerido:

```json
{
  "sub": "1",
  "email": "usuario@email.com",
  "exp": 1714150000
}
```

## 16.2 Armazenamento do Token

No frontend Flask, o token poderá ser armazenado em:

```python
session["access_token"]
```

Em cada requisição ao backend:

```http
Authorization: Bearer <token>
```

## 16.3 Senhas

As senhas devem ser armazenadas usando hash seguro, por exemplo:

```text
bcrypt
```

Nunca armazenar senhas em texto puro.

## 16.4 Chave da OpenAI

A chave da OpenAI deve existir somente no backend:

```env
OPENAI_API_KEY=...
```

A chave nunca deve ser enviada para:

- frontend;
- templates HTML;
- JavaScript;
- logs públicos;
- respostas da API.

## 16.5 Upload de Arquivos

O backend deve validar:

- extensão `.pdf`;
- MIME type;
- tamanho máximo;
- nome seguro;
- legibilidade mínima;
- diretório de destino controlado.

O nome original do arquivo não deve ser usado diretamente como nome salvo em disco.

## 16.6 Autorização por Usuário

Toda consulta a papers e análises deve filtrar pelo `user_id`.

Exemplo correto:

```python
paper = db.query(Paper).filter(
    Paper.id == paper_id,
    Paper.user_id == current_user.id
).first()
```

Exemplo incorreto:

```python
paper = db.query(Paper).filter(
    Paper.id == paper_id
).first()
```

Recomendação: retornar `404 Not Found` quando o recurso não existir ou não pertencer ao usuário, evitando revelar a existência de dados de outros usuários.

---

## 17. Variáveis de Ambiente

## 17.1 Backend `.env`

```env
APP_NAME=Paper Review API

DATABASE_URL=sqlite:///./paper_review.db

JWT_SECRET_KEY=change_this_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

MAX_UPLOAD_SIZE_MB=30

STORAGE_DIR=storage
SKILLS_DIR=storage/skills
UPLOADS_DIR=storage/uploads
OUTPUTS_DIR=storage/outputs
TEMP_DIR=storage/temp

OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=configure_model_here
OPENAI_SUMMARY_MODEL=configure_summary_model_here
OPENAI_MAX_RETRIES=3
OPENAI_TIMEOUT_SECONDS=120
```

## 17.2 Frontend `.env`

```env
FLASK_SECRET_KEY=change_this_frontend_secret
BACKEND_API_URL=http://localhost:8000/api
```

---

## 18. Prompts do Pipeline

## 18.1 Prompt para `Paper_Summary.txt`

```text
Você é um avaliador técnico-científico experiente.

Leia cuidadosamente o arquivo PDF anexado, que contém um paper científico.

Produza um resumo técnico preliminar contendo:

1. Tema central do artigo.
2. Objetivo principal.
3. Problema de pesquisa.
4. Hipótese, questão de pesquisa ou motivação.
5. Metodologia utilizada.
6. Dados, corpus, participantes ou artefatos analisados.
7. Técnicas, ferramentas ou modelos utilizados.
8. Principais resultados.
9. Contribuições declaradas.
10. Limitações reconhecidas pelos autores.
11. Pontos mais importantes do trabalho.

Use linguagem técnica, objetiva e estruturada.
Não invente informações que não estejam presentes no paper.
Quando alguma informação não estiver clara, indique explicitamente.
```

---

## 18.2 Prompt para `Comments to Authors.txt`

```text
Você é um revisor técnico-científico de uma conferência ou periódico.

Leia o paper anexado e considere o resumo preliminar abaixo.

Também siga rigorosamente as instruções da skill1.md, intitulada Paper Review Comments.

Sua tarefa é produzir comentários técnicos, críticos e construtivos destinados aos autores do artigo.

Os comentários devem avaliar:

1. Clareza do objetivo.
2. Relevância do problema.
3. Contribuição científica e técnica.
4. Adequação da metodologia.
5. Qualidade dos dados, experimentos ou estudo de caso.
6. Qualidade dos resultados.
7. Discussão e ameaças à validade.
8. Clareza textual e organização.
9. Pontos fortes.
10. Pontos fracos.
11. Sugestões de melhoria.

O texto deve ser público, respeitoso, técnico e útil para os autores.
Não inclua comentários confidenciais ao comitê.
Não invente dados ou resultados.
```

---

## 18.3 Prompt para `Comments to Committee.txt`

```text
Você é um avaliador sênior escrevendo comentários confidenciais para o comitê do programa.

Leia o paper anexado, considere o resumo preliminar do paper e considere também os comentários preparados para os autores.

Siga rigorosamente as instruções da skill2.md, intitulada Program Committee Review Comments.

Sua tarefa é produzir comentários técnicos, críticos e confidenciais ao comitê.

O comentário deve avaliar:

1. Síntese crítica do artigo.
2. Aderência ao escopo da conferência ou periódico.
3. Relevância científica.
4. Originalidade.
5. Robustez metodológica.
6. Confiabilidade dos resultados.
7. Riscos e ameaças à validade.
8. Fragilidades críticas.
9. Potencial impacto da publicação.
10. Recomendação editorial justificada.

O texto pode ser mais direto e estratégico do que os comentários aos autores.
Diferencie claramente o que é observação pública do que é preocupação confidencial.
Não invente informações.
```

---

## 18.4 Prompt para resumo de `Comments to Authors.txt`

```text
Resuma o conteúdo abaixo para no máximo 5000 caracteres.

Preserve os pontos mais importantes da avaliação aos autores, incluindo:

1. Síntese do artigo.
2. Principais pontos fortes.
3. Principais pontos fracos.
4. Observações metodológicas centrais.
5. Sugestões de melhoria.
6. Conclusão avaliativa.

Mantenha tom técnico, crítico, respeitoso e construtivo.

O resultado final deve ter no máximo 5000 caracteres, contando espaços.
Não inclua texto adicional fora do resumo.
```

---

## 18.5 Prompt para resumo de `Comments to Committee.txt`

```text
Resuma o conteúdo abaixo para no máximo 5000 caracteres.

Preserve os pontos mais relevantes para decisão editorial, incluindo:

1. Síntese crítica do artigo.
2. Avaliação geral.
3. Contribuição científica.
4. Fragilidades metodológicas.
5. Riscos para aceitação/publicação.
6. Pontos fortes.
7. Pontos fracos.
8. Recomendação ao comitê.

Mantenha o caráter confidencial e técnico do comentário.

O resultado final deve ter no máximo 5000 caracteres, contando espaços.
Não inclua texto adicional fora do resumo.
```

---

## 19. Requisitos Funcionais

| Código | Requisito |
|---|---|
| RF01 | A aplicação deve permitir cadastro de usuários. |
| RF02 | A aplicação deve permitir login com e-mail e senha. |
| RF03 | A aplicação deve autenticar usuários com JWT. |
| RF04 | A aplicação deve permitir upload de `paper.pdf`. |
| RF05 | A aplicação deve validar o arquivo PDF enviado. |
| RF06 | A aplicação deve manter `skill1.md` e `skill2.md` no backend. |
| RF07 | A aplicação deve executar o pipeline após o upload. |
| RF08 | A aplicação deve integrar o backend à API da OpenAI. |
| RF09 | A aplicação deve enviar o paper à OpenAI para leitura e análise. |
| RF10 | A aplicação deve gerar `Paper_Summary.txt`. |
| RF11 | A aplicação deve gerar `Comments to Authors.txt`. |
| RF12 | A aplicação deve gerar `Comments to Committee.txt`. |
| RF13 | A aplicação deve gerar resumo dos comentários aos autores com até 5000 caracteres. |
| RF14 | A aplicação deve gerar resumo dos comentários ao comitê com até 5000 caracteres. |
| RF15 | A aplicação deve validar localmente o limite de 5000 caracteres. |
| RF16 | A aplicação deve salvar todos os artefatos em disco. |
| RF17 | A aplicação deve persistir metadados e resultados no SQLite. |
| RF18 | A aplicação deve listar apenas papers do usuário autenticado. |
| RF19 | A aplicação deve permitir visualização dos resultados. |
| RF20 | A aplicação deve permitir download dos resultados. |
| RF21 | A aplicação deve impedir acesso a papers e análises de outros usuários. |
| RF22 | A aplicação deve registrar modelo OpenAI usado e status da análise. |

---

## 20. Requisitos Não Funcionais

| Código | Requisito |
|---|---|
| RNF01 | A aplicação deve proteger senhas com hash seguro. |
| RNF02 | A chave da OpenAI deve ficar apenas no backend. |
| RNF03 | A aplicação deve separar frontend e backend. |
| RNF04 | O backend deve ser modular e organizado por rotas, serviços, schemas e modelos. |
| RNF05 | A aplicação deve permitir migração futura de SQLite para PostgreSQL. |
| RNF06 | A interface deve ser responsiva com Bootstrap 5.3. |
| RNF07 | A aplicação deve preservar os artefatos completos para auditoria. |
| RNF08 | A aplicação deve registrar logs técnicos sem expor conteúdo sensível. |
| RNF09 | O modelo OpenAI deve ser configurável por variável de ambiente. |
| RNF10 | O sistema deve tratar falhas de timeout, rede, limite de taxa e erro da API. |
| RNF11 | O sistema deve permitir reprocessamento futuro do paper. |
| RNF12 | O sistema deve garantir isolamento por usuário em todas as consultas. |
| RNF13 | O backend deve validar tipo, extensão e tamanho do arquivo enviado. |
| RNF14 | O frontend não deve acessar diretamente a API da OpenAI. |

---

## 21. Execução Síncrona e Assíncrona

## 21.1 Versão Inicial

A primeira versão pode usar `FastAPI BackgroundTasks`.

Fluxo:

```text
Upload → cria registro → inicia tarefa em background → dashboard consulta status
```

## 21.2 Versão Recomendada para Produção

Para produção, recomenda-se usar fila de tarefas:

```text
Celery + Redis
RQ + Redis
Dramatiq + Redis
```

Fluxo:

```text
Upload → job na fila → worker executa pipeline → banco é atualizado → frontend consulta status
```

---

## 22. Critérios de Aceitação

A aplicação será considerada funcional quando:

1. Um usuário conseguir se cadastrar.
2. Um usuário conseguir fazer login.
3. O backend retornar JWT válido.
4. Um usuário autenticado conseguir enviar um PDF.
5. O backend salvar o PDF no diretório correto.
6. O backend carregar `skill1.md` e `skill2.md`.
7. O backend enviar o PDF à OpenAI.
8. O pipeline gerar `Paper_Summary.txt`.
9. O pipeline gerar `Comments to Authors.txt`.
10. O pipeline gerar `Comments to Committee.txt`.
11. O pipeline gerar os dois resumos finais com até 5000 caracteres.
12. Os arquivos forem salvos em `outputs/user_id/paper_id/`.
13. Os resultados forem persistidos no SQLite.
14. O dashboard listar somente papers do usuário logado.
15. A tela de detalhes exibir os resumos finais.
16. O usuário conseguir baixar seus resultados.
17. Um usuário não conseguir acessar papers ou análises de outro usuário.
18. O status do paper refletir corretamente `uploaded`, `processing`, `completed` ou `failed`.

---

## 23. Resultado Final Esperado

Para cada paper analisado, a aplicação deverá produzir:

```text
Paper_Summary.txt
Comments to Authors.txt
Comments to Committee.txt
Comments to Authors - Summary 5000 chars.txt
Comments to Committee - Summary 5000 chars.txt
```

Além disso, deverá persistir:

```text
user_id
paper_id
status
openai_file_id
model_used
paths dos arquivos gerados
texto resumido dos comentários aos autores
texto resumido dos comentários ao comitê
datas de início e fim da análise
mensagem de erro, quando houver
```

A regra principal de segurança é:

```text
Cada usuário só pode acessar seus próprios papers, suas próprias análises e seus próprios resultados.
```

---

## 24. Síntese Final da Solução

A aplicação final será uma plataforma web de análise automatizada de papers científicos, com frontend Flask e backend FastAPI. O usuário autenticado fará upload de um paper em PDF, e o backend usará skills locais para orientar chamadas à API da OpenAI. A OpenAI será responsável pela leitura e interpretação do paper e pela geração dos artefatos textuais do pipeline. O backend será responsável por orquestrar o processo, validar os resultados, salvar arquivos, persistir dados e proteger o acesso por usuário.

A arquitetura proposta permite uma primeira versão local simples, usando SQLite e armazenamento em disco, mas mantém separação suficiente para evoluir futuramente para PostgreSQL, filas assíncronas, workers dedicados, armazenamento em nuvem e controle administrativo das skills.
