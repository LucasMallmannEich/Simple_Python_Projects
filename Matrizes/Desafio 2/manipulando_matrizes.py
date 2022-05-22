"""
Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos.
Escreva ao final a matriz obtida.
"""

# Declaração da matriz.
matriz = []

# Loop for para tornar a matriz 5 por 5 (5 linhas contendo 5 elementos - número zero).
for i in range(5):
    matriz.append([0]*5)

# Preenchendo a diagonal principal (quando o número da coluna é igual ao número da linha) com o número 1.
for linha in range(5):
    for coluna in range(5):
        if coluna == linha:
            matriz[linha][coluna] = 1

# Imprimindo a matriz obtida.
for listas in matriz:
    print(listas)
