# 5 - Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.

lista = []
par = []

while len(lista) != 10:
    valor = float(input('Digite um número que será acrescentado ao vetor: '))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)

print(f' Este vetor possui {len(par)} valores pares.')
