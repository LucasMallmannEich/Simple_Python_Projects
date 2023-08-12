"""
18 - Baseando-se no exercício anterior, adicione os atributos "numero_canais" e "volume_maximo", onde "numero_canais" indica o
número máximo de canais que o televisor pode sintonizar e "volume_maximo" indica qual o maior nível de volume possível.
O método "imprimir" deve ser modificado de forma a mostrar na tela os valores de todos os atributos.
"""


# Classe "Televisor".
class Televisor:

    # Método construtor.
    def __init__(self, ligado, canal, volume, numero_canais, volume_maximo):
        if type(ligado) != bool:
            raise TypeError("O atributo ligado deve ser do tipo booleano.")
        elif type(canal) != int or type(volume) != int:
            raise TypeError("Os atributos canal e volume devem receber números inteiros.")
        elif canal < 1 or volume < 0:
            raise ValueError("O menor número possível para o canal é 1 e para o volume é 0.")
        elif type(numero_canais) != int or type(volume_maximo) != int:
            raise TypeError("O número de canais e o volume máximo suportado pelo televisor devem ser números inteiros.")
        elif numero_canais < 1 or volume_maximo < 1:
            raise ValueError("O número de canais mínimo é 1, enquanto o volume mínimo deve ser 1.")
        elif canal > numero_canais:
            raise ValueError("O canal atual não pode ser maior do que o número de canais existentes.")
        elif volume > volume_maximo:
            raise ValueError("O volume atual não pode ser maior do que o volume máximo permitido.")
        else:
            self.__ligado = ligado
            self.__canal = canal
            self.__volume = volume
            self.__numero_canais = numero_canais
            self.__volume_maximo = volume_maximo

    # Método "ligar".
    def ligar(self):
        self.__ligado = True

    # Método "desligar".
    def desligar(self):
        self.__ligado = False

    # Método "imprimir".
    def imprimir(self):
        print(f' Ligado: {self.__ligado} \t Canal: {self.__canal} \t Volume: {self.__volume} \t'
              f' Número de canais: {self.__numero_canais} \t Volume máximo: {self.__volume_maximo} \n')


# Testando.
televisor1 = Televisor(True, 595, 8, 700, 20)

televisor1.imprimir()  # OUTPUT: Ligado: True 	 Canal: 595 	 Volume: 8 	 Número de canais: 700 	 Volume máximo: 20

televisor1.desligar()  # Ligado: False

televisor1.imprimir()  # OUTPUT: Ligado: False 	 Canal: 595 	 Volume: 8 	 Número de canais: 700 	 Volume máximo: 20
