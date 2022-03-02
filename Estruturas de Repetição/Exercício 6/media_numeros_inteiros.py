"""
6 - Faça um programa que leia 10 inteiros e imprima sua média.
"""

# Declaração da variável que será usada para somar os números informados.
soma = 0

# "Loop for" utilizado para permitir ao usuário digitar dez números.
for n in range(1, 11):
    num = ''
    # O programa só irá para o próximo loop quando o usuário digitar um número do tipo "int" (inteiro).
    while type(num) != int:
        try:
            num = int(input(f'Digite 10 números inteiros {n}/10: '))
        except ValueError:
            print('Você deveria ter digitado um número inteiro.\n')
        else:
            soma = num + soma

# Imprime a média dos dez números digitados pelo usuário.
print(soma/10)
