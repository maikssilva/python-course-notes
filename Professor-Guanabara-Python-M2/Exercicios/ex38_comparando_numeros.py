#Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print(f'O primeiro valor é {num} e o segundo valor é {num2}.')
if num > num2:
    print('O primeiro valor é maior.')
elif num2 > num:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')