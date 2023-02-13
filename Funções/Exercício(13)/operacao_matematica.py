"""
Faça uma função que receba dois valores numéricos e um símbolo.
Esse símbolo representará a operação que se deseja efetuar com os números.
Se o símbolo for '+', deverá ser realizada uma adição; se for '-', uma subtração.
Se o símbolo for '/', deverá ser efetuada uma divisão; se for '*', uma multiplicação.
"""


# Função criada.
def operacao(num1, num2, simbol):
    if simbol == "+":
        return num1 + num2
    elif simbol == "-":
        return num1 - num2
    elif simbol == "/":
        return num1 / num2
    elif simbol == "*":
        return num1 * num2


# Testando a função criada.
try:
    n1 = float(input('Digite o primeiro valor numérico: '))
    n2 = float(input('Digite o segundo valor numérico: '))
    simbolo = input('Digite um dos símbolos a seguir (+, -, /, *): ')
except ValueError:
    print(' Você deveria ter digitado valores numéricos.')
else:
    if simbolo not in ('+', '-', '/', '*'):
        print(' Você deveria ter escolhido um dos símbolos apresentados.')
    else:
        print(f' Operação: {n1} {simbolo} {n2} = {operacao(n1, n2, simbolo):.2f}')
