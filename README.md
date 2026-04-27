# 📝 Paper Analyzer AI

A premium, modern web application designed for high-precision scientific paper analysis. Leveraging the experimental **OpenAI Responses API** and the cutting-edge **gpt-5-mini** model, this tool automates the rigorous 6-step review pipeline typically performed by conference committees.

## 🚀 Key Features

- **Sequential Analysis Pipeline**: Automated 6-step workflow:
  1. 📄 **Technical Summary**: Deep extraction of theme, objective, methodology, and results.
  2. 👥 **Authors Review**: Critical feedback based on specific scientific skills.
  3. 🏛️ **Committee Review**: Confidential technical evaluation for editorial decisions.
  4. 🖋️ **Executive Summaries**: High-level synthesis of all group reviews.
- **Contextual Scientific Skills**: Integrates PDF content with custom-defined evaluation guidelines (Skills) via OpenAI Vector Stores.
- **Full Observability**: Real-time logging of every API Request/Response/Error for maximum transparency.
- **Secure Architecture**: JWT-based authentication with local-first data storage.
- **Premium UI/UX**: Sleek interface built with Flask and Bootstrap 5.3, featuring persistence for dark/light mode and dynamic progress tracking.

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Backend** | Python 3.13, FastAPI, SQLAlchemy, Uvicorn |
| **Frontend** | Flask, Bootstrap 5.3, Javascript, FontAwesome |
| **Database** | SQLite (Local storage) |
| **AI Engine** | OpenAI Responses API (**gpt-5-mini**) |
| **Process Management** | UV (Fast Python package manager) |

## 📂 Project Structure

```bash
.
├── backend/            # FastAPI Core, Models & Analysis Logic
│   ├── app/            # Main application directory
│   │   ├── api/        # REST Endpoints
│   │   ├── services/   # AI Pipeline & File Logic (Key: openai_service.py)
│   │   └── db/         # SQLAlchemy Models & Migrations
│   └── storage/        # Local persistent storage for PDFs and Outputs
├── frontend/           # Flask Presentation Layer
│   ├── static/         # CSS/JS/Image assets
│   └── templates/      # Jinja2 Layouts & Pages
└── README.md           # Documentation
```


## ⚙️ Installation & Setup

### Prerequisites
- [uv](https://github.com/astral-sh/uv) (Recommended) or `pip`
- OpenAI API Key

### 1. Root Configuration
Copy the environment template and configure your keys:
```bash
cp .env.example .env
# Edit .env with your OPENAI_API_KEY and set OPENAI_MODEL=gpt-5-mini
```

### 2. Backend Setup
```bash
cd backend
uv sync
uv run python main.py
```
*API will be available at `http://localhost:8000/docs`*

### 3. Frontend Setup
```bash
cd frontend
uv sync
uv run python app.py
```
*Dashboard will be available at `http://localhost:5000`*

## 🛡️ Reliability & Innovation
- **Recursive Conversational Logic**: Implements a unique recursive scanner to handle dynamic OpenAI `conv_` IDs.
- **Atomic Operations**: Ensures database state is consistent even if API steps fail.
- **Safe Dates**: Automatic handling of user-local timezones for accurate upload records.

## ⚖️ License
Internal Use / Research Project.