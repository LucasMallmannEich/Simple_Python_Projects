# 4 - Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
# - o número digitado ao quadrado;
# - a raiz quadrada do número digitado.

numero = float(input('Digite um número: '))

if numero > 0:
    print(f' O número digitado ao quadrado é igual a {numero * numero:.2f}.')
    print(f' A raiz quadrada do número digitado {numero ** (1 / 2):.2f}.\n')
