"""
7 - Faça um programa que receba do usuário um arquivo texto.
Crie outro arquivo texto contendo o texto do arquivo de entrada, mas com as vogais substituídas por "*".
"""

# Recebendo o arquivo do usuário e criando o nome do novo arquivo.
arquivo_original = input('Digite o nome do arquivo texto, sem a extensão ".txt": ')
arquivo_modificado = arquivo_original + '_modificado.txt'
arquivo_original += '.txt'

# Lista de vogais a serem substituídas.
vogais = 'aeiouAEIOUãÃáÁâÂéÉêÊíÍôÔõÕóÓúÚ'
lista = []
nova_lista = []

# Bloco try/except/else utilizado para percorrer o arquivo e gerar um novo com as devidas alterações.
try:
    with open(arquivo_original, 'r') as arq:
        for linha in arq.readlines():
            lista.append(linha)
except FileNotFoundError:
    print(' O arquivo não foi encontrado.')
else:
    for linha in lista:
        for letra in linha:
            if letra in vogais:
                letra = '*'
            nova_lista.append(letra)
    with open(arquivo_modificado, 'w', encoding='utf-8') as arq:
        for linha in nova_lista:
            arq.write(linha)
    print(' Foi gerado um novo arquivo com as devidas alterações realizadas com sucesso.')
