# 4 - Faça um programa que leia um vetor de 8 posições.
# E, em seguida, leia também dois valores X e Y quaisquer correspondentes a duas posições no vetor.
# Ao final de seu programa, deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.

lista = []

while len(lista) != 8:
    valor = float(input('Digite um número que será acrescentado ao vetor: '))
    lista.append(valor)

x = int(input('Digite uma posição do vetor, lembrando que ele vai do 0 ao 7: '))
y = int(input('Digite outra posição do vetor, lembrando que ele vai do 0 ao 7: '))

soma = lista[x] + lista[y]
print(f' A soma dos valores encontrados nas respectivas posições X e Y resulta em {soma}.')
