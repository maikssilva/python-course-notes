#Procurando uma string dentro de outra 
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome. 

name = input('Digite seu nome completo: ')

print(f'Seu nome é: {name}')

print(f'O nome {name} possui "Silva" no nome? {name.find('Silva')}')