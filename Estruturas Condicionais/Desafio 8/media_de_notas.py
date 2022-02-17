"""
8 - Faça um programa que leia 2 notas de um aluno.
Verifique se as notas são válidas e exiba na tela a média destas notas.
Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0.
Caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.
"""

try:
    # Captará as informações do usuário.
    nota_A = float(input('Digite a primeira nota de um aluno:  '))
    nota_B = float(input('Digite a segunda nota de um aluno:  '))
except ValueError:
    # Caso o usuário digite algum tipo de dado que não seja um número.
    print(' Você deveria ter digitado números.\n')
else:
    # Se o usuário digitar um número, o programa fará a média das duas notas.
    media = (nota_A + nota_B) / 2
    # Se a primeira e a segunda nota estiverem entre o valor válido de 0 e 10, o programa imprime essa média.
    if 10 >= nota_A >= 0 and 10 >= nota_B >= 0:
        print(f' A média dessas notas é: {media}.\n')
    else:
        print(' A nota não possui um valor válido.\n')
