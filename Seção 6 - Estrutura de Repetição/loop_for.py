"""
Estrutura de repetição FOR - Utilizado para iterar sobre sequências.
As estrutura de repetição tendem a diminuir a repetição de código para a mesma finalidade.
"""
# Definindo as variáveis globais
nome = "Geek University"
lista = [1,2,3,4,5]
numeros = range(1,10)

# Iterando a variável nome do tipo string
print("=======================Iterando uma string=======================")
for letra in nome:
    print(letra, end='-')

# Iterando a variável lista do tipo lista
print("\n==================Iterando uma lista de números====================")
for item in lista:
    print(item, end="")

# Iterando o range números
print("\n======================Iterando um range===========================")
for n in numeros:
    print(n, end='')

# Enumerate
# Quando não precisar do valor, basta desconsiderar com underline(_)
print("\n======================Iterando com enumerate=======================")
for valor in enumerate(nome):
    print(valor, end='')

print("\n")
for _, letra in enumerate(nome):
    print(letra, end='')

print("\n")

print("=======================Iterando emojis========================")
# https://app.timwhitlock.info/emogi/tables/unicode
for letra in range(3):
    for num in range(1, 11):
        print('\U0001F605' * num)
