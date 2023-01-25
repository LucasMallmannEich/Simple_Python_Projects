Estruturas Condicionais em Python

Proposta:
  - 14 - A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10.
  - Respectivamente: a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
  - A média das três notas mencionadas anteriormente obedece aos pesos:
  - Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5.
  - De acordo com o resultado,mostre na tela se o aluno está reprovado (média entre 0 e 2.9), recuparação (entre 3 e 4.9).
  - Ou se foi aprovado. Faça todas as verificações necessárias.

Resolução:
  - Utilizei um bloco try/except/else para poder realizar a validação de dados recebidos do usuário.
  - Caso o usuário tenha digitado um valor não numérico ou um valor menor que 0 ou maior que 10, um erro do tipo "ValueError" será gerado.
