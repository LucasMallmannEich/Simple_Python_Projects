# 1 - Faça um programa que possua um vetor denominado A que armazene 6 números inteiros.
# O programa deve executar os seguintes passos:
# (A) -> Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
# (B) -> Armazene em uma variável inteira (simples) a soma entre os valores da posição A[0], A[1] e A[5] do vetor e
# mostre na tela esta soma.
# (C) -> Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
# (D) -> Mostre na tela cada valor do vetor A, um em cada linha.

A = [1, 0, 5, -2, -5, 7]  # (A)

soma = A[0] + A[1] + A[5]  # (B)
print(soma)

A[4] = 100  # (C)
print(A)

for vetor in A:  # (D)
    print(vetor)
