# 6 - Escreva um programa que, dados dois números inteiros:
# mostre na tela o maior deles, assim como a diferença existente entre ambos.

try:
    numero1 = int(input('Digite um número inteiro:  '))
    numero2 = int(input('Digite um número inteiro:  '))
except ValueError:
    print("Você deveria ter digitado um número do tipo inteiro.")
else:
    if numero1 > numero2:
        print(f' O maior deles é o número {numero1}.')
        print(f' A diferença entre eles é igual a {numero1 - numero2}.\n')
    elif numero1 < numero2:
        print(f' O maior deles é o número {numero2}.')
        print(f' A diferença entre eles é igual a {numero2 - numero1}.\n')
    else:
        print(f' Os números são iguais, logo, não existe diferença entre eles.\n')
