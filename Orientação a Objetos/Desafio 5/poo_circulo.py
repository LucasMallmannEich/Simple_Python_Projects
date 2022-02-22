"""
Escreva um código que apresente a classe "Circulo", com atributos "raio", "area" e "perimetro". A classe ainda deve ter
os métodos "calcular_area", "calcular_perimetro" e "imprimir". Os métodos "calcular_area" e "calcular_perimetro" devem
efetuar seus respectivos cálculos e colocar os valores nos atributos "area" e "perimetro". O método "imprimir" deve
mostrar na tela os valores de todos os atributos. Salienta-se que a área de um círculo é obtida pela fórmula
(pi * raio * raio) e o perímetro por (2 * pi * raio).
"""

# Importação da biblioteca "math", com o intuito de utilizar o valor de pi.
import math


# Classe "Circurlo".
class Circulo:

    # Método construtor.
    def __init__(self, raio):
        if type(raio) == int or type(raio) == float:
            self.__raio = raio
            self.__area = Circulo.calcular_area(self)
            self.__perimetro = Circulo.calcular_perimetro(self)
        else:
            print('Você deveria ter digitado um valor numérico.')

    # Método "calcular_area".
    def calcular_area(self):
        return math.pi * math.pi * self.__raio

    # Método "calcular_perimetro".
    def calcular_perimetro(self):
        return math.pi * (self.__raio * 2)

    # Método "imprimir".
    def imprimir(self):
        if self.__raio is True or self.__raio is False:
            if self.__raio >= 0 and (type(self.__raio) == int or type(self.__raio) == float):
                print(f'Raio: {self.__raio:.2f} m \t Área: {self.__area:.2f} m² \t Perímetro: {self.__perimetro:.2f} m')
            else:
                print('Você deveria ter digitado um raio com valor não negativo.')
        else:
            print('Você deveria ter digitado um raio com valor não negativo.')


# Testando.
circulo1 = Circulo(4.5)

circulo1.imprimir()  # OUTPUT: Raio: 4.50 m 	 Área: 44.41 m² 	 Perímetro: 28.27 m



# Testando.
circulo1 = Circulo(4.5)

circulo1.imprimir()  # OUTPUT: Raio: 4.50 m 	 Área: 44.41 m² 	 Perímetro: 28.27 m
