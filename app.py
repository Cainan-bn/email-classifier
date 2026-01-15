from flask import Flask, render_template, request
from ai_service import classificar_email, gerar_resposta

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    categoria = None
    resposta = None
    email_texto = ""

    if request.method == "POST":
        email_texto = request.form.get("email_texto")

        if email_texto:
            categoria = classificar_email(email_texto)
            resposta = gerar_resposta(email_texto, categoria)

    return render_template(
        "index.html",
        categoria=categoria,
        resposta=resposta,
        email_texto=email_texto
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)