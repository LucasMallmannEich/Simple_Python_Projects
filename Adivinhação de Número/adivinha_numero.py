import random

numero = random.randint(1, 1001)
cont = 0
numeroAlea = numero

while True:
    chute = int(input('Digite um número para tentar acertar o(s) algarismo(s) gerado (CHUTE!): '))
    cont = cont + 1

    if chute == numeroAlea:
        print(f' Você acertou! Foi preciso {cont} chutes!')
        break

    elif chute > numeroAlea:
        print(' O chute é maior do que o número gerado.')

    elif chute < numeroAlea:
        print(' O chute é menor do que o número gerado.')

    else:
        print(' Você deve informar um número entre 1 e 1000.')