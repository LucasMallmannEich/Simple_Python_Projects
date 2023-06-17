"""
10 - Baseando-se no exercício anterior, adicione os métodos "marcha_acima" e "marcha_abaixo", que deverão efetuar a
troca de marchas, onde o método "marcha_acima" deverá subir uma marcha, ou seja, se a moto estiver na primeira marcha,
deverá ser trocada para segunda marcha e assim por diante. O método "marcha_abaixo" deverá realizar o oposto, ou seja,
descer a marcha.
"""


# Classe "Moto".
class Moto:

    # Método construtor.
    def __init__(self, marca, modelo, cor, marcha):
        if type(marca) == str and type(modelo) == str and type(cor) == str:
            self.__marca = marca
            self.__modelo = modelo
            self.__cor = cor
        else:
            raise TypeError('A marca, o modelo e a cor devem ser argumentos do tipo string(str).')
        if type(marcha) != int:
            raise TypeError("A marcha deve ser um número inteiro.")
        elif marcha < 0:
            raise ValueError("A marcha deve ser um número não negativo e inteiro.")
        else:
            self.__marcha = marcha

    # Método "marcha_acima".
    def marcha_acima(self):
        self.__marcha = self.__marcha + 1

    # Método "marcha_abaixo".
    def marcha_abaixo(self):
        if self.__marcha > 0:
            self.__marcha = self.__marcha - 1
        else:
            print('Não é possível diminuir a marcha, pois ela já está em zero.')

    # Método "imprimir".
    def imprimir(self):
        print(f' Marca: {self.__marca} \t Modelo: {self.__modelo} \t Cor: {self.__cor} \t Marcha: {self.__marcha}')


# Testando.
moto1 = Moto('Suzuki', 'SRS-78', 'Azul', 6)

moto1.imprimir()  # OUTPUT: Marca: Suzuki 	 Modelo: SRS-78 	 Cor: Azul 	 Marcha: 6

moto1.marcha_acima()  # Marcha: 7
moto1.marcha_acima()  # Marcha: 8

moto1.imprimir()  # OUTPUT: Marca: Suzuki 	 Modelo: SRS-78 	 Cor: Azul 	 Marcha: 8

moto1.marcha_abaixo()  # Marcha: 7

moto1.imprimir()  # OUTPUT: Marca: Suzuki 	 Modelo: SRS-78 	 Cor: Azul 	 Marcha: 7