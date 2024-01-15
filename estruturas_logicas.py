"""
Estruturas lógicas

Operadores unários
    - not
Operadores binários:
    - and, or
Operadores de identidade - Utilizados para comparar os objetos, testando se suas referências são do mesmo objeto
    - is, is not
"""
ativo = True
logado = False
print("Nome usuário:")
nome = input().title()

print("\n======================Operadores Lógicos===========================")
if ativo and logado:
    print(f"Bem Vindo, {nome}")
else:
    print("Você precisa ativar sua conta, cheque seu e-mail!")

print("\n===================Operadores de identidade========================")
if ativo is logado:
    print("Referenciam o mesmo objeto")
    print(f"Ativo: {ativo}\nLogado: {logado}")
else:
    print("Não referenciam o mesmo objeto")
