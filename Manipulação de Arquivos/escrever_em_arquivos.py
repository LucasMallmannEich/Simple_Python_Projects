"""
Escrevendo em Arquivos

# OBS.: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas lê-lo.
Da mesma forma, se abrirmos um arquivo para a escrita, não podemos efetuar sua leitura, apenas escrever neste arquivo.

# OBS.: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Essa função recebe uma string como parâmetro (se não digitarmos uma string como parâmetro, teremos um TypeError).

Abrindo um arquivo para escrita com o modo 'w':
- se o arquivo não existir, ele será criado.
- se o arquivo já existir, o anterior será totalmente substituído pelo texto que escrevermos.
Dessa forma, todo o conteúdo no arquivo anterior é perdido.
"""

# Exemplo de escrita - modo 'w' - 'write' (escrever):

with open('writing.txt', 'w') as arquivo:
    arquivo.write(' Banco de dados: SQL.\n')
    arquivo.write(' Não sei programar em Java.\n')
    arquivo.write(' Sou inciante na programação há um ano.')

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = str(input('Digite uma fruta ou digite "sair": '))
        if fruta == 'sair':
            break
        else:
            arquivo.write(f'{fruta}\n')
