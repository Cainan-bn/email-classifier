
# 📧 AutoU – Classificador Inteligente de Emails

Aplicação web desenvolvida como **desafio técnico de estágio da AutoU**, com o objetivo de classificar emails automaticamente como **Produtivo** ou **Improdutivo**, utilizando **Inteligência Artificial** e **Processamento de Linguagem Natural (NLP)**.

O sistema permite que qualquer usuário acesse via navegador, cole o conteúdo de um email e receba instantaneamente a classificação, **sem necessidade de instalação local**.

---

## 🚀 Demonstração

🔗 **Link da aplicação (Deploy):**
> *(será inserido após o deploy no Render)*

🎥 **Vídeo demonstrativo:**
> *(link a ser adicionado)*

---

## 🧠 Como funciona

1. O usuário cola o texto do email na interface web
2. O backend em **Flask (Python)** envia o texto para uma **API de IA**
3. A IA analisa o conteúdo e classifica como:
   - ✅ **Produtivo**
   - ❌ **Improdutivo**
4. O resultado é exibido de forma clara na tela

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **OpenAI API**
- **HTML5 / CSS3**
- **Python-dotenv**
- **Gunicorn** (produção)
- **Render** (deploy)

---

## 📁 Estrutura do Projeto

```
autou-email-classifier/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
```

---

## 🔐 Segurança

A chave da API da OpenAI **não é exposta no código**.

Ela é armazenada:
- Localmente via arquivo `.env`
- Em produção via **Environment Variables** no Render

---

## ▶️ Executar Localmente

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/autou-email-classifier.git
cd autou-email-classifier
```

### 2️⃣ Criar e ativar ambiente virtual
```bash
python -m venv .venv
source .venv/Scripts/activate  # Git Bash / Linux / Mac
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Criar arquivo `.env`
```env
OPENAI_API_KEY=sua_chave_aqui
```

### 5️⃣ Executar aplicação
```bash
python app.py
```

Acesse:
```
http://127.0.0.1:5000
```

---

## 🌐 Deploy

A aplicação é publicada na nuvem utilizando **Render**, permitindo acesso público sem instalação local.

---

## 👨‍💻 Autor

**Cainã Barros do Nascimento**  
Desenvolvedor | Engenharia de IA | Full Stack  
📍 Brasil

---

## 🏁 Considerações Finais

Este projeto demonstra:
- Integração prática com IA Generativa
- Boas práticas de segurança
- Deploy funcional em nuvem
- Foco em experiência do usuário

Desenvolvido exclusivamente para o **desafio técnico da AutoU**.
