"""
6 - Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas vezes cada letra do alfabeto
aparece dentro do arquivo.
"""

# Inserção do nome do arquivo pelo usuário.
arquivo = input('Digite um arquivo de texto, sem a extensão ".txt": ')
arquivo = arquivo + '.txt'

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

letras = []

for i in range(26):
    letras.append(0)

# Bloco try/except/else utilizado para captar os dados e realizar a sua leitura.
try:
    with open(arquivo, 'r') as arq:
        conteudo = arq.read()
        for letra in conteudo:
            if letra.lower() in alfabeto:
                letras[alfabeto.index(letra.lower())] += 1
except FileNotFoundError:
    print('O arquivo não foi encontrado.\n')
else:
    for i in range(26):
        print(f' A letra "{alfabeto[i]}" aparece {letras[i]} vezes no arquivo digitado.\n')
