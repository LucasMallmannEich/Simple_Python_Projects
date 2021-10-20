Jogo da Forca

Objetivo:

Elaborar um jogo da forca utilizando a linguagem Python.

Resolução:

Para criar esse jogo da forca, utilizei uma lista de alimentos, ou seja, uma lista que contém as strings que podem aparecer no jogo.   
Logo no início do código, a variável "palavra" (do tipo string), seleciona, por meio da função "choice" (do módulo "random"), uma das palavras da lista.  
Após isso, utilizei um "loop for" para adicionar um "underline" à lista "impressao", de acordo com o número de caracteres da palavra sorteada. Ou seja, se a palavra sorteada for "bacon", a lista "impressao" será composta, neste primeiro momento, por cinco underlines.   
A variável "chances", do tipo inteiro (int), controla quantas chances o usuário precisará para acertar o nome.  
O número máximo de chances dadas será 6.  
Tendo isso em mente, criei um "loop while", em que a condição de parada dele será quando a variável "chances" for igual à 6, pois isso significa que as chances do usuário estão esgotadas.   
Então, criei um if para verificar se o usuário já havia ganho, ou seja, se a variável int "chances_certas" é igual ao tamanho da palavra sorteada.   
Se sim, o programa encerra o "loop" por meio de um "break" e imprime que o usuário venceu, além de mostar o número de vezes em que errou.   
Se o usuário ainda não venceu, ele dará um palpite, ou seja, digitará uma letra.  
Se a letra dada já foi informada alguma outra vez, o código diz ao usuário digitar uma letra diferente.   
Se a letra estiver na palavra sorteada, o código irá informar o usuário acerca disso e irá substituir todas as posições da lista "impressao" que tiverem o mesmo caractere nessa posição da "palavra", pela letra informada.   
Se a letra não estiver na palavra sorteada, o código informará isso ao usuário também.   
Após isso, a lista "letras_digitadas" irá adicionar à si mesma a letra informada pelo usuário nesse ciclo específico do "loop while".  
