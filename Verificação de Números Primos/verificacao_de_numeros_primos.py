def primo(num):
    soma = 0
    for n in range(2, num):
        if num % n == 0:
            soma = soma + 1
    if soma == 0:
        return f'O número {num} é primo.'
    else:
        return f'O número {num} não é primo.'


numero = 1

while numero != 0:
    try:
        numero = int(input('Digite um número inteiro e positivo (caso queira sair, digite 0): '))
    except ValueError:
        print('Por favor, digite novamente.')
    else:
        if numero == 0:
            print('Você saiu do programa.')
        elif numero > 0:
            print(primo(numero))
        else:
            print('Por favor, digite novamente.')
