#   POO
#   1º Abstração
#   2º Herança
#   3º Polimorfismo 

'''
Programação Orientada a Objeto
'''

class Veiculos:
    # Método construtor:
     # Em python o método construtor sempre começa assim. _ _init_ _(self).
    def __init__(self, velo_max, marca, modelo, ano, ):
        self.velo_max = velo_max
        self.velo_atual = 0
        self.ligado = False
        self.marca = marca
        self.modelo = modelo
        self.fab = ano


# Método frear:
    def frea(self):
        if self.velo_atual - 10 >= 0:
            self.velo_atual -= 10
        else:
            self.velo_atual = 0

# Método acelerar;
    def acelerar(self):
        if self.velo_atual + 10 <= self.velo_max and (self.ligado):
            self.velo_atual += 10
        elif(self.velo_atual+10 > self.velo_max) and (self.ligado):
            self.velo_atual = self.velo_max

    def ligar_desligar(self):
        if(not self.ligado)  and self.velo_atual == 0:
            self.ligado = True
        elif (self.ligado) and (self.velo_atual == 0):
            self.ligado = False

    def cambio(self):
        if self.velo_atual < 40:
            return f"1ª Marcha"
        elif self.velo_atual < 60:
            return f"2ª Marcha"
        elif self.velo_atual < 80:
            return f"3ª Marcha"
        elif self.velo_atual < 95:
            return f"4ª Marcha"
        elif self.velo_atual < 110:
            return f"5ª Marcha"
            
                


        
                
            

    


                       