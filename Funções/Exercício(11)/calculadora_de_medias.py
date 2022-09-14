"""
Elabore uma função que receba 3 notas de um aluno como parâmetros e uma letra.
Se a letra for A, a função deverá calcular a média aritmética das notas do aluno.
Se a letra for P, a função deverá calcular a média ponderada, com pesos 5, 3 e 2.
"""


def calculadora_notas(n1, n2, n3, letra1):
    if letra1 == 'P':
        return (n1*5 + n2*3 + n3*2) / 10
    elif letra1 == 'A':
        return (n1 + n2 + n3) / 3
    else:
        return 'A letra informada não foi "P" ou "A".'


num1, num2, num3 = -1, -1, -1

try:
    while num1 < 0 or num1 > 10:
        num1 = float(input('Digite a primeira nota do aluno: '))
        if num1 < 0 or num1 > 10:
            print(' A nota deve estar entre 0 e 10.')
    while num2 < 0 or num2 > 10:
        num2 = float(input('Digite a segunda nota do aluno: '))
        if num2 < 0 or num2 > 10:
            print(' A nota deve estar entre 0 e 10.')
    while num3 < 0 or num3 > 10:
        num3 = float(input('Digite a terceira nota do aluno: '))
        if num3 < 0 or num3 > 10:
            print(' A nota deve estar entre 0 e 10.')
except ValueError:
    print(' Você deveria ter informado um número.')
else:
    try:
        letra = str(input('Digite a letra "A", para média aritmética, ou a letra "P", para média ponderada: '))
    except ValueError:
        print(' Você deveria ter informado uma letra.')
    else:
        if letra != 'A' and letra != 'P':
            print(' Você deveria ter informado as letras "A" ou "P".')
        else:
            if letra == 'P':
                print(f' Média Ponderada: {calculadora_notas(num1, num2, num3, letra):.2f}')
            else:
                print(f' Média Aritmética: {calculadora_notas(num1, num2, num3, letra):.2f}')
