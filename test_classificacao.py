from ai_service import classificar_email

email_produtivo = """
Olá, tudo bem?

Poderiam me informar o andamento do chamado #4589?
Estou aguardando retorno.

Obrigado.
"""

email_improdutivo = """
Bom dia pessoal!

Passando apenas para desejar um ótimo final de semana 😊
Abraços!
"""

print("Email 1:", classificar_email(email_produtivo))
print("Email 2:", classificar_email(email_improdutivo))
