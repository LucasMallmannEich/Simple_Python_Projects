# 1 - Faça um programa que receba dois números e mostre qual deles é o maior.

number1 = float(input('Digite um número:  '))
number2 = float(input('Digite um número:  '))

if number1 > number2:
    print(f' O {number1} é maior do que o {number2}.\n')

if number1 == number2:
    print(f' Os dois números possuem o mesmo valor.\n')

if number1 < number2:
    print(f' O {number2} é maior do que o {number1}.\n')
