# 6 - Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos e segundos.
# Você deve convertê-los em segundos.


def tempo(h, m, seg):
    return h*3600+m*60+seg


horas = int(input(' Digite a quantidade de horas: '))
minutos = int(input(' Digite a quantidade de minutos: '))
segundos = int(input(' Digite a quantidade de segundos: '))

print(f' O horário informado totaliza {tempo(horas, minutos, segundos)} segundos.')
