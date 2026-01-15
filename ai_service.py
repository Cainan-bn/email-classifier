import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classificar_email(texto_email: str) -> str:
    prompt = f"""
Você é um assistente que classifica emails corporativos.

Classifique o email abaixo como APENAS uma das opções:
- Produtivo
- Improdutivo

Email:
\"\"\"{texto_email}\"\"\"

Responda APENAS com a palavra: Produtivo ou Improdutivo.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    resultado = response.choices[0].message.content.strip()

    if "produtivo" in resultado:
        return "Produtivo"
    else:
        return "Improdutivo"
    


def gerar_resposta(texto_email: str, categoria: str) -> str:
    if categoria == "Produtivo":
        prompt = f"""
Você é um assistente corporativo.

Gere uma resposta profissional, clara e objetiva para o email abaixo.
A resposta deve indicar que a solicitação foi recebida e que será analisada.

Email:
\"\"\"{texto_email}\"\"\"
"""
    else:
        prompt = f"""
Você é um assistente corporativo.

Gere uma resposta educada e cordial para o email abaixo.
A resposta não deve indicar abertura de chamado ou ação futura.

Email:
\"\"\"{texto_email}\"\"\"
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()