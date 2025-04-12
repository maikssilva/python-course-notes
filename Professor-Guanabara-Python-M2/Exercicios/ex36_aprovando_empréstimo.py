#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o VALOR DA CASA, o SALÁRIO, do comprador e em QUANTOS ANOS ele vai pagar. 

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. 

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = casa / (anos * 12)
print(f'A prestação mensal será de R$ {prestacao:.2f}')
if prestacao <= salario * 0.3:
    print('Empréstimo Aprovado!')
else:
    print('Empréstimo Negado!')