"""
2 - Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas linhas esse arquivo possui.
"""

# Declaração da variável que armazena o nome do arquivo de texto.
arquivo = ''

# Laço de repetição que irá ser interrompido apenas quando o usuário digitar o nome de um arquivo.
while len(arquivo) == 0:
    arquivo = str(input('Digite um arquivo de texto, sem o ".txt" ao final: '))

# Junção da string para não exigir que o usuário digite ".txt" no momento da inserção de dados.
arquivo = arquivo + '.txt'

# Bloco try/except/else para verificar se o arquivo de texto informado existe ou foi encontrado.
try:
    # Abre o arquivo no modo de leitura.
    with open(arquivo, 'r') as arq:
        # A lista "linhas" armazena o valor de cada linha do arquivo em cada posição.
        linhas = arq.readlines()
except FileNotFoundError:
    # Informa ao usuário que o arquivo não foi encontrado.
    print(' O arquivo não foi encontrado.')
else:
    # Informa ao usuário o número de linhas que o arquivo informado possui.
    print(f' Esse arquivo possui {len(linhas)} linhas.')
