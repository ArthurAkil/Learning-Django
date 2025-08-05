# Learning-Django

Repositório de estudos e experimentos com **Django**, o famoso framework web em Python.

---

## 🔍 Visão Geral

Este projeto reúne exercícios, tutoriais pessoais e aplicações didáticas com o objetivo de aprender e documentar conceitos chave do Django:

- Estrutura de diretórios típicos de um projeto Django  
- Modelos, views e templates  
- Rotas, formulários e gestão de dados  
- Customizações e deploys simples

---

## 📁 Estrutura do Projeto

```text
Learning-Django/
├── <Aprendizado>/
├── <Secao10Agenda>/
├── <Secao11Blog>/ 
```

> **Observações**:  
> - `requirements.txt` lista as dependências (geralmente Django e outras libs).  
---

## 🚀 Como Executar (Local)
0. **Abra a pasta do projeto específico que deseja visualizar**  

1. **Clone o repositório da pasta**  
   ```bash
   git clone https://github.com/ArthurAkil/Learning-Django.git
   cd Learning-Django
   ```

2. **Crie e ative um virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale dependências**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique migrações e rode o servidor**  
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Acesse no navegador**  
   Vá para `http://127.0.0.1:8000/` para ver a aplicação rodando.

---

## ✅ Funcionalidades Implementadas

- CRUD básico com modelos e formulários  
- Uso de templates com herança e includes  
- Rotas configuradas em `urls.py` dos apps  
- Interface administrativa Django para gerenciamento  

---

## 🛠️ Tecnologias e Dependências

- **Python 3.x**  
- **Django (versão usada)**: especificada no `requirements.txt`  

---

## 🚧 Status e Roadmap

Este projeto está em **desenvolvimento contínuo**.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Para isso:

1. Faça um _fork_ do repositório  
2. Crie uma branch para sua alteração (`git checkout -b feature/nova-coisa`)  
3. Faça commits claros e descriptivos  
4. Envie um Pull Request (PR) com descrição das mudanças

---

## 📄 Licença

Este projeto segue a [licença padrão do desenvolvedor] ou ainda não tem licença definida. Consulte `LICENSE` se houver. Para uso próprio ou acadêmico sempre ideal verificar os termos específicos.

---

## 🧠 Recursos de Estudo

Para evolução no aprendizado de Django, recomenda-se:

- Documentação oficial do Django: https://www.djangoproject.com/start/  
- Tutorial de Django da Mozilla (MDN)  
- Livros e guias como *Django for Beginners* ou *Two Scoops of Django*  

---

## 📬 Contato

Se quiser contribuir, sugerir melhorias ou tirar dúvidas, fique à vontade para abrir uma *issue* ou entrar em contato via GitHub.

---
