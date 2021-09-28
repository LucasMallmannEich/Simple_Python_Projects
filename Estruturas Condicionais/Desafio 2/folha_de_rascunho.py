# 2 - Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz qudrada do número.
# Se o número for negativo, mostre uma mensagem dizendo que o número é invalido.

number = float(input('Digite um número:  '))

if number > 0:
    print(f' A raiz quadrada desse número é: {number ** (1 / 2)}.\n')

elif number < 0:
    print(f' O número digitado é inválido.\n')