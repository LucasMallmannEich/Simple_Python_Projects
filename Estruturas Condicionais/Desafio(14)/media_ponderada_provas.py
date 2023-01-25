"""
14 - A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10.
Respectivamente: a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
A média das três notas mencionadas anteriormente obedece aos pesos:
Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5.
De acordo com o resultado,mostre na tela se o aluno está reprovado (média entre 0 e 2.9), recuparação (entre 3 e 4.9).
Ou se foi aprovado. Faça todas as verificações necessárias.
"""

# Irá ser levantado um ValueError caso o usuário digite algo fora dos padrões.
try:
    nota1 = float(input('Digite a nota do trabalho de laboratório (0 à 10): '))
    nota2 = float(input('Digite a nota da avaliação semestral (0 à 10): '))
    nota3 = float(input('Digite a nota do exame final (0 à 10): '))
    if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10:
        raise ValueError
except ValueError:
    print('Você deveria ter digitado valores numéricos entre 0 e 10.')
else:
    media = (nota1*2 + nota2*3 + nota3*5)/10
    if media < 3:
        print(' O aluno foi reprovado.')
    elif media > 4.9:
        print(' O aluno foi aprovado.')
    else:
        print(' O aluno está de recuperação.')
