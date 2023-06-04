"""
9 - Faça um programa que receba dois arquivos do usuário e crie um terceiro arquivo com o conteúdo dos dois primeiros
juntos (o conteúdo do primeiro seguido do conteúdo do segundo).
"""

# Recebendo os dois arquivos do usuário.
arq1 = input('Digite o primeiro arquivo de texto, sem a extensão ".txt": ')
arq1 += '.txt'
arq2 = input('Digite o segundo arquivo de texto, sem a extensão ".txt": ')
arq2 += '.txt'
arq3 = input('Digite o nome do arquivo de texto a ser criado, sem a extensão ".txt": ')
arq3 += '.txt'

conteudo = ''

# Bloco try/except/else utilizado para concatenar os dois arquivos em um terceiro.
try:
    with open(arq1, 'r') as arq:
        for letra in arq.read():
            conteudo += letra
    conteudo += '\n'
    with open(arq2, 'r') as arq:
        for letra in arq.read():
            conteudo += letra
except FileNotFoundError:
    print(' O arquivo digitado não foi encontrado.')
else:
    with open(arq3, 'w', encoding='utf-8') as arq:
        for caractere in conteudo:
            arq.write(caractere)
