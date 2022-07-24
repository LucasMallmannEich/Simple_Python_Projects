"""
3 - Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais.
"""

# Declaração da variável que armazena o nome do arquivo.
arquivo = ''

# Captação do nome do arquivo, sem o ".txt".
while len(arquivo) == 0:
    arquivo = str(input('Digite o nome do arquivo, sem o ".txt": '))

# Acréscimo da extensão ".txt" ao nome do arquivo.
arquivo = arquivo + '.txt'

# Lista que possui as vogais da língua portuguesa.
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',
          'á', 'Á', 'é', 'É', 'í', 'Í', 'ó', 'Ó', 'ú', 'Ú',
          'â', 'Â', 'ê', 'Ê', 'î', 'Î', 'ô', 'Ô', 'û', 'Û',
          'ã', 'Ã', 'õ', 'Õ', 'à', 'À']

# Declaração e inicialização da variável que contabiliza o número de vogais presentes no arquivo.
cont = 0

# Bloco try/except/else utilizado para abrir o arquivo e extrair dele o número de vogais.
try:
    # Tenta abrir o arquivo informado pelo usuário.
    with open(arquivo, 'r', encoding='utf-8') as arq:
        conteudo = arq.read()
except FileNotFoundError:
    # Caso o arquivo não seja encontrado.
    print(' O arquivo não foi encontrado.')
else:
    # Utiliza um "loop for" para verificar todas os caracteres do arquivo informado.
    for caractere in conteudo:
        if caractere in vogais:
            cont += 1
    if cont == 0:
        print(f' Não há vogais neste arquivo de texto.')
    elif cont == 1:
        print(f' Neste arquivo de texto há 1 vogal.')
    else:
        print(f' Neste arquivo de texto há {cont} vogais.')
