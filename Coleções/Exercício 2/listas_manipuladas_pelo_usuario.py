# 2 - Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.

counter = 0
numeros = []

while counter != 6:
    numero = int(input('Digite um número inteiro: '))
    numeros.append(numero)
    counter = counter + 1

for num in numeros:
    print(num)
