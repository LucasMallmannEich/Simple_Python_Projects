"""
Leia uma matriz 4 x 4 de números inteiros, conte e escreva quantos valores maiores que 10 ela possui.
"""

# Declaração das listas que serão usadas futuramente.
matriz = []
maiores_10 = []

# Inicialização da matriz.
while len(matriz) != 4:
    matriz.append([0] * 4)

# Inserção de dados na matriz.
for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = int(input('Digite um número: '))
        if matriz[linha][coluna] > 10:
            maiores_10.append(matriz[linha][coluna])

# Impressão dos dados.
if len(maiores_10) != 0:
    print(f' Há {len(maiores_10)} valor(es) maior(es) do que 10: {maiores_10}. ')
else:
    print(' Não há nenhum valor maior do que 10.')
