# Desafio 16 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

import math
num = float(input('Digite um número: '))
inteiro = math.trunc(num)
print(f'O número {num} tem a parte inteira {inteiro}')