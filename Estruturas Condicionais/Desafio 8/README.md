Utilizando Estruturas Condicionais

Proposta:

Faça um programa que leia 2 notas de um aluno.        
Verifique se as notas são válidas e exiba na tela a média destas notas.        
Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0.                                     
Caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.             
          
Resolução:                      
             
Em primeiro lugar, utilizei um bloco try/except/else.     
A parte do "try" é responsável por captar os dados do usuário (ou ao menos tentar).          
Se o usuário não digitou um número, ele irá entrar num "ValueError", pois o input estava pedindo um float e o usuário não atendeu a esse pedido.     
Logo, se o usuário entrar nessa "Exception", o programa o informa que ele deveria ter digitado um número e se encerra.                               
Se o usuário digitou, de fato, um número qualquer, ele irá entrar na seção do "else".                                        
A partir daí, o programa já declara uma variável chamada "media", cujo valor será a média entre as duas notas informadas pelo usuário.            
Se ambas as notas informadas estiverem dentro dos parâmetros (entre 0 e 10, inclusos), o programa irá imprimir a média das duas notas passadas.     
Caso alguma das notas informadas não estiverem dentro dos parâmetros, o programa irá chegar ao fim, imprimindo na tela uma mensagem dizendo que a nota não possui valor válido.
