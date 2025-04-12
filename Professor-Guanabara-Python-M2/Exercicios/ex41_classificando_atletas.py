# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 20 anos: SÊNIOR
# - Acima de 25 anos: MASTER

ano = int(input('Digite o ano de nascimento: '))
from datetime import date
ano_atual = date.today().year
idade = ano_atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('MIRIM')          
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 20:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')