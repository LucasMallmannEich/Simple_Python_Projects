"""
Faça um programa que preencha uma lista com 10 números reais.
Calcule e mostre a quantidade de números negativos e a soma dos números positivos dessa lista.
"""

# Declaração da lista, do contador de ocorrências de números negativos e do somador de números positivos.
lista = []
cont_negativos = 0
soma_positivos = 0

# Laço de repetição utilizado para captar 10 valores numéricos reais do usuário.
while len(lista) < 10:
    try:
        numero = float(input('Digite um número real que será acrescentado à lista: '))
    except ValueError:
        print(' Digite o número corretamente. Por favor, tente novamente.\n')
    else:
        lista.append(numero)
        if numero < 0:
            cont_negativos += 1
        if numero > 0:
            soma_positivos += numero

# Impressão dos resultados.
print(f' Quantidade de número negativos: {cont_negativos} \n Soma dos números positivos: {soma_positivos}')
