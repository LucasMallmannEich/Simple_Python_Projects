"""
13 - Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o menor valor.
"""
lista = []

# Bloco try/except/else utilizado para captar valores inseridos pelo usuário.
for i in range(5):
    num = ''
    while len(lista) < 5:
        try:
            num = float(input('Digite um número: '))
        except ValueError:
            print(' Você deve digitar um valor numérico.')
        else:
            lista.append(num)

# Captando, por meio do método "index", a posição do maior e menor elemento na lista.
maior = lista.index(max(lista))
menor = lista.index(min(lista))

print(f' O maior elemento encontra-se na posição {maior}.\n O menor elemento encontra-se na posição {menor}.')
