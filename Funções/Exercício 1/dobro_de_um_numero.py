# 1 - Crie uma função que recebe como parâmetro um número inteiro e devolve o seu dobro.


def dobro(numero):
    return numero*2


num = float(input('Digite um numero que será o dobro: '))

print(f' O dobro de {num} é {dobro(num)}.')
