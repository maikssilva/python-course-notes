#Analisador de textos

#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")) #correção (adicionar str antes do input)
print(f'Seu nome é: {nome}')

print(f'Seu nome com todas as letras maiúsculas é: {nome.upper()}')

print(f'Seu nome com todas as letras minúsculas é: {nome.lower()}')

print(f'Seu nome tem {len(nome) - nome.count(" ")} letras.')

print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras.')


