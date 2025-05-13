#Primeiro e último nome de uma pessoa   
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o últino nome separadamente: 

name = input('Digite seu nome completo: ')

print(f'Seu nome completo é: {name}')

print(f'Seu primeiro nome é: {name.split()[0]}')

print(f' Seu último nome é: {name.split()[-1]}')
