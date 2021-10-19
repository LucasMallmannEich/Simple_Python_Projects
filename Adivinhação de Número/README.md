Adivinhando um Número Aleatório Gerado

Objetivo:

Elaborar um jogo de adivinhação de um número aleatório (entre 1 e 1000, inclusos) gerado pelo computador. 

Resolução:

Em primeiro lugar, importei o módulo "random".  
Em segundo lugar, declarei a variável int "numero" como um número aleatório entre 1 e 1000, inclusos.  
Após isso, entrei num "loop while True", que apenas será interrompido quando o usuário acertar o número aleatório gerado pela máquina do computador.   
Logo no início de cada ciclo do "loop", o usuário tentará acertar o número gerado, sendo que, a cada tentativa, a variável "cont" (int) será incrementada uma unidade.  
Feito esse processo, será verificado se a tentativa do usuário é certeira.  
Se ela for certeira, será impresso na tela que ele acertou e o "loop" será interrompido.  
Caso contrário, o programa o informará se a sua tentativa foi maior ou menor do que o número gerado aleatoriamente.   
Por fim, se o usuário não digitar um número ente 1 e 1000 (inclusos), será impresso na tela a seguinte frase: " Você deve informar um número entre 1 e 1000.".
