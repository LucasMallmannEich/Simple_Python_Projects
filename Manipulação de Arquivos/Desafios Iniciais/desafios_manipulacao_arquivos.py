# Desafio 1 - Exiba todos os nomes dos inscritos que estão no arquivo inscritos.txt no console.

with open('inscritos.txt', 'r', encoding='utf-8') as arquivo:
    for nome in arquivo:
        print(nome, end='')

# Desafio 2 - Adicione o seu nome na lista de inscritos e depois mostre todos os nomes que estão no arquivo
# inscritos.txt no console.

with open('inscritos.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Lucas Mallmann Eich')

# Desafio 3 - Com o seu nome já na lista de inscritos, exiba o nome de cada pessoas que está inscrito na lista +
# o número que ele representa na lista em ordem crescente.
# (Ex.: 1 jhonatan , 2 Patricio Silva, 3 Kid Boy 3000).

with open('inscritos.txt', 'r', encoding='utf-8') as arquivo:
    pos = 1
    for subscriber in arquivo:
        print(f' {pos} {subscriber}')
        pos += 1