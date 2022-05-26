"""
Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa.
"""

# Declaração da lista.
lista = []

# Laço de repetição utilizado pra captar 6 valores pares digitados pelo usuário.
while len(lista) != 6:
    # Bloco try/except/else para verificar se o usuário digitou um valor inteiro quando foi solicitado.
    try:
        valor = int(input('Digite um número par que será acrescentado ao vetor: '))
    except ValueError:
        print(' Você deve digitar um número inteiro.\n')
    else:
        # Verificação para saber se o valor informado é par ou ímpar.
        if valor % 2 == 0:
            lista.append(valor)
        else:
            print(' Você deve digitar um valor par!\n')

# Impressão dos valores da lista na ordem inversa.
print(f' Os valores (pares) lidos na ordem inversa são: {lista[::-1]}')
