#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
if num > num2 and num > num3:
    maior = num
    menor = num2 if num2 < num3 else num3
elif num2 > num and num2 > num3:
    maior = num2
    menor = num if num < num3 else num3
else:
    maior = num3
    menor = num if num < num2 else num2
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')