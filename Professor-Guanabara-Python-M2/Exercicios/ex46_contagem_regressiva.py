#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, indo de 10 até 0, com uma pausa de 1 segundo entre eles. 

# import time

# for i in range (10, 0, -1):
#     print(i)
#     time.sleep(1)

# print('Let us go')

# 2ª versão

import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela do windows

print('Contagem regressiva iniciando...\n')
time.sleep(1)

for i in range(10,0, -1):
    clear()
    print(f'\n\n\t\t{i} ⏳')
    time.sleep(1)

clear()
print("\n\n\t\t💥 Let us go! 💥")