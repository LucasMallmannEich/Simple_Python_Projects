"""
Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral.
"""

# Declaração do vetor que armazena as notas dos alunos.
notas = []

# Laço de repetição que só será interrompido quando houver a inserção de 15 notas válidas.
while len(notas) != 15:
    try:
        nota = float(input(f'Digite a nota do  {len(notas)+1}º aluno: '))
    except ValueError:
        print('Você deve digitar um número real.')
    else:
        if nota < 0 or nota > 10:
            print('Você deve digitar um número entre 0 e 10 (inclusos).')
        else:
            notas.append(nota)

# Soma as notas da turma inteira e armazena na variável "media_geral".
media_geral = sum(notas)

# Calcula a média geral da turma considerando que há 15 alunos nela.
media_geral = media_geral/15

# Impressão da média geral das notas da turma.
print(f'{media_geral:.2f}')
