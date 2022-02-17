Utilizando Estruturas Condicionais em Python

Proposta:

Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal.
Utilizando as seguintes fórmulas (onde h corresponde a altura):
Homens: (72.7 * h) - 58
Mulheres: (62.1 * h) - 44.7

Resolução:
 
Em primeiro lugar, utilizei um bloco try/except/else, com o objetivo de validar se os dados informados pelo usuário são do tipo correto.           
Se os dados estiverem corretos, o programa ainda irá verificar se a altura da pessoa informada é maior do que zero.     
Se os dados estarem de acordo com esses requisitos, o programa irá calcular, por meio da fórmula dada na proposta do desafio, o peso ideal para as mulheres e o peso ideal para os homens.         
Se o sexo informado for masculino ou masculino, o programa irá dizer o peso ideal para essa pessoa.   
Se o sexo informado não corresponder a nenhum dessas duas opções, o programa irá informar o usuário que ele deveria ter digitado "masculino" ou "feminino" como valor para o sexo da pessoa.
