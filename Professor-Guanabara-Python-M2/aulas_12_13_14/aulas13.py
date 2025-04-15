# Estruturas de controle 
# Laços de repetição são utilizados para repetir um bloco de código várias vezes.
# Existem dois tipos de laços de repetição em Python:
# 1. Laços de repetição com contagem definida (for)
# 2. Laços de repetição sem contagem definida (while)

# Prática   

# for c in range(0,7, 2):
#     print(c)
# print('FIM')    

# n = int(input('Digite um número: '))
# for c in range(0, n+1):
#     print(c)
# print('FIM')     

i = int(input('Início:  '))
f = int(input('FIM: ')) 
p = int(input('Passo:   '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
