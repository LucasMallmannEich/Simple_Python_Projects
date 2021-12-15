class Filme:

    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes = self.likes + 1


class Serie:

    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes = self.likes + 1


mogli = Filme('mogli', 2018, 120)
arrow = Serie('arrow', 2012, 8)

print(f' Nome: {mogli.nome} \n Ano: {mogli.ano} \n Duração: {mogli.duracao} min \n Likes: {mogli.likes} \n\n')
print(f' Nome: {arrow.nome} \n Ano: {arrow.ano} \n Temporadas: {arrow.temporadas} \n Likes: {arrow.likes} \n')

mogli.dar_like()
mogli.dar_like()

arrow.dar_like()
arrow.dar_like()
arrow.dar_like()
arrow.dar_like()
arrow.dar_like()
arrow.dar_like()
arrow.dar_like()

print(f' Nome: {mogli.nome} \n Ano: {mogli.ano} \n Duração: {mogli.duracao} min \n Likes: {mogli.likes} \n\n')
print(f' Nome: {arrow.nome} \n Ano: {arrow.ano} \n Temporadas: {arrow.temporadas} \n Likes: {arrow.likes}')
