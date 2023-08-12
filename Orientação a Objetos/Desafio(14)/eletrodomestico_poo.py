"""
14 - Escreva um código que apresente a classe "Eletrodomestico", com atributo "ligado" e o método "imprimir". O
método "imprimir" deve mostrar na tela os valores de todos os atributos. O atributo "ligado" será booleano e deverá
indicar o estado atual do eletrodoméstico, se ele está ligado ou desligado.
"""


# Classe "Eletrodomestico".
class Eletrodomestico:

    # Método construtor:
    def __init__(self, ligado):
        if type(ligado) != bool:
            raise TypeError("O atributo ligado deve ser do tipo booleano.")
        else:
            self.__ligado = ligado

    # Método "imprimir".
    def imprimir(self):
        print(f' Ligado: {self.__ligado}')


# Testando.
eletrodomestico1 = Eletrodomestico(True)

eletrodomestico1.imprimir()  # OUTPUT: Ligado: True
