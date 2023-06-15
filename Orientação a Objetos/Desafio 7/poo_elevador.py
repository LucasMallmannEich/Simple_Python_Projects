"""
7 - Crie uma classe denominada "Elevador" para armazenar as informações de um elevador dentro de um prédio. A classe deve
armazenar o andar atual (térreo = 0), total de andares no prédio, excluindo o térreo, capacidade do elevador, além de
quantas pessoas estão presentes nele.
A classe deve também disponibilizar os seguintes métodos:
    - Inicializa: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os
elevadores sempre começam no terréo e vazio);
    - Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
    - Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
    - Sobe: para subir um andar (não deve subir se já estiver no último andar);
    - Desce: para descer um andar (não deve descer se já estiver térreo).
"""


class Elevador:

    def __init__(self, capacidade, total_de_andares):
        self.__capacidade = capacidade
        self.__total_de_andares = total_de_andares
        self.__pessoas_presentes = 0
        self.__andar_atual = 0

    def entra(self):
        if self.__pessoas_presentes < self.__capacidade:
            self.__pessoas_presentes = self.__pessoas_presentes + 1

    def sai(self):
        if self.__pessoas_presentes != 0:
            self.__pessoas_presentes = self.__pessoas_presentes - 1

    def sobe(self):
        if self.__andar_atual != self.__total_de_andares:
            self.__andar_atual = self.__andar_atual + 1

    def desce(self):
        if self.__andar_atual != 0:
            self.__andar_atual = self.__andar_atual - 1