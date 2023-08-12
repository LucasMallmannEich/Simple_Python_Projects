"""
17 - Baseando-se no exercício anterior, adicione os métodos "ligar" e "desligar", que deverão mudar o conteúdo do
atributo "ligado" conforme o caso.
"""


# Classe "Televisor".
class Televisor:

    # Método construtor.
    def __init__(self, ligado, canal, volume):
        if type(ligado) != bool:
            raise TypeError("O atributo ligado deve ser do tipo booleano.")
        elif type(canal) != int or type(volume) != int:
            raise TypeError("Os atributos canal e volume devem receber números inteiros.")
        elif canal < 1 or volume < 0:
            raise ValueError("O menor número possível para o canal é 1 e para o volume é 0.")
        else:
            self.__ligado = ligado
            self.__canal = canal
            self.__volume = volume

    # Método "ligar".
    def ligar(self):
        self.__ligado = True

    # Método "desligar".
    def desligar(self):
        self.__ligado = False

    # Método "imprimir".
    def imprimir(self):
        print(f' Ligado: {self.__ligado} \t Canal: {self.__canal} \t Volume: {self.__volume}')


# Testando.
televisor1 = Televisor(True, 595, 8)

televisor1.imprimir()  # OUTPUT: Ligado: True 	 Canal: 595 	 Volume: 8

televisor1.desligar()  # Ligado: False

televisor1.imprimir()  # OUTPUT: Ligado: False 	 Canal: 595 	 Volume: 8
