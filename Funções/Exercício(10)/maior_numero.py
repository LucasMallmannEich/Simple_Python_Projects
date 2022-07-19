"""
Faça uma função que receba dois números e retorne qual deles é o maior.
"""


# Função que retorna qual dos dois números é o maior.
def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    return "Os números são iguais."  # caso ambos sejam iguais;


# Teste da função "maior_numero" e captação de informações do usuário.
try:
    n1 = float(input('Digite o valor do primeiro número: '))
    n2 = float(input('Digite o valor do segundo número: '))
except ValueError:
    print('Você deveria ter digitado valores numéricos para ambos os números.')
else:
    print(f'Maior número: {maior_numero(n1, n2)}')
