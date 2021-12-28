Utilizando Listas em Python

Proposta:

Escreva um programa que leia 10 números inteiros e os armazene em um vetor.      
Imprima o vetor, o maior elemento e a posição que ele se encontra.       

Resolução:

Em primeiro lugar, declarei uma lista sem nenhum valor.   
Essa lista será onde os números digitados pelo usuário do programa irão ser armazenados.    
Utilizando um "loop while", enquanto o tamanho da lista não for 10, a lista continuará armazenando os valores digitados pelo usuário.   
Após esse "loop while" se encerrar, declarei uma variável "maximo", que é igual ao maior valor contido na lista (fiz isso utilizando a função "max").    
Após isso, imprimi a lista e essa variável "maximo", como o vetor e o seu maior elemento, de forma respectiva.    
Por fim, com o intuito de localizar a posição em que o maior elemento está dentro dessa lista, utilizei a função "index()", escrevendo assim:    
"lista.index(maximo)" ---> retorna a posição do valor máximo na lista
