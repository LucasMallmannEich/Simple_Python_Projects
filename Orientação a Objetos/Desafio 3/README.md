Utilizando Classes e Objetos em Python

Proposta:

Escrever um código que apresente a classe "Quadrado", com atributos "lado", "area" e "perimetro".    
A classe também deve apresentar os métodos "calcular_area", "calcular_perimetro" e "imprimir".    
Os métodos "calcular_area" e "calcular_perimetro" devem efetuar seus respectivos cálculos e colocar os valores nos atributos "area" e "perimetro".    
O método "imprimir" deve mostrar na tela os valores de todos os atributos.      
Salienta-se que a área de um quadrado é obtida pela fórmula (lado * lado) e o perímetro por (4 * lado).

Resolução:

Crie uma classe, chamada "Quadrado", e crie seu método construtor em seu interior.            
A classe contém 3 atributos privados, sendo que apenas um deles será passado pelo método construtor (o lado).   
Antes de calcular os valores dos outros atributos, verifiquei se o lado é um valor inteiro e maior do que zero.       
Após isso, elaborei dois métodos: o método "calcular_area", que retorna o lado vezes o lado, e o método "calcular_perimetro", que retorna o lado vezes 4.    
Com isso pronto, declarei o atributo "area" sendo igual ao retorno do método "calcular_area" e declarei o atributo "perimetro" sendo igual ao retorno do método "calcular_perimetro".              
Por fim, codifiquei o método "imprimir", que, quando executado, imprime os valores instanciados do lado, da área e do perímetro.      
