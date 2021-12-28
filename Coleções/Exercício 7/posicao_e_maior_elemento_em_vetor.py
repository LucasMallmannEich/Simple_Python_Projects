# 7 - Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
# Imprima o vetor, o maior elemento e a posição que ele se encontra.

lista = []

while len(lista) != 10:
    valor = float(input('Digite um número que será acrescentado ao vetor: '))
    lista.append(valor)

maximo = max(lista)

print(f' O vetor é este: {lista}.\n'
      f' O maior elemento do vetor possui o valor {maximo}, que está localizado na posição {lista.index(maximo)}.')
