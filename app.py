from poo22102024 import (Veiculos, )
#Criar os objetos ----------------------------------------------------------

chevette = Veiculos(
    140,
    "GM",
    "Chevette Hatch",
    1890
)

print(f"Velocidade Atual = {chevette.velo_atual} ")
print(f"Ligando o Carro {chevette.ligar_desligar()}")

for aceleracao in range (14):
    chevette.acelerar()
    print(f"==> {chevette.velo_atual}, (v) -> {chevette.cambio()}")

chevette.ligar_desligar()
print(f"Ligado? {chevette.ligado}")




for freando in range (14):
    chevette.frea()
    print(f"--> {chevette.velo_atual}")


