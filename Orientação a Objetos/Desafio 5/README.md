Utilizando Classes e Objetos em Python

Proposta:

Escreva um código que apresente a classe "Circulo", com atributos "raio", "area" e "perimetro".                
A classe ainda deve ter os métodos "calcular_area", "calcular_perimetro" e "imprimir".             
Os métodos "calcular_area" e "calcular_perimetro" devem efetuar seus respectivos cálculos e colocar os valores nos atributos "area" e "perimetro".                     
O método "imprimir" deve mostrar na tela os valores de todos os atributos.             
Salienta-se que a área de um círculo é obtida pela fórmula (pi * raio * raio) e o perímetro por (2 * pi * raio).

Resolução:  

Em primeiro lugar, eu importei a biblioteca "math", afinal, irei usar o valor exato de pi para efetuar os cálculos necessários do programa.          
Em segundo lugar, criei uma classe "Circulo", que é inicializada com o valor do raio.      
Antes de avançar, verifiquei se o tipo do valor do raio é um float ou é um int.         
Se não for, o programa irá avisar o usuário que ele deveria ter digitado um valor numérico.        
Após isso, atribui valores aos atributos "area" e "perimetro" por meio das funções "calcular_area" e "calcular_perimetro", respectivamente.       
Para implementar o método "imprimir", efetuei mais algumas verificações, como verificar se o raio passado pelo usuário é igual ou maior do que zero.            
Após isso, testei o código escrito e conclui que ele se comportou de maneira satisfatória.                      
