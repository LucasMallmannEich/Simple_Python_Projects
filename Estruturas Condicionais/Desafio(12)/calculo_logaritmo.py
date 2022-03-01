"""
12 - Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido".
Se o número for positivo, calcular o logaritmo deste número.
"""

# Importação da biblioteca "math".
import math

# Captação de informação do usuário.
try:
    numero = int(input('Digite um número inteiro e positivo:  '))
except ValueError:
    print('Você deveria ter digitado um número inteiro.\n')
else:
    if numero > 0:
        # Caso o número informado for positivo, o programa calcula o logaritmo desse número.
        logaritmo = math.log(numero)
        print(f' O logaritmo deste número é: {logaritmo}.\n')
    elif numero < 0:
        # Caso o número informado for negativo, o programa imprime a seguinte mensagem: "Número inválido.".
        print(f' Número inválido.\n')
    else:
        # Caso o número seja igual à zero(0).
        print(f'Para ser possível calcular o logaritmo de algum número, é necessário que ele seja positivo.\n')
