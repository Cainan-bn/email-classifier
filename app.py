from flask import Flask, render_template, request
from ai_service import analisar_emails_em_lote
import pdfplumber
import re
app = Flask(__name__)


def separar_emails(texto):
    texto = texto.strip()

    partes = re.split(r"\n?\s*\d+\s*[-.)]\s*", texto)
    emails = [p.strip() for p in partes if p.strip()]

    if len(emails) > 1:
        return emails

    
    partes = re.split(r"\n\s*\n", texto)
    emails = [p.strip() for p in partes if p.strip()]

    if len(emails) > 1:
        return emails

   
    partes = texto.split("\n")
    emails = [p.strip() for p in partes if p.strip()]

    return emails




def extrair_texto_pdf(file):
    texto = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            texto += page.extract_text() + "\n"
    return texto


@app.route("/", methods=["GET", "POST"])
def index():
    resultados = []

    if request.method == "POST":
        emails = []

        
        email_texto = request.form.get("email_texto", "").strip()
        if email_texto:
            emails.extend(separar_emails(email_texto))

        
        arquivo = request.files.get("email_arquivo")

        if arquivo and arquivo.filename:
            if arquivo.filename.endswith(".txt"):
                conteudo = arquivo.read().decode("utf-8")
                emails.extend(separar_emails(conteudo))

            elif arquivo.filename.endswith(".pdf"):
                conteudo = extrair_texto_pdf(arquivo)
                emails.extend(separar_emails(conteudo))

        
        if emails:
            resultados = analisar_emails_em_lote(emails)

    return render_template("index.html", resultados=resultados)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)