# Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes.
# E tem como saída o número de cada dado em relação entre eles (>, <, =) de cada lançamento.

import random

n = int(input('Digite o número de vezes que os dados serão lançados: '))
contador = 0
count1 = 0
count2 = 0
count3 = 0

while contador != n:
    contador += 1
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)

    if d1 > d2:
        print(f' O número gerado pelo d1 foi {d1} e o número gerado pelo d2 foi {d2}. Logo, como {d1} > {d2}, d1 > d2.')
        count1 += 1

    elif d2 > d1:
        print(f' O número gerado pelo d1 foi {d1} e o número gerado pelo d2 foi {d2}. Logo, como {d2} > {d1}, d2 > d1.')
        count2 += 1

    elif d1 == d2:
        print(f' O número gerado pelo d1 foi {d1} e o número gerado pelo d2 foi {d2}. Logo, como {d1} = {d2}, d1 = d2.')
        count3 += 1

print(f' O dado 1 venceu o dado 2: {count1} vez(es).')
print(f' O dado 2 venceu o dado 1: {count2} vez(es).')
print(f' Acabou empatado: {count3} vez(es).')
