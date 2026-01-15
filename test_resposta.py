from ai_service import classificar_email, gerar_resposta

email = """
Olá,

Meu acesso ao sistema está bloqueado desde ontem.
Poderiam verificar, por favor?

Obrigado.
"""

categoria = classificar_email(email)
resposta = gerar_resposta(email, categoria)

print("Categoria:", categoria)
print("\nResposta sugerida:\n")
print(resposta)
