# 7 - Faça um programa que receba dois números e mostre o maior.
# Se por acaso, os dois números forem iguais, imprima a mensagem "Números iguais".

numero1 = float(input('Digite um número:  '))
if type(numero1) != float:
    raise TypeError("Você deveria ter digitado um número.")

numero2 = float(input('Digite mais um número:  '))
if type(numero2) != float:
    raise TypeError("Você deveria ter digitado um número.")

if numero1 > numero2:
    print(f' O maior número entre os dois é o {numero1}.\n')
elif numero1 < numero2:
    print(f' O maior número entre os dois é o {numero2}.\n')
else:
    print(f' Números iguais.\n')
