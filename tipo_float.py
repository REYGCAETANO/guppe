"""
Tipo float(decimal, real) - casas Decimais

Obs: O separador de casas decimais é o ponto e não a vírgula

Obs: Números complexos são definidos colocando o j no final do valor da variável
"""
# Do ponto de vista do float está errado, mas o comando é aceito e gera uma dupla de inteiros.
valor = 1,44
print(valor)

# Certo do ponto de vista do float
valor1 = 1.4
print(valor1)

# Dupla atribuição
valor2, valor3 = 2, 3
print(valor2)
print(type(valor2))
print(valor3)
print(type(valor2))

# Conversão de float para int
conv_int = int(valor1)
print(conv_int)
print(type(conv_int))

# Números complexos
num_complexo = 5j
print(num_complexo)
print(type(num_complexo))
