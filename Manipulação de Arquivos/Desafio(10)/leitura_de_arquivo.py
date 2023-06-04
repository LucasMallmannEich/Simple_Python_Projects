"""
10 - Faça um programa que receba o nome de um arquivo de entrada e outro de saída. O arquivo de entrada contém em cada
linha o nome de uma cidade (ocupando 40 caracteres) e o seu número de habitantes. O programa deverá ler o arquivo de
entrada e gerar um arquivo de saída onde aparece o nome da cidade mais populosa seguida pelo seu número de habitantes.
"""

# Inserção de informações pelo usuário.
arq_ent = input('Digite o nome do arquivo de texto de entrada, sem a extensão ".txt": ')
arq_ent += '.txt'
arq_saida = input('Digite o nome do arquivo de texto de saída, sem a extensão ".txt": ')
arq_saida += '.txt'

populacao = []
encontrado = 0
x = 0

try:
    with open(arq_ent, 'r') as arq:
        for linha in arq.readlines():
            if x:
                populacao.append(linha[40:47])  # considerando que a população seja representada por 7 dígitos (máximo)
            else:
                x = 1
except FileNotFoundError:
    print('O arquivo digitado não foi encontrado.')
else:
    encontrado = 1

if encontrado:
    maior = 0  # variável para armazenar o maior número populacional

    for numero in populacao:
        numero = int(numero)
        if numero > maior:
            maior = numero

    maior_cidade = ''  # variavel para armazenar o nome da cidade com o maior número populacional

    with open(arq_ent, 'r') as arq:
        for linha in arq.readlines():
            if str(maior) in linha:
                maior_cidade = linha[0:39]  # considerando que o nome da cidade não exceda 39 caracteres

    # Loop for utilizado para excluir caracteres vazios, para que o tamanho da string seja o tamanho do nome da cidade.
    for caractere in maior_cidade:
        if caractere == ' ':
            maior_cidade = maior_cidade.replace(caractere, '')

    # Gerando o novo arquivo com as informações necessárias.
    with open(arq_saida, 'w', encoding='utf-8') as arq:
        arq.write(f' {maior_cidade} tem {maior} habitantes.')
    print(f' O novo arquivo foi gerado com sucesso.')