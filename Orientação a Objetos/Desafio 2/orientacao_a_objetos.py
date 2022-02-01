"""
Escreva um código que apresente a classe Pessoa, com atributos "nome", "endereco", "telefone" e o método "imprimir".
O método "imprimir" deve mostrar na tela os valores de todos os atributos.
"""


# Classe "Pessoa".
class Pessoa:

    # Método construtor contendo os atributos privados "nome", "endereco" e "telefone".
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    # Método "imprimir".
    def imprimir(self):
        print(f' Nome: {self.__nome} \t Endereço: {self.__endereco} \t Telefone: {self.__telefone}')


# Testando:

pessoa1 = Pessoa('Carla', 'Rua Tiradentes, 455', '(51) 98765-4532')

pessoa1.imprimir()  # OUTPUT: Nome: Carla 	 Endereço: Rua Tiradentes, 455 	 Telefone: (51) 98765-4532
