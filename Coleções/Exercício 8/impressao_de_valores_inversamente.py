# 8 - Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.

lista = []

while len(lista) != 6:
    valor = int(input('Digite um número que será acrescentado ao vetor: '))
    lista.append(valor)

print(f' Os valores lidos na ordem inversa são: {lista[::-1]}')
