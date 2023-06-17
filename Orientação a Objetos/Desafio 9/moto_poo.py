"""
9 - Escreva um código que apresente a classe "Moto", com os atributos "marca", "modelo", "cor" e "marcha". Além disso, a
classe também deve ter o método "imprimir". O método "imprimir" deve mostrar na tela os valores de todos os atributos. O
atributo marcha indica em que marcha a "Moto" se encontra no momento, sendo representada de forma inteira, onde
0 - neutro, 1 - primeira, 2 - segunda, etc.
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

    # Método "imprimir".
    def imprimir(self):
        print(f' Marca: {self.__marca} \t Modelo: {self.__modelo} \t Cor: {self.__cor} \t Marcha: {self.__marcha}')


# Testando.
moto1 = Moto('Suzuki', 'SRS-78', 'Azul', 6)
moto1.imprimir()  # OUTPUT: Marca: Suzuki 	 Modelo: SRS-78 	 Cor: Azul 	 Marcha: 6
