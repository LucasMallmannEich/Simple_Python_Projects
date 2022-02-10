Utilizando Classes e Objetos em Python

Proposta:

Escreva um código que apresente a classe "Retangulo", com atributos "comprimento", "largura", "area" e "perimetro".      
Essa classe também deve ter os métodos "calcular_area", "calcular_perimetro" e "imprimir".      
Os métodos "calcular_area" e "calcular_perimetro" devem efetuar seus respectivos cálculos e colocar os valores nos atributos "area" e "perimetro".             
O método "imprimir" deve mostrar na tela os valores de todos os atributos.               
Salienta-se que a área de um retângulo é obtida pela fórmula (comprimento * largura) e o perímetro pela fórmula (2*comprimento) + (2*largura).

Resolução:

Crie uma classe, chamada "Retangulo", e crie seu método construtor em seu interior.                                 
A classe contém 4 atributos privados, sendo que apenas dois deles ("comprimento" e "largura") será passado pelo método construtor.          
Antes de calcular os valores dos outros atributos, verifiquei se o comprimento e a largura digitada são número não negativos.       
Se eles não atenderem aos atributos anteriores, o programa indicará um erro.     
Após isso, elaborei dois métodos: o método "calcular_area", que retorna o comprimento vezes a largura, e o método "calcular_perimetro", que retorna o comprimento vezes 2 mais a largura vezes 2.     
Com isso finalizado, declarei o atributo "area" sendo igual ao retorno do método "calcular_area" e declarei o atributo "perimetro" sendo igual ao retorno do método "calcular_perimetro".
Por fim, codifiquei o método "imprimir", que, quando executado, imprime os valores instanciados do lado, da área e do perímetro.
