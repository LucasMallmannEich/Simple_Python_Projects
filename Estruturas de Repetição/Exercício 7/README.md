Exercício 7 

Proposta:
  - Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.

Solução:  
  - As seguintes variáveis são usadas para controlar qual será o valor da soma e qual será o número de valores positivos inseridos.
  ```
  soma = 0
  contador_positivos = 0
  ```
  
  - O "contador_positivos" deve chegar à 10, de acordo com o que foi dito no enunciado.
  - Além disso, o bloco try/except/else serve para tratar erros que possam surgir caso o usuário digite um tipo de valor errado na inserção de dados.
  ```
  while contador_positivos < 10:
    try:
        num = int(input('Digite um número positivo: '))
    except ValueError:
        print('Você deve digitar um número positivo. Por favor, tente novamente.')
    else:
        if num > 0:
            contador_positivos = contador_positivos + 1
            soma = soma + num
    
