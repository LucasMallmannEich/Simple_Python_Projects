Utilizando Estruturas de Repetição em Python

Proposta:

Faça um programa que leia 10 inteiros e imprima sua média.      

Resolução:

Em primeiro lugar, declarei a variável "soma", do tipo inteiro, para armazenar os números inteiros informados pelo usuário.     

```python
soma = 0
```

Após isso, escrevi um "loop for", com o auxílio do "range", para possibilitar ao usuário digitar dez números inteiros.   
Com o auxílio do "loop while" e do bloco "try/except/else", o usuário apenas irá para a próxima repetição do loop quando ele digitar um número inteiro.     

```python
for n in range(1, 11):
    num = ''
    while type(num) != int:
        try:
            num = int(input(f'Digite 10 números inteiros {n}/10: '))
        except ValueError:
            print('Você deveria ter digitado um número inteiro.\n')
        else:
            soma = num + soma
```

Ao final da captação dos números, o programa divide a soma de todos os números informados por 10, imprimindo o resultado dessa operação matemática.

```python
print(soma/10)
```
