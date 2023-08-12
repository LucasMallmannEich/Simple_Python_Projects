"""
11 - Baseando-se no exercício anterior, adicione os atributos "menor_marcha" e "maior_marcha", onde o atributo
"menor_marcha" indica qual será a menor marcha possível para a moto e o atributo "maior_marcha" indica qual será a maior
marcha possível. Desta forma, os métodos "marcha_acima" e "marcha_abaixo" devem ser reescritos de forma a não permiterem
a troca de marchas para valores abaixo da "menor_marcha" e acima da "maior_marcha". O método "imprimir" deve ser
modificado de forma a mostrar na tela os valores de todos os atributos.
"""


# Classe "Moto".
class Moto:

    # Método construtor.
    def __init__(self, marca, modelo, cor, marcha, menor_marcha, maior_marcha):
        if type(marca) == str and type(modelo) == str and type(cor) == str:
            self.__marca = marca
            self.__modelo = modelo
            self.__cor = cor
        else:
            raise TypeError('A marca, o modelo e a cor devem ser argumentos do tipo string(str).')
        if type(marcha) != int or type(menor_marcha) != int or type(maior_marcha) != int:
            raise TypeError("A marcha deve ser um número inteiro.")
        elif marcha < 0 or menor_marcha < 0 or maior_marcha < 0:
            raise ValueError("A marcha deve ser um número não negativo e inteiro.")
        elif menor_marcha > marcha or marcha > maior_marcha:
            raise ValueError("A marcha atual deve obedecer os valores da marcha mínima e máxima.")
        else:
            self.__marcha = marcha
            self.__menor_marcha = menor_marcha
            self.__maior_marcha = maior_marcha

    # Método "marcha_acima".
    def marcha_acima(self):
        if self.__marcha < self.__maior_marcha:
            self.__marcha = self.__marcha + 1
        else:
            print(' A moto já está em sua maior marcha possível.')

    # Método "marcha_abaixo".
    def marcha_abaixo(self):
        if self.__marcha > self.__menor_marcha:
            self.__marcha = self.__marcha - 1
        else:
            print(' A moto já está em sua menor marcha possível.')

    # Método "imprimir".
    def imprimir(self):
        print(f' Marca: {self.__marca} \t Modelo: {self.__modelo} \t Cor: {self.__cor} \t Marcha: {self.__marcha} \t'
              f' Menor marcha: {self.__menor_marcha} \t Maior marcha: {self.__maior_marcha}')


# Testando.
moto1 = Moto('Mitstubishi', 'ER-901', 'Amarelo', 5, 4, 8)

moto1.imprimir()
# OUTPUT: Marca: Mitstubishi 	 Modelo: ER-901 	 Cor: Amarelo 	 Marcha: 5 	 Menor marcha: 4 	 Maior marcha: 8

moto1.marcha_abaixo()  # Marcha: 4
moto1.marcha_abaixo()  # OUTPUT: A moto já está em sua menor marcha possível.

moto1.imprimir()
# OUTPUT: Marca: Mitstubishi 	 Modelo: ER-901 	 Cor: Amarelo 	 Marcha: 4 	 Menor marcha: 4 	 Maior marcha: 8

moto1.marcha_acima()  # Marcha: 5
moto1.marcha_acima()  # Marcha: 6

moto1.imprimir()
# OUTPUT: Marca: Mitstubishi 	 Modelo: ER-901 	 Cor: Amarelo 	 Marcha: 6 	 Menor marcha: 4 	 Maior marcha: 8
