"""
1 - Escreva um programa que:
(a) Cria/abra um arquivo de texto de nome "arq.txt";
(b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere '0';
(c) Feche o arquivo.
Agora, abra e leia o arquivo, caractere por caractere, e escreva na tela todos os caracteres armazenados.
"""

caractere = ''

with open('arq.txt', 'a') as arquivo:
    while caractere != '0':
        caractere = str(input('Digite um caractere que será gravado no arquivo "arq.txt": '))
        if caractere != '0':
            arquivo.write(caractere)

with open('arq.txt', 'r') as arquivo:
    lista = arquivo.readlines()
    if len(lista) != 0:
        for linha in lista:
            for char in linha:
                print(char)
        print(f' Todos os caracteres armazenados: {lista}.')

    else:
        print(' Você não digitou nenhum número.')

