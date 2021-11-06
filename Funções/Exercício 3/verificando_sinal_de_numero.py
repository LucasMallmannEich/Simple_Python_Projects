# 3 - Faça uma função para verificar se um número é positivo ou negativo.
# Sendo que o valor do retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0.


def verifica_sinal(numero):
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    return 0


num = float(input('Digite um número real: '))

print(verifica_sinal(num))