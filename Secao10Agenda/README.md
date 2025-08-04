# Secao10Agenda 📅

Projeto desenvolvido durante os estudos com Django, com foco em criação de uma agenda de contatos com autenticação, filtros, imagens e outras funcionalidades práticas de um sistema CRUD.

## 🛠 Tecnologias usadas

- Python
- Django
- SQLite3 (banco de dados padrão)
- HTML/CSS

## 📦 Instalação
```bash

1. Clone o repositório:

git clone https://github.com/ArthurAkil/Learning-Django.git
cd Learning-Django/Secao10Agenda

2. Crie e ative um ambiente virtual:

python -m venv venv

# Windows:
venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate

3. Instale as dependências:

pip install -r requirements.txt

4. Rode as migrações:

python manage.py migrate

5. Crie um superusuário (opcional, apenas para acessar o admin):

python manage.py createsuperuser

6. Acesse: http://127.0.0.1:8000

📷 Funcionalidades

    Cadastro e listagem de contatos

    Autenticação de usuários

    Filtros por nome, telefone e e-mail

    Upload de imagens para os contatos

    Visualização individual de cada contato

📁 Estrutura principal

    Secao10Agenda/
    ├── contact/           # App principal
    ├── project/           # Configurações do projeto
    ├── media/             # Imagens dos contatos
    ├── static/            # Arquivos estáticos
    └── templates/         # HTMLs
