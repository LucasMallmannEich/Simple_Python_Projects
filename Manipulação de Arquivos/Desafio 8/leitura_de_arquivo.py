"""
8 - Faça um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo conteúdo, mas com todas as letras
minúsculas convertidas para maiúsculas. Os nomes dos arquivos serão fornecidos, via teclado, pelo usuário.
A função que converte maiúscula para minúscula é o upper(). Ela é aplicada em cada caractere da string.
"""

# Inserção dos nomes dos arquivos pelo usuário.
arquivo = str(input('Digite um arquivo de texto a ser lido, sem a extensão ".txt": '))
arquivo += '.txt'
arquivo_novo = str(input('Digite o nome do novo arquivo de texto, sem o ".txt": '))
arquivo_novo += '.txt'

lista = []
cont = 0

# Bloco try/except/else utilizado para ler o arquivo original e escrever um novo arquivo de texto.
try:
    with open(arquivo, 'r') as arq:
        for linha in arq.readlines():
            for letra in linha:
                lista.append(letra)
except FileNotFoundError:
    print(' O arquivo digitado não foi encontrado.')
else:
    with open(arquivo_novo, 'w', encoding='utf-8') as arq:
        for letra in lista:
            arq.write(lista[cont].upper())
            cont += 1
