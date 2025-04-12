# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e a CONDIÇÃO DE PAGAMENTO:

# - Á vista dinheiro/cheque: 10% de desconto
# - Á vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print ('{:^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$ '))
print('''
FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))