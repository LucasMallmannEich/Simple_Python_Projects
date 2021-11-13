# 5 - Faça uma função e um programa de teste para o cálculo do volume de uma esfera.
# Sendo que o raio é passado por parâmetro. V = 4/3 * (pi) * R³.


def volume_esfera(raio):
    raio_cubo = raio**3
    v = (4/3)*3.14159263589*raio_cubo
    return v


raio1 = float(input('Digite o valor do raio da esfera, em metros (m): '))

print(f' O volume da esfera é {volume_esfera(raio1):.2f} m³.')