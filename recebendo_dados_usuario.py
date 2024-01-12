"""
Recebendo dados do usuário
"""

# Entrada de dados
# print("Qual seu nome?")
nome = input("Qual seu nome? ").title()

#Exemplo de print 'antigo' 2.x
# print("Seja bem-vindo(a) %s" % nome)

# Exemplo de print moderno 3.x
# print("Seja bem-vindo(a) {0}".format(nome.title()))

# print("Qual dia idade?")
idade = int(input("Qual dia idade?"))

# Exemplo de print mais atual > 3.7
print(f"Seja bem-vindo(a) {nome}")
# Processamento de dados

# Saída de dados
print("A(o) %s tem %s anos de idade" % (nome.title(), idade))

# Cast é a conversão do tipo de dados
print(f"A(o) {nome} nasceu em {2024- idade}")