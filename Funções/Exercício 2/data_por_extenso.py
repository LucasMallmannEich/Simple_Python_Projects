# 2 - Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela no formato textual por
# extenso. Exemplo: Data: 01/01/2000, Imprimir: 1 de Janeiro de 2000.


def data(dia, mes, ano):
    if mes == 1 and 0 < dia < 32:
        return f' {dia} de Janeiro de {ano}.'
    elif mes == 2 and 0 < dia < 30:
        return f' {dia} de Fevereiro de {ano}.'
    elif mes == 3 and 0 < dia < 32:
        return f' {dia} de Março de {ano}.'
    elif mes == 4 and 0 < dia < 31:
        return f' {dia} de Abril de {ano}.'
    elif mes == 5 and 0 < dia < 32:
        return f' {dia} de Maio de {ano}.'
    elif mes == 6 and 0 < dia < 31:
        return f' {dia} de Junho de {ano}.'
    elif mes == 7 and 0 < dia < 32:
        return f' {dia} de Julho de {ano}.'
    elif mes == 8 and 0 < dia < 32:
        return f' {dia} de Agosto de {ano}.'
    elif mes == 9 and 0 < dia < 31:
        return f' {dia} de Setembro de {ano}.'
    elif mes == 10 and 0 < dia < 32:
        return f' {dia} de Outubro de {ano}.'
    elif mes == 11 and 0 < dia < 31:
        return f' {dia} de Novembro de {ano}.'
    elif mes == 12 and 0 < dia < 32:
        return f' {dia} de Dezembro de {ano}.'
    return ' Digite uma data válida da próxima vez.'


dia1 = int(input('Digite o dia: '))
mes1 = int(input('Digite o mês: '))
ano1 = int(input('Digite o ano: '))

print(data(dia1, mes1, ano1))
