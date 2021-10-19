numero = int(input('Digite um número inteiro: '))

soma = 0

for n in range(2, numero):
    if numero % n == 0:
        soma += 1
if soma != 0:
    print(f' Esse número não é primo.')
else:
    print(f' Esse número é primo.')
