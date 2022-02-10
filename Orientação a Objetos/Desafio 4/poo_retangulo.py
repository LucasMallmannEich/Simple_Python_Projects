"""
Escreva um código que apresente a classe "Retangulo", com atributos "comprimento", "largura", "area" e "perimetro". Essa
classe também deve ter os métodos "calcular_area", "calcular_perimetro" e "imprimir". Os métodos "calcular_area" e
"calcular_perimetro" devem efetuar seus respectivos cálculos e colocar os valores nos atributos "area" e "perimetro".
O método "imprimir" deve mostrar na tela os valores de todos os atributos. Salienta-se que a área de um retângulo é
obtida pela fórmula (comprimento * largura) e o perímetro pela fórmula (2*comprimento) + (2*largura).
"""


# classe "Retangulo"
class Retangulo:

    # Método construtor.
    def __init__(self, comprimento, largura):
        if type(comprimento) != int and type(comprimento) != float:
            raise TypeError("O comprimento do retângulo que você deseja contruir deve ser um número.")
        elif type(largura) != int and type(largura) != float:
            raise TypeError("A largura do retângulo que você deseja contruir deve ser um número.")
        elif comprimento < 0 or largura < 0:
            raise ValueError("O valor do comprimento ou da largura do retângulo não pode ser negativo.")
        else:
            self.__comprimento = comprimento
            self.__largura = largura

        self.__area = Retangulo.calcular_area(self)
        self.__perimetro = Retangulo.calcular_perimetro(self)

    # Método "calcular_area".
    def calcular_area(self):
        return self.__comprimento * self.__largura

    # Método "calcular_perimetro".
    def calcular_perimetro(self):
        return (self.__comprimento * 2) + (self.__largura * 2)

    # Método "imprimir".
    def imprimir(self):
        print(f' Comprimento: {self.__comprimento} m \t Largura: {self.__largura} m \t'
              f' Área: {self.__area} m² \t Perímetro: {self.__perimetro} m')


# Testando.
retangulo1 = Retangulo(10, 4.5)

retangulo1.imprimir()  # OUTPUT: Comprimento: 10 m 	 Largura: 4.5 m 	 Área: 45.0 m² 	 Perímetro: 29.0 m
