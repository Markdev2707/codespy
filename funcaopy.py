'''importando a biblioteca criada em outra página. biblioteca.py'''
from biblioteca import (tira_duplicata) 
'''outra forma de puxar as função da biblioteca.'''
'''import biblioteca as bib'''


'''def par_impar(arg:int) -> bool:
 
    Esta função serve para verificar se um número é par ou impar.
  
    if arg % 2 == 0:
        return True
    else:
        return False
    
x = int(input("Digite: "))

print(par_impar(x))
'''
'''-----------------------------------------------------------------'''

'''def vogal(caracter:str) -> bool:
    
    Esta função serve para verificar se a exite vogal no que foi digitado.

    if caracter in "aeiou":
        return True
    else:
        return False
    
palavra = input("Digite algo: ").lower()

print(vogal(palavra))'''


'''-----------------------------Puxando função da biblioteca para resolver o problema------------------------------------'''

'''largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

print(area_retangulo(largura, altura))'''


'''---------------------------------Contador de palavras----------------------------------'''
'''-----Puxando da biblioteca-----'''

'''palavra = input("Digite uma frase: ")
    
print(len(contador_letra(palavra)))'''

'''-----------------------------------------------'''

'''função que recebe lista de email e retorna a lista sem duplicação'''

lista_emails = ["ana@gmail.com", "pedro@hotmail", "ana@gmail.com"]

print(tira_duplicata(lista_emails))