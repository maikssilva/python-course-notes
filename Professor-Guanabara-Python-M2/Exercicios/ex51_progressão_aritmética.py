# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. 

primeiro = int(input('Primeiro termo:    '))
razão = int(input('Razão:   '))
for c in range (primeiro, 10, razão):
    print(f'{c}', end= ' → ')
print('ACABOU')