"""
14 - Faça um programa que leia um vetor de 10 posições, verifique se existem valores numéricos iguais e os escreva na tela.
"""
tupla = ()
repetidos = ()
# Bloco try/except/else para captar os valores da tupla do usuário.
for i in range(10):
    while len(tupla) < 10:
        try:
            num = float(input('Digite um número: '))
        except ValueError:
            print(' Você deve digitar um valor numérico.')
        else:
            if num in tupla:
                repetidos += (num, )
            tupla += (num, )

if len(repetidos) == 0:
    print(' Não há nenhuma repetição nesse vetor.')
else:
    print(f' Valores repetidos: {repetidos}')
