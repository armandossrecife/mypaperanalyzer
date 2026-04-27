# 🛠️ Especificação Técnica: Paper Analyzer AI

## 1. Visão Geral
O **Paper Analyzer AI** é um sistema de software distribuído projetado para automatizar a revisão técnica de artigos científicos. Ele utiliza uma arquitetura baseada em microsserviços (conceitualmente separada em Frontend e Backend) para processar documentos PDF através de uma pipeline de inteligência artificial de alta precisão.


## 2. Requisitos do Sistema

### 2.1 Requisitos Funcionais (RF)
| ID | Requisito | Descrição |
| :--- | :--- | :--- |
| RF01 | Autenticação Segura | O sistema deve permitir autenticação via JWT com senhas criptografadas (Bcrypt). |
| RF02 | Upload de Documentos | Suporte a arquivos PDF de até 30MB com validação de integridade. |
| RF03 | Pipeline Sequencial | Execução automática de: Resumo Técnico -> Revisão para Autores -> Avaliação para Comitê -> Súmulas Executivas. |
| RF04 | Gestão de Contexto | Uso de "Skills" (diretrizes de avaliação) injetadas como contexto de sistema. |
| RF05 | Dashboard de Status | Visualização do progresso da análise (Uploaded -> Processing -> Completed). |
| RF06 | Observabilidade | Logs detalhados de cada interação com a API da OpenAI para auditoria técnica. |

### 2.2 Requisitos Não Funcionais (RNF)
- **RNF01 (Tecnologia)**: O backend deve ser construído em **Python 3.13** com **FastAPI**.
- **RNF02 (Performance)**: Chamadas de IA devem ser executadas em background para não travar a UI.
- **RNF03 (Escalabilidade)**: O storage deve ser organizado por `user_id` e `paper_id`.
- **RNF04 (Resiliência)**: Implementação de *Polling* para garantir que arquivos PDFs estejam indexados no Vector Store antes da análise.

## 3. Arquitetura de Software

### 3.1 Diagrama de Fluxo
`Usuário (Browser) -> Frontend (Flask) -> API Gateway (FastAPI) -> Background Task -> OpenAI Responses API -> Storage Local`

### 3.2 Camadas do Backend
1. **API Layer**: Rotas REST (Auth, Papers, Analyses).
2. **Service Layer**: Lógica de negócio (OpenAI Bridge, File Service, Pipeline Orchestrator).
3. **Database Layer**: SQLAlchemy ORM gerenciando SQLite (`paper_review.db`).
4. **Storage Layer**: Pasta `storage/` contendo arquivos planos (.pdf e .txt).

### 3.3 Camadas do Frontend
1. **Flask App**: Gestão de rotas e sessões de usuário (`app.py`).
2. **Jinja2 Templates**: Estrutura moderna (Bootstrap 5.3) com Dark Mode persistente.
3. **Async JS**: Script de monitoramento de status e busca de logs via AJAX/Fetch.


## 4. Engenharia de Integração IA (OpenAI)

### 4.1 Responses API Design
A aplicação utiliza a **Responses API (Experimental)** da OpenAI:
- **Criação de Conversas**: Uso de sessões persistentes via IDs `conv_...`, gerenciadas por um scanner recursivo de atributos.
- **File Search Tool**: Ativação da ferramenta de busca semântica sobre os documentos.
- **Vector Stores**: Criação de um banco de vetores dedicado para cada paper para garantir isolamento e precisão.

### 4.2 Pipeline de 6 Etapas
1. **Step 1: Summary** -> Geração da base de conhecimento do artigo.
2. **Step 2: Authors Feedback** -> Feedback construtivo baseado na `skill1.md`.
3. **Step 3: Committee Feedback** -> Avaliação ética e confidencial baseada na `skill2.md`.
4. **Step 4: Summary for Authors** -> Compressão do feedback (max 5000 chars).
5. **Step 5: Summary for Committee** -> Compressão da revisão editorial (max 5000 chars).
6. **Step 6: Finalization** -> Persistência final de logs técnicos (tokens, modelo, etc).

## 5. Estrutura de Storage
`backend/storage/outputs/user_{id}/paper_{id}/`

Arquivos geradores:
- `Paper_Summary.txt`
- `Comments to Authors.txt`
- `Comments to Committee.txt`
- `Comments to Authors - Summary 5000 chars.txt`
- `Comments to Committee - Summary 5000 chars.txt`

## 6. Segurança e Estabilidade
- **Timezone Aware**: Datas de upload ajustadas para o horário local do servidor.
- **Atomic Concurrency**: Garantia de que logs de erro sejam gravados mesmo em falhas de falha crítica na API da OpenAI.
- **Recursive ID Tracking**: Resiliência contra mudanças de formato no JSON de resposta da OpenAI.

**Data**: 26 de Abril de 2026
**Versão**: 2.1
