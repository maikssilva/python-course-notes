# Manipulando texto 

# Fatiamento de strings - devemos lembrar que o primeiro caractere tem índice 0 - e utilizamos os colchetes para indicar o índice do caractere que queremos acessar com : dentro deles. 

# frase = '  Curso em Vídeo Python  '# print(frase) # Acessando a string inteira.
#print(frase[9:13]) # Acessando os índices 9, 10, 11 e 12 - o último índice não é incluído no fatiamento.

#print(frase[:5]) # Acessando os índices 0, 1, 2, 3 e 4 - o último índice não é incluído no fatiamento.

# print(frase[15:]) # Acessando os índices 15, 16, 17, 18, 19, 20 e 21 - o último índice não é incluído no fatiamento.

# print(frase[9::13]) # Acessando os índices 9, 22, 35 e 48 - o último índice não é incluído no fatiamento. - 

# #Análise de strings - len() - conta o número de caracteres da string, ou seja, o tamanho da string.

# frase = 'Curso em Vídeo Python'
# # print(len(frase)) # Acessando o tamanho da string.

# # print(frase.count('o',0,13)) # Acessando o número de vezes que o caractere '0' aparece na string - o último índice não é incluído no fatiamento.

# # print(frase.find('deo')) # Acessando o índice do caractere 'd' na string - o último índice não é incluído no fatiamento.

# print('curso'in frase) # Acessando se a string 'curso' está contida na string - Não é necessário utilizar colchetes nesse caso.

#TRANSFORMAÇÃO DE STRINGS -

# frase = '  Curso em Vídeo Python  '# print(frase) # Acessando a string inteira.

# print(frase.replace('Python','Android')) # Substituindo a string 'Python' por 'Android' na string 'frase'. Não altera a string original.

# print(frase.upper()) # Transforma todos os caracteres da string em maiúsculas.

# print(frase.lower()) # Transforma todos os caracteres da string em minúsculas.

# print(frase.capitalize()) # Transforma o primeiro caractere da string em maiúscula e o restante em minúsculas.

# print(frase.title()) # Transforma o primeiro caractere de cada palavra da string em maiúscula e o restante em minúsculas.

# print(frase.strip()) # Remove os espaços em branco do início e do fim da string.

# print(frase.rstrip()) # Remove os espaços em branco do fim da string.

# print(frase.lstrip()) # Remove os espaços em branco do início da string.

#DIVISÃOO DE STRINGS -

# frase = 'Curso em Vídeo Python'

# print(frase.split()) # Divide a string em uma lista de strings, utilizando o espaço em branco como separador.

# print('-'.join(frase)) # Junta as strings da lista em uma única string, utilizando o caractere '-' como separador.

