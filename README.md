# 📧 Classificador Inteligente de Emails com IA

Projeto desenvolvido com foco em **IA aplicada, NLP, experiência do usuário e deploy em nuvem**.

A aplicação analisa emails (texto direto, `.txt` ou `.pdf`), **classifica cada email como Produtivo ou Improdutivo** e **gera uma resposta automática individual para cada um**, utilizando a API da OpenAI.

---

🖼️ **Interface da aplicação:**

> 📌 *Screenshot da interface principal*

```
/static/screenshot-interface.png
```

---

## 🧠 Funcionalidades

- ✅ Classificação automática de emails com IA
- ✅ Geração de resposta personalizada para **cada email**
- ✅ Entrada por:
  - Texto digitado
  - Upload de arquivo `.txt`
  - Upload de arquivo `.pdf`
- ✅ Processamento em lote (vários emails de uma vez)
- ✅ Interface web simples e intuitiva
- ✅ Deploy em nuvem (Render)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Flask** – backend web
- **OpenAI API** – análise e geração de respostas
- **pdfplumber** – leitura de PDFs
- **HTML + CSS** – interface
- **Render** – deploy em produção

---

## 📂 Estrutura do Projeto

```bash
autou-email-classifier/
│
├── app.py                 # Aplicação Flask
├── ai_service.py          # Lógica de IA (OpenAI)
├── requirements.txt       # Dependências
├── .env.example           # Exemplo de variáveis de ambiente
│
├── templates/
│   └── index.html         # Interface web
│
├── static/
│   ├── style.css          # Estilos
│   └── screenshot-interface.png
│
└── README.md
```

---

## ⚙️ Configuração Local

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/Cainan-bn/email-classifier.git
cd autou-email-classifier
```

### 2️⃣ Crie o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure a API Key

Crie um arquivo `.env`:

```env
OPENAI_API_KEY=sua_api_key_aqui
```


---

## ▶️ Executando o Projeto

```bash
python app.py
```

Acesse no navegador:

```
http://127.0.0.1:5000
```

---

## 🧪 Como Usar

### ✍️ Texto direto
Cole um ou mais emails separados por **linha em branco** ou enumerados.

### 📄 Arquivo `.txt`
Cada email deve estar separado por uma linha em branco ou enumerados.

### 📕 Arquivo `.pdf`
O sistema extrai o texto e processa automaticamente.

---

## 🤖 Lógica de IA (Resumo)

- Os emails são processados **em lote**
- A IA retorna:
  - Categoria (Produtivo / Improdutivo)
  - Resposta automática adequada
- O resultado é exibido individualmente na interface

---

## 📌 Observações Importantes

- O projeto respeita limites de requisição da API
- Em PDFs muito grandes, podem ocorrer erros de conexão temporários
- Ideal para uso demonstrativo e desafios técnicos

---

##  Autor

**Cainã Barros do Nascimento**  
Estudante de Engenharia de IA & Desenvolvimento Full Stack

<a href="https://www.linkedin.com/in/cainã-barros-0aaa0a282/" target="_blank"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn" width="40" height="40"/></a>


---

##  Considerações Finais

Este projeto demonstra:

- Integração real com API de IA
- Boas práticas de backend
- UX simples e funcional
- Deploy em produção



