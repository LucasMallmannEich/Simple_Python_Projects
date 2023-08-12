"""
13 - Baseando-se no exercício anterior, adicione os métodos "ligar" e "desligar", que deverão mudar o conteúdo do
atributo "ligada" confome o caso.
"""


# Classe "Moto".
class Moto:

    # Método construtor.
    def __init__(self, marca, modelo, cor, marcha, menor_marcha, maior_marcha, ligada):
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
        if type(ligada) != bool:
            raise TypeError("O atributo 'ligada' deve ser do tipo booleano.")
        else:
            self.__ligada = ligada

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

    # Método "ligar".
    def ligar(self):
        self.__ligada = True

    # Método "desligar".
    def desligar(self):
        self.__ligada = False

    # Método "imprimir".
    def imprimir(self):
        print(f' Marca: {self.__marca} \t Modelo: {self.__modelo} \t Cor: {self.__cor} \t Marcha: {self.__marcha} \t'
              f' Menor marcha: {self.__menor_marcha} \t Maior marcha: {self.__maior_marcha} \t Ligada: {self.__ligada}')


# Testando.
moto1 = Moto('Mitstubishi', 'ER-901', 'Amarelo', 5, 4, 8, True)

moto1.imprimir()
# Marca: Mitstubishi 	 Modelo: ER-901   Cor: Amarelo 	 Marcha: 5 	 Menor marcha: 4  Maior marcha: 8   Ligada: True

moto1.marcha_abaixo()  # Marcha: 4
moto1.marcha_abaixo()  # OUTPUT: A moto já está em sua menor marcha possível.
moto1.desligar()  # Ligada = False

moto1.imprimir()
# Marca: Mitstubishi 	 Modelo: ER-901   Cor: Amarelo 	 Marcha: 4 	 Menor marcha: 4  Maior marcha: 8   Ligada: False

moto1.marcha_acima()  # Marcha: 5
moto1.marcha_acima()  # Marcha: 6
moto1.ligar()  # Ligada = True

moto1.imprimir()
# Marca: Mitstubishi 	 Modelo: ER-901   Cor: Amarelo 	 Marcha: 5 	 Menor marcha: 6  Maior marcha: 8   Ligada: True
