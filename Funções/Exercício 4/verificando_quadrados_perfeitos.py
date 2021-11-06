#  4 - Faça uma função para verificar se um número é um quadrado perfeito. Um quadrado perfeito é um número inteiro não
# negativo que pode ser expresso como o quadrado de outro número inteiro. Ex.: 1, 4, 9...


def quadrado_perfeito(numero):
    soma = 0
    if numero >= 0:
        for n in range(0, numero+1):
            if n**2 == numero:
                soma = soma + 1
        if soma == 0:
            return ' Esse número não é um quadrado perfeito.'
        return ' Esse número é um quadrado perfeito.'
    return ' O número não pode ser negativo para ser testado, pois não existem quadrados perfeitos negativos.'


num = int(input('Digite um número inteiro não negativo: '))

print(quadrado_perfeito(num))
