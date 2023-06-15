"""
6 - Crie uma classe "Agenda" que possa armazenar 10 pessoas e seja capaz de realizar as seguintes operações:
+ void armazena_pessoa(String nome, int idade, float altura);
+ void remove_pessoa(String nome);
+ int busca_pessoa(String nome); ---> Informa em que posição da agenda está a pessoa.
+ void imprime_agenda(); ---> Imprime os dados de todas as pessoas da agenda.
+ void imprime_pessoa(int index); ---> Imprime os dados da pessoa que está na posição "i" da agenda.
"""


class Agenda:

    def __init__(self):
        self.__nomes = []
        self.__idades = []
        self.__alturas = []

    def armazena_pessoa(self, nome, idade, altura):

        if len(self.__nomes) < 10:
            self.__nomes.append(nome)
            self.__idades.append(idade)
            self.__alturas.append(altura)

    def remove_pessoa(self, nome):
        if nome in self.__nomes:
            i = self.__nomes.index(nome)
            for nome in self.__nomes:
                if self.__nomes.index(nome) == i:
                    self.__nomes.remove(nome)
            for idade in self.__idades:
                if self.__idades.index(idade) == i:
                    self.__idades.remove(idade)
            for altura in self.__alturas:
                if self.__alturas.index(altura) == i:
                    self.__alturas.remove(altura)

    def busca_pessoa(self, nome):
        if nome in self.__nomes:
            i = self.__nomes.index(nome)
            return f' O nome informado está na {i+1}ª posição da agenda.'
        else:
            return f' O nome informado não está na agenda.'

    def imprime_agenda(self):
        for nome in self.__nomes:
            i = self.__nomes.index(nome)
            print(f' Nome: {nome} \n Idade: {self.__idades[i]} anos \n Altura: {self.__alturas[i]:.2f} m \n\n')

    def imprime_pessoa(self, i):
        if i < len(self.__nomes):
            print(f' Nome: {self.__nomes[i]} \n Idade: {self.__idades[i]} anos \n Altura: {self.__alturas[i]:.2f} m \n\n')


# Testando a classe criada.
agenda1 = Agenda()

# Testando o método "armazena_pessoa".
agenda1.armazena_pessoa('Carlos', 24, 1.78)
agenda1.armazena_pessoa('Roberto', 38, 1.60)
agenda1.armazena_pessoa('Glória', 20, 1.80)

# Testando o método "remove_pessoa".
agenda1.remove_pessoa('Carlos')

# Testando o método "busca_pessoa".
print(agenda1.busca_pessoa('Glória'))
print(agenda1.busca_pessoa('Roberto'))

# Testando o método "imprime_agenda".
agenda1.imprime_agenda()

# Testando o método "imprime_pessoa".
agenda1.imprime_pessoa(0)
agenda1.imprime_pessoa(1)
