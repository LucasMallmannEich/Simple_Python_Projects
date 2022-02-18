Utilizando Estruturas Condicionais em Python

Proposta:

Escreva um programa que leia um número inteiro maior do que zero.      
Ele precisa devolver, na tela, a soma de os seus algarismos.           
Por exemplo, ao número 251 corresponderá o valor 8(2+5+1).             
Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".

Resolução:

Eu utilizei um bloco try/except/else, com o intuito de verificar se a informação captada pelo usuário atendia aos requisitos desse desafio.   
Antes de iniciar a lógica do programa, verifiquei se o dado informado pelo usuário é um número inteiro maior do que zero.    
Se sim, transformei o número para uma string e utilizei um "loop for" para percorrer cada posição da string do número informado.    
Então, a cada repetição do loop, o programa somava determinada posição da string, transformando o valor para um inteiro, com a variável "soma".  
Ao final do programa, ele exibe a variável "soma", informando ao usuário qual é o valor da soma de todos os caracteres do número por ele informado anteriormente.
