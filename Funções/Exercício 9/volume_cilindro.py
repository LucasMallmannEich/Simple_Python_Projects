"""
Faça uma função que receba a altura e o raio de um cilindro circular e retorne o volume do cilindro.
O volume de um cilindro circular é calculado por meio da seguinte fórmula: V = pi * raio² * altura, onde pi=3.141592.
"""


# Função que calcula o volume de um cilindro circular.
def volume_cilindro(altura, raio):
    return 3.141592 * (raio**2) * altura


# Bloco try/except/else utilizado para captar informação do usuário e testar a função "volume_cilindro".
try:
    r = float(input('Digite a medida do raio, em metros: '))
    h = float(input('Digite a medida da altura, em metros: '))
except ValueError:
    print('Você deveria ter digitado um valor numérico para as medidas de raio e altura.')
else:
    print(f'O volume do cilindro é {volume_cilindro(h, r)} m².')
