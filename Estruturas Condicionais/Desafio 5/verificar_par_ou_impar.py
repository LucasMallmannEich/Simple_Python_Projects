# 5 - Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.

numero = int(input('Digite um número inteiro:  '))
resto = numero % 2

if resto == 0:
    print(f' O {numero} é par.\n')

else:
    print(f' O {numero} é ímpar.\n')
