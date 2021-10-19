import random

options = ['pedra', 'papel', 'tesoura']
jogada_humana = str(input('Digite se você quer escolher "pedra", "papel" ou "tesoura": '))
jogada_maquina = random.choice(options)

print(f' A máquina escolheu {jogada_maquina.upper()}.')

if jogada_humana == jogada_maquina:
    print(' Empate.')
elif jogada_humana == 'papel' and jogada_maquina == 'pedra':
    print(' Você venceu.')
elif jogada_humana == 'papel' and jogada_maquina == 'tesoura':
    print(' Você perdeu.')
elif jogada_humana == 'tesoura' and jogada_maquina == 'pedra':
    print(' Você perdeu.')
elif jogada_humana == 'tesoura' and jogada_maquina == 'papel':
    print(' Você venceu.')
elif jogada_humana == 'pedra' and jogada_maquina == 'tesoura':
    print(' Você venceu.')
elif jogada_humana == 'pedra' and jogada_maquina == 'papel':
    print(' Você perdeu.')
else:
    print(' Você deveria ter retornado um dos valores a seguir: "papel", "pedra", "tesoura".')
