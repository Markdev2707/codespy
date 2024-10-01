from biblioteca import(validar_email, validar_senha)
email = input('Digite email: ')


if validar_email(email):
    print("Email Válido.")
else:
    print('Email invalido!')
