from dotenv import load_dotenv
import os
from openai import OpenAI
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analisar_emails_em_lote(lista_emails):
    """
    Recebe uma lista de emails e retorna classificação e resposta para cada um
    em uma única chamada à API.
    """

    emails_formatados = ""
    for i, email in enumerate(lista_emails, start=1):
        emails_formatados += f"\nEMAIL {i}:\n{email}\n"

    prompt = f"""
Você é um assistente corporativo especializado em análise de emails.

Tarefa:
- Para CADA email abaixo, faça:
  1. Classificação: "Produtivo" ou "Improdutivo"
  2. Gere uma resposta automática adequada

Regras:
- Retorne APENAS um JSON válido
- Não inclua explicações fora do JSON
- Use exatamente este formato:

[
  {{
    "email_id": 1,
    "categoria": "Produtivo",
    "resposta": "texto da resposta"
  }}
]

Emails para análise:
{emails_formatados}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    conteudo = response.choices[0].message.content.strip()

    return json.loads(conteudo)
