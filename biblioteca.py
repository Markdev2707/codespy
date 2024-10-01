def conta_palavras(texto):
    lista = texto.split()
    return len(lista)

def validar_email(email):
    qt = email.count('@') #função que conta quantos @ tem no texto.
    if qt != 1:
        return False # Se a quantidade de ! for diferente de 1 ele retorna falso.
    
    lista = email.split('@') #O split pegou o email e dividiu em dois e colocamos e o if no index 1.

    if not '.' in lista[1] and '_' in email:
        return False
    
    return True

def validar_senha(texto):
    if len(texto) < 8:
        return False
    
    if not('@' or '!' or '?') in texto:
        return False
    
    return True 