from random import choice

comidas = ['feijão', 'banana', 'acarajé', 'arroz', 'uva', 'limão', 'laranja', 'manga', 'pão', 'queijo', 'presunto',
           'ovo', 'bacon', 'sanduíche', 'carne', 'grão-de-bico', 'manteiga', 'maionese', 'quindim', 'pêssego']

palavra = choice(comidas)
tam = len(palavra)

chances = 0

impressao = []
for i in range(tam):
    impressao.append('_')

chances_certas = 0

letras_digitadas = []

while chances != 6:
    if chances_certas == tam:
        print(f' Você venceu! Você só errou {chances} vezes.')
        break
    palpite = str(input('Digite uma letra: '))
    if palpite in letras_digitadas:
        print(' Você já digitou essa letra. Tente outra vez!')
    elif palpite in palavra and palpite not in impressao:
        print(' Parabéns! Essa letra está contida na palavra.')
        for i in range(tam):
            if palpite == palavra[i]:
                impressao[i] = palpite
                chances_certas = chances_certas + 1
    else:
        chances = chances + 1
        print(f' Esta letra não está na palavra. Chances erradas: {chances}.')
    letras_digitadas.append(palpite)
    print(impressao)

if chances == 6:
    print(' Você perdeu!')
    print(f' A palavra era: "{palavra}".')
