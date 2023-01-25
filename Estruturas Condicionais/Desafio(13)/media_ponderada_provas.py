"""
13 - Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda prova têm peso 1 e a terceira tem peso 2.
Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
A nota para aprovação deve ser igual ou superior a 60 pontos.
"""

# Irá ser levantado um ValueError caso o usuário digite algo fora dos padrões.
try:
    nota1 = float(input('Digite a primeira nota do aluno (0 à 100): '))
    nota2 = float(input('Digite a segunda nota do aluno (0 à 100): '))
    nota3 = float(input('Digite a terceira nota do aluno (0 à 100): '))
    if nota1 < 0 or nota1 > 100 or nota2 < 0 or nota2 > 100 or nota3 < 0 or nota3 > 100:
        raise ValueError
except ValueError:
    print('Você deveria ter digitado valores numéricos entre 0 e 100.')
else:
    media = (nota1 + nota2 + nota3*2)/4
    if media < 60:
        print(' O aluno foi reprovado.')
    else:
        print(' O aluno foi aprovado.')
