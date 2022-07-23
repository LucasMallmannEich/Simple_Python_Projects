"""
12 - Faça um programa que leia 5 valores.
Após isso, mostre todos os valores lidos juntamente com o maior, o menor e a média dos valores.
"""

# Declaração da variável que armazena os cinco valores listados.
lista = []

# O "loop while" garante que o usuário digite cinco valores numéricos reais para prosseguir com a execução do programa.
while len(lista) < 5:
    try:
        numero = float(input('Digite um valor numérico real: '))
    except ValueError:
        print(' Tente inserir valores corretos, por gentileza.\n')
    else:
        lista.append(numero)

# Declaração das variáveis responsáveis por armazenar o valor da média dos valores, o maior valor e o menor valor.
media = 0
maior = lista[0]
menor = lista[0]

print(' Valores:')

# Laço de repetição utilizado para descobrir o maior e menor valor, além da média dos valores.
for elemento in lista:
    if elemento > maior:
        maior = elemento
    if elemento < menor:
        menor = elemento
    media = media + elemento
    print(elemento)
media = media / 5

# Impressão do maior valor, menor valor e a média dos valores.
print(f' Maior Valor: {maior}\n Menor Valor: {menor} \n Média dos Valores: {media:.2f}')
