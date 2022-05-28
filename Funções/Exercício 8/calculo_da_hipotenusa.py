"""
Sejam a e b catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = raiz quadrada(a² + b²).
Faça uma função que receba os valores de a e b e calcule o valor da hipotenusa através da equação.
"""


# Função que calcula a hipotenusa a partir de dois parâmetros (os catetos) informados.
def hipotenusa(a_1, b_1):
    dentro_raiz = (a_1**2) + (b_1**2)
    return dentro_raiz**(1/2)


# Bloco try/except/else utilizado para captar a informação do usuário e se proteger contra possíveis erros no código.
try:
    a1 = float(input('Digite um valor para o 1º cateto, em metros: '))
    if a1 <= 0:
        raise ValueError
except ValueError:
    print(' Você deveria ter digitado um valor válido para o 1º cateto.')
else:
    try:
        b1 = float(input('Digite um valor para o 2º cateto, em metros: '))
        if b1 <= 0:
            raise ValueError
    except ValueError:
        print(' Você deveria ter digitado um valor válido para o 2º cateto.')
    else:
        # Se o usuário digitou os valores corretamente, o programa irá imprimir na tela o valor da hipotenusa.
        print(f' A hipotenusa desse triângulo é {hipotenusa(a1, b1):.2f} m.')
