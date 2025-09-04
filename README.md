# 🗂️ Trello Clone (Flask)

Projeto simples em **Flask** que simula um mini-Trello: cadastro/login de usuários e CRUD de tarefas com status (pendente, em andamento, concluída). Usa **SQLite** como banco local.

## 🚀 Como rodar

```bash
# Clone o repositório e entre na pasta
git clone https://github.com/seu-usuario/trello.git
cd trello

# Crie e ative o ambiente virtual
# Windows
python -m venv venv && venv\Scripts\activate
# Linux/Mac
python3 -m venv venv && source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Rode o servidor
flask run
# Acesse: http://127.0.0.1:5000
