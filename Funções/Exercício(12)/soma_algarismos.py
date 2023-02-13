"""
Escreva uma função que receba um número inteiro maior do que zero e retorne a soma de todos os seus algarismos.
Por exemplo, ao número 251 corresponderá ao valor 8 (2 + 5 + 1).
Se o número lido não for maior do que zero, o programa terminará com  mensagem "Número inválido".
"""


# Função criada.
def soma_algarismos(numero):
    soma = 0
    s_num = str(numero)
    for algarismo in s_num:
        soma = soma + int(algarismo)
    return soma


# Testando a função criada.
try:
    num = int(input('Digite um número inteiro maior que zero: '))
except ValueError:
    print(' Você deveria ter digitado um número inteiro.')
else:
    if num > 0:
        print(f' A soma dos algarismos resulta em {soma_algarismos(num)}.')
    else:
        print(' Número inválido.')
