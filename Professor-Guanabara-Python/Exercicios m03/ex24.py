#Verificando as primeiras letras de um texto       
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

city = input('Digite o nome de uma cidade: ') 

print(f'A cidade que você digitou é: {city}!')

print(f'A cidade {city} começa com "Santo"? {city.find('Santo')}')