#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

comprimento = float(input('Digite o comprimento da primeira reta: '))
comprimento2 = float(input('Digite o comprimento da segunda reta: '))
comprimento3 = float(input('Digite o comprimento da terceira reta: '))
if comprimento < comprimento2 + comprimento3 and comprimento2 < comprimento + comprimento3 and comprimento3 < comprimento + comprimento2:
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')
