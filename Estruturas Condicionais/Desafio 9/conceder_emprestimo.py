"""
9 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
Se a prestação for maior que 20% do salário imprima: "Empréstimo não concedido.".
Caso contrário imprima: "Empréstimo concedido.".
"""

try:
    salario = float(input('Digite o salário de um trabalhador:  '))
    prestacao_do_emprestimo = float(input('Digite o valor da prestação do empréstimo:  '))
except ValueError:
    print('Você deveria ter digitado números.')
else:
    if prestacao_do_emprestimo > 0 and salario > 0:
        if prestacao_do_emprestimo > (0.2 * salario):
            print(f'Empréstimo não concedido.\n')
        else:
            print(f'Empréstimo concedido.\n')
    else:
        print('Os valores deveriam ser números positivos.')
