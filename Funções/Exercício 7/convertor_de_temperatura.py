"""
Faça uma função que receba uma temperatura em graus Celcius e retorne-a convertida em graus Fahrenheit. A fórmula de
conversão é: F = C * (9/5) + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celcius.
"""


# Função "temperatura".
def temperatura(cel):
    if type(cel) == int or type(cel) == float:
        return cel * (9/5) + 32
    else:
        raise ValueError("A temperatura deve ser representada por um número.")


# Bloco try/except/else, utilizado para validar o valor digitado pelo usuário.
try:
    celcius = float(input('Digite uma temperatura em graus Celcius: '))
except ValueError:
    print("A temperatura deve ser um representada por um número.")
else:
    print(f' A temperatura correspondente, em graus Fahrenheit, é: {temperatura(celcius):.2f} ºF.')
