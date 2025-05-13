# n1 = input('Digite um valor: ') 
# print(type(n1)) 
# The input function always returns a string. To convert it to an integer, use the int() function.
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
# print('A soma entre', n1, 'e', n2, 'vale', s)
print ('A soma entre {} e {} vale {}'.format(n1, n2, s))
# The {} are placeholders for the variables that will be passed to the format method.