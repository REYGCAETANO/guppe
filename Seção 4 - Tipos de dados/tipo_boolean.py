"""
Tipo booleano
Este tipo de dado trabalha com duas variantes, ou seja, é binária: True e False

Operações básicas:
NOT - A negação de um booleano resulta no inverso dele.
    not True = False
    not Flase = True
OR - Está operação válida duas variáveis, onde pelo menos uma delas precisa ser verdadeira para o resultado ser True.
    True or False = True
    False or False = False
AND - Está operação também trabalha de forma binária, onde os dois valores precisam ser verdadeiro para o resultado ser True
    True and True = True
    False and True = False
"""
valor1 = True
valor2 = False
valor3 = True
valor4 = False

print("\n")
print("------------------Operação not (Negação de valores-------------------------)")
print(f"not {valor1} => {not valor1}")
print(f"not {valor2} => {not valor2}")

print("-------------------------------Operação AND---------------------------------")
print(f"{valor1} and {valor2} => {valor1 and valor2}")
print(f"{valor1} and {valor3} => {valor1 and valor3}")

print("---------------------------------Operação OR--------------------------------")
print(f"{valor1} or {valor2} => {valor1 or valor2}")
print(f"{valor1} or {valor3} => {valor1 or valor3}")
print(f"{valor2} or {valor4} => {valor2 or valor4}")

