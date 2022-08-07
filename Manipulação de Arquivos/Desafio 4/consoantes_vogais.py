"""
4 - Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais e quantas são
consoantes.
"""

# Captando o nome do arquivo por meio da inserção de dados do usuário.
arquivo = ''
while len(arquivo) == 0:
    arquivo = str(input('Digite o nome do arquivo, sem o ".txt": '))
arquivo = arquivo + '.txt'

# Lista que possui as vogais da língua portuguesa.
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',
          'á', 'Á', 'é', 'É', 'í', 'Í', 'ó', 'Ó', 'ú', 'Ú',
          'â', 'Â', 'ê', 'Ê', 'î', 'Î', 'ô', 'Ô', 'û', 'Û',
          'ã', 'Ã', 'õ', 'Õ', 'à', 'À']

# Lista que possui as consoantes da língua portuguesa.
consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
              'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y',
              'Z', 'Ç', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
              'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
              'x', 'y', 'z', 'ç']

# Contador de vogais e contador de consoantes, respectivamente.
cont_v = 0
cont_c = 0

# Bloco try/except/else para tentar abrir o arquivo.
try:
    # Tentativa de abrir o arquivo informado no modo de leitura.
    with open(arquivo, 'r') as arq:
        conteudo = arq.read()
except FileNotFoundError:
    # Caso o arquivo não tenha sido encontrado.
    print(' O arquivo informado não foi encontrado.\n')
else:
    # Contando os números de vogais e consoantes.
    for caractere in conteudo:
        if caractere in vogais:
            cont_v = cont_v + 1
        elif caractere in consoantes:
            cont_c = cont_c + 1

# Impressão do número de vogais e consoantes.
print(f' Número de Vogais: {cont_v}')
print(f' Número de Consoantes: {cont_c}')