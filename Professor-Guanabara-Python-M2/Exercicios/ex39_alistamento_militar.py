#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# - Se ele AINDA VAI SE ALISTAR ao serviço militar.
# - Se é a HORA DE SE ALISTAR
# Se já PASSOU DO TEMPO de alistamento.

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Digite o ano de nascimento: '))
from datetime import date
ano_atual = date.today().year   
idade = ano_atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}.')
if idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano_alistamento = ano + 18
    print(f'Seu alistamento será em {ano_alistamento}.')