Manipulação de Arquivos no Modo Leitura

Proposta:
  - Fazer um programa que peça ao usuário um arquivo de texto e mostre na tela quantas linhas este possui.

Considerações:
  - Um aspecto importante ao se realizar uma consulta de arquivos de texto informado pelo usuário é a verificação da existência destes;                         
  - Uma forma fácil e eficaz de realizar essa verificação pode ser feita utilizando o bloco try/except/else;                                
  - Esse bloco irá tentar, por meio da condição "try", abrir o arquivo de texto, sendo que, se ocorrer um erro, por meio da condição "except", de arquivo não encontrado ("FileNotFoundError"), ele irá imprimir uma mensagem na tela, ao invés de acusar um erro no programa;                        
  - Se tudo ocorrer bem e o arquivo de texto realmente existir, a condição "else" irá garantir que seja impresso o número de linhas que está presente no arquivo.                               
