# 3 - Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado dos componentes deste vetor.
# Assim, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.

counter = 0
conjunto1 = []
conjunto2 = []

while counter != 10:
    conjunto = float(input('Digite um número real: '))
    conjunto1.append(conjunto)
    counter += 1

for x in conjunto1:
    x1 = x*x
    conjunto2.append(x1)

print(conjunto1)
print(conjunto2)
