"""
11 - Escreva um programa que leia um número inteiro maior do que zero.
Ele precisa devolver, na tela, a soma de os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8(2+5+1).
Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".
"""

try:
    # Captará as informações enviadas pelo usuário.
    numero = int(input('Digite um número inteiro maior do que zero:  '))
except ValueError:
    # Caso o usuário não digite um número do tipo inteiro.
    print(' Você deveria ter digitado um número inteiro.\n')
else:
    if numero > 0:
        # Caso o número seja maior do que zero.
        str_num = str(numero)
        soma = 0
        for n in range(len(str_num)):
            soma = soma + int(str_num[n])
        print(f' A soma dos algarismos do número informado é {soma}.\n')
    else:
        # Caso o número não seja maior do que zero.
        print(' Número inválido.\n')
