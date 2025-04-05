#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
computador = randint(0, 5) # Faz o computador pensar
jogador = int(input('Tente adivinhar o número que o computador pensou entre 0 e 5: ')) # Jogador tenta adivinhar
if jogador == computador:
    print('Parabéns! Você acertou! O número era {}.'.format(computador))
else:
    print('Você errou! O número era {}.'.format(computador))