"""
10 - Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal.
Utilizando as seguintes fórmulas (onde h corresponde a altura):
Homens: (72.7 * h) - 58
Mulheres: (62.1 * h) - 44.7
"""

try:
    # Captará as informações fornecidas pelo usuários.
    altura = float(input('Digite a altura de uma pessoa, em metros:  '))
    sexo = str(input('Digite o sexo de uma pessoa, com letras minúsculas:  '))
except ValueError:
    # Caso o usuário não digite um valor numérico para a altura da pessoa.
    print('Você deveria ter digitado um valor numérico para representar a altura da pessoa informada.')
else:
    if altura > 0:
        # Caso a altura seja maior do que zero.
        peso_ideal_homens = (72.7 * altura) - 58
        peso_ideal_mulheres = (62.1 * altura) - 44.7
        if sexo == 'masculino':
            # Caso o sexo digitado seja "masculino".
            print(f' O seu peso ideal é igual a {peso_ideal_homens:.2f} Kg.\n')
        elif sexo == 'feminino':
            # Caso o sexo digitado seja "feminino".
            print(f' O seu peso ideal é igual a {peso_ideal_mulheres:.2f} Kg.\n')
        else:
            # Caso o usuário não tenha digitado "feminino" ou "masculino".
            print(' O sexo precisa ser ou "feminino" ou "masculino".\n')
    else:
        # Caso a altura não seja maior do que zero.pes
        print(' A altura digitada deveria ser maior do que zero.')
