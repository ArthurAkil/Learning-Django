# Learning-Django

Repositório de estudos e experimentos com **Django**, framework web em Python.

---

## 🧠 Visão Geral

Esse repositório serve como um espaço para praticar, explorar e documentar conceitos importantes do Django, como:

- Criação de aplicações com Models, Views e Templates  
- Estrutura de pastas típica de projetos Django  
- Rotas (`urls.py`), formulários e interação com banco de dados  
- Uso da interface administrativa (admin) do Django  
- Integração com Django REST Framework (quando aplicável)  
- Boas práticas de organização, migrações e deploys simples

---

## 📁 Estrutura do Projeto

<pre>
Learning-Django/
   ├── Curso_1/
      ├── Outros_exercícios, seções ou apps de estudo/
   ├── Curso_2_incluso_DRF/
      ├── Outros exercícios, seções ou apps de estudo/
   ├── README.md
</pre>


- Cada pasta (como `Curso_1`, `Curso_2_incluso_DRF`) contém exercícios, apps ou exemplos específicos.  
- O arquivo `requirements.txt` reúne as dependências usadas no(s) projeto(s).

---

## 🚀 Como Executar Localmente

1. Clone o repositório  
   ```bash
   git clone https://github.com/ArthurAkil/Learning-Django.git
   cd Learning-Django

2. Crie e ative um ambiente virtual
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Linux/macOS
   # ou no Windows:
   venv\Scripts\activate

4. Instale as dependências
   ```bash
   pip install -r requirements.txt

6. Aplique as migrações e rode o servidor
   ```bash
   python manage.py migrate
   python manage.py runserver

8. Abra o navegador em:
   ```bash
   http://127.0.0.1:8000/

## O.B.S.: Alguns projetos podem estar usando docker, por tanto dê uma olhada no projeto que for puxar. Além disso caso queira baixar apenas uma pasta específica do projeto utilize: 
🌐 Sites que permitem baixar só uma pasta

DownGit → você cola a URL da pasta do repositório e ele gera um link para download só daquela pasta em .zip.
GitHub Folder Downloader → funciona parecido: cole a URL da pasta e ele baixa só ela.

## ✅ Funcionalidades Implementadas

1. CRUD básico via modelos, views e formulários

2. Templates com herança e includes para reutilização de layout

3. Rotas estruturadas por app com urls.py

4. Interface administrativa (Django Admin) para gestão dos dados

## 🔧 Tecnologias e Dependências

1. Python 3.x

2. Django (versão definida em requirements.txt)

3. Outras libs conforme exercícios (ex.: Django REST Framework)

## 📅 Status & Roadmap

Este repositório está em desenvolvimento contínuo.
Possíveis próximos passos:

1. Criar testes automatizados (unitários e integração)

2. Adicionar autenticação e autorização de usuários

3. Melhorar documentação interna dos apps (README em cada pasta)

4. Exemplos de deploy em produção

## 🤝 Contribuições

Contribuições são bem-vindas!

1. Faça um fork deste repositório

2. Crie uma branch para sua funcionalidade/correção:
   ```bash
   git checkout -b feature/nome-da-feature

3. Commit e push:
   ```bash
   git commit -m "Descrição da mudança"
   git push origin feature/nome-da-feature

4. Abra um Pull Request explicando suas alterações


## 📚 Recursos de Estudo

Documentação oficial do Django e UDEMY
