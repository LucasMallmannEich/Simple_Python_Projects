"""
5 - Faça um programa que receba do usuário um arquivo texto e um caractere.
Mostre na tela quantas vezes aquele caractere ocorre dentro do arquivo.
"""

# Recebendo um arquivo e um caractere do usuário.
arquivo = input('Digite um arquivo de texto, sem a extensão ".txt": ')
arquivo = arquivo + '.txt'
caractere = input('Digite um caractere: ')

cont = 0  # Contador de incidência daquele caractere no arquivo.

# Bloco try/except/else utilizado para ler o arquivo e exibir o número de vezes que o caractere aparece.
try:
    with open(arquivo, 'r') as arq:
        conteudo = arq.read()
        for char in conteudo:
            if char == caractere:
                cont += 1
except FileNotFoundError:
    print(' O arquivo digitado não existe.')
else:
    if cont != 0:
        print(f' O caractere "{caractere}" aparece {cont} vez(es) no arquivo.')
    else:
        print(f' O caractere "{caractere}" não aparece no arquivo.')
