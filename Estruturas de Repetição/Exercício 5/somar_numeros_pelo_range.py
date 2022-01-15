# 5 - Faça um programa que peça ao usuário para digitar 10 valores e some-os.

soma = 0

for n in range(1, 11):
    num = float(input(f'Digite 10 números {n}/{10}: '))
    soma = num + soma

print(f' A soma dos 10 números digitados equivale a {soma:.2f}.')
