# Crie um programa que faça o computador jogar JOKENPO com você.

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) # 0 = Pedra, 1 = Papel, 2 = Tesoura
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # Computador jogou Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('Jogada inválida')
elif computador == 1:
    # Computador jogou Papel
    if jogador == 0:
        print('Computador Venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Venceu')
    else:
        print('Jogada inválida')
elif computador == 2:
    # Computador jogou Tesoura
    if jogador == 0:
        print('Jogador Venceu')
    elif jogador == 1:
        print('Computador Venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')
# Fim do jogo   