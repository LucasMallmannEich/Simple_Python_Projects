"""
15 - Baseando-se no exercício anterior, adicione os métodos "ligar" e "desligar", que deverão mudar o conteúdo do
atributo "ligado" confome o caso.
"""


# Classe "Eletrodomestico".
class Eletrodomestico:

    # Método construtor:
    def __init__(self, ligado):
        if type(ligado) != bool:
            raise TypeError("O atributo ligado deve ser do tipo booleano.")
        else:
            self.__ligado = ligado

    # Método "ligar".
    def ligar(self):
        self.__ligado = True

    # Método "desligar".
    def desligar(self):
        self.__ligado = False

    # Método "imprimir".
    def imprimir(self):
        print(f' Ligado: {self.__ligado}')


# Testando.
eletrodomestico1 = Eletrodomestico(True)

eletrodomestico1.imprimir()  # OUTPUT: Ligado: True

eletrodomestico1.desligar()  # Ligado: False

eletrodomestico1.imprimir()  # OUTPUT: Ligado: False

eletrodomestico1.ligar()  # Ligado: True

eletrodomestico1.imprimir()  # OUTPUT: Ligado: True
