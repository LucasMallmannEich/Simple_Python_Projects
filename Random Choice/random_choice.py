import random

number = int(input('Type the number of players: '))

list_players = []

while len(list_players) != number:
    list_players.append(input(f'Type the name of player {len(list_players)+1}: '))

raffled_player = random.choice(list_players)

print(f' The raffled player is {raffled_player}. Congratulations!')
