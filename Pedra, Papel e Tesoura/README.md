Jogo: Pedra, Papel e Tesoura

Objetivo:

Elaborar um código que simule um jogo de pedra, papel e tesoura entre o usuário e o computador.   

Resolução:

Em primeiro lugar, importei a biblioteca "random".   
Após isso, defini uma lista chamada "options", que contém a palavra "pedra", "papel" e "tesoura".   
A variável "jogada_humana" (string) é informada pelo usuário do código.  
A variável "jogada_maquina" (string) é escolhida, de acordo com os valores presentes na lista "options", de forma aleatória pelo programa.   
Feito isso, se a "jogada_humana" for igual à "jogada_maquina", será impresso que o jogo empatou.   
Caso contrário, será impresso " Você venceu." ou " Você perdeu.", de acordo com as regras tradicionais do jogo.  
Por fim, se o usuário não digitou nenhum dos três nomes (pedra, papel ou tesoura), será impresso que ele deveria ter retornado algum destes valores.
