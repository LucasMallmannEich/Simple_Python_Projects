# 6 - Faça um programa que receba do usuário um vetor com 10 posições.
# Em seguida, deverá ser impresso o maior e o menor elemento do vetor.

lista = []

while len(lista) != 10:
    valor = float(input('Digite um número que será acrescentado ao vetor: '))
    lista.append(valor)

print(f' O maior e o menor elemento do vetor possuem, respectivamente, os valores {min(lista)} e {max(lista)}.')