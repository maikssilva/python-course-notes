# Variáveis e tipos de dados "básicos"

# Variáveis são espaços na memória que guardam valores

# Tipos de dados básicos: int, float, str, bool

# <nome da var> = <valor>  Atribuição de valor a uma variável

nome = "Maik" # Variável do tipo string (str), (texto), sempre entre aspas, (simples ou duplas)
idade = 32 # Variável do tipo inteiro (int), (recebe número sem casas decimais), não precisa de aspas
altura = 1.92 # Variável do tipo float, (recebe número com casas decimais), não precisa de aspas
dev = True # Variável do tipo booleano (bool), (recebe True ou False), não precisa de aspas

nome = input("Digite seu nome: ") # A variável nome agora recebe o valor digitado pelo usuário
idade = int(input("Digite sua idade: ")) # A variável idade agora recebe o valor digitado pelo usuário, convertido para inteiro
altura = float(input("Digite sua altura: ")) # A variável altura agora recebe o valor digitado pelo usuário, convertido para float

print(f"Olá, {nome}! Você tem {idade} anos e {altura}m de altura")