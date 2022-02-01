"""
Escreva um código que apresente a classe "Quadrado", com atributos "lado", "area" e "perimetro". A classe também
deve apresentar os métodos "calcular_area", "calcular_perimetro" e "imprimir". Os métodos "calcular_area" e
"calcular_perimetro" devem efetuar seus respectivos cálculos e colocar os valores nos atributos "area" e "perimetro". O
método "imprimir" deve mostrar na tela os valores de todos os atributos. Salienta-se que a área de um quadrado é obtida
pela fórmula (lado * lado) e o perímetro por (4 * lado).
"""


# Classe "Quadrado".
class Quadrado:

    # Método construtor.
    def __init__(self, lado):
        if lado >= 0:
            self.__lado = lado
        else:
            raise ValueError("O valor do lado não pode ser negativo.")
        self.__area = Quadrado.calcular_area(self)
        self.__perimetro = Quadrado.calcular_perimetro(self)

    # Método "calcular_area".
    def calcular_area(self):
        return self.__lado * self.__lado

    # Método "calcular_perimetro".
    def calcular_perimetro(self):
        return 4 * self.__lado

    # Método "imprimir".
    def imprimir(self):
        print(f' Lado: {self.__lado} m \t Área: {self.__area} m² \t Perímetro: {self.__perimetro} m')


# Testando:
quadrado1 = Quadrado(12)

quadrado1.imprimir()  # OUTPUT: Lado: 12 m 	 Área: 144 m² 	 Perímetro: 48 m
ori