# Primeira e última ocorrência de uma string    
# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A".
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ')
print(frase.upper)
print(f'A letra "a" aparece {frase.count('a')} vezes.')

print(f' A letra "a" aparece pela primeira vez na posição: {frase.find('a')}.')

print(f'A letra "a" aparece pela última vez na posição: {frase.rfind('a')}')

