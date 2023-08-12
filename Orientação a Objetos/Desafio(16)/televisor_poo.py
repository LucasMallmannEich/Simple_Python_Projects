"""
16 - Escreva um código que apresente a classe "Televisor", com atributos "ligado", "canal" e "volume". Além disso, a
classe deve apresentar o método "imprimir". O método "imprimir" deve mostrar na tela os valores de todos os atributos. O
atributo "ligado" será boleano e deverá indicar o estado atual do televisor, se ligado ou desligado. O atributo "canal"
deverá indicar o canal atual em que o televisor está sintonizado. O atributo volume deverá indicar o volume atual do
televisor.
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

    # Método "imprimir".
    def imprimir(self):
        print(f' Ligado: {self.__ligado} \t Canal: {self.__canal} \t Volume: {self.__volume}')


# Testando.
televisor1 = Televisor(True, 595, 8)

televisor1.imprimir()  # OUTPUT: Ligado: True 	 Canal: 595 	 Volume: 8
