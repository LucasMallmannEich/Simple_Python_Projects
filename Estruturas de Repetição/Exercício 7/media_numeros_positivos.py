"""
7 - Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
"""

soma = 0
contador_positivos = 0

while contador_positivos < 10:
    try:
        num = int(input('Digite um número positivo: '))
    except ValueError:
        print('Você deve digitar um número positivo. Por favor, tente novamente.')
    else:
        if num > 0:
            contador_positivos = contador_positivos + 1
            soma = soma + num

print(f'Média: {soma/contador_positivos:.2f}')
