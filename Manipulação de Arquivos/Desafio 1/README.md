Manipulando Arquivos com a Utilização do "with"

Proposta: 

Escreva um programa que:           
(a) Cria/abra um arquivo de texto de nome "arq.txt";                   
(b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere '0';            
(c) Feche o arquivo.                                                                                               
Agora, abra e leia o arquivo, caractere por caractere, e escreva na tela todos os caracteres armazenados.           

Resolução:

Em primeiro lugar, declarei a variável caractere com um valor qualquer, para ser considerada uma variável do tipo "string".    
Em segundo lugar, utilizei um "with" para criar um arquivo de texto chamado "arq.txt" no modo "append", ou seja, toda vez que esse bloco "with" for executado, o programa irá adicionar mais conteúdo ao arquivo "arq.txt" sem que apague o que havia nele anteriormente.      
Então, dentro desse primeiro bloco "with", enquanto o usuário não digitar o caractere "0", o programa irá continuar pedindo a ele digitar um caractere a ser adicionado no arquivo de texto aberto/criado, por meio do método "write".   
Quando o usuário sair desse primeiro bloco, o programa irá entrar no segundo bloco "with", que agora irá abrir o arquivo "arq.txt" no modo "r", ou seja, no modo de leitura de arquivo.     
A variável "lista" será uma lista que conterá, em cada posição, uma string contendo o conteúdo de cada linha presente no arquivo de texto passado como parâmetro acima.    
Então, para cada caractere presente em cada linha desse arquivo, o programa imprime esse caractere.   
Ao final do programa, ele imprime todos os caracteres do arquivo "arq.txt", por meio da variável "lista".
