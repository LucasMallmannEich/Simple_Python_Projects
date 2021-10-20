# 2 - Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes.
# A primeira vez deve usar a estrutura de repetição for, a segunda while, e a terceira while True e break.

for num in range(1, 101):
    print(num)

num = 1
while num < 101:
    print(num)
    num = num + 1

num = 1
while True:
    if num < 101:
        print(num)
    else:
        break
    num = num + 1
