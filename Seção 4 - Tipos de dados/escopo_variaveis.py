"""
Escopo de variáveis.

O escopo de variáveis são divididas em dois blocos:
    - Locais - As variáveis locais são definidas dentro do escopo de uma função e por isso só são reconhecidas dentro desse contexto.
    - Globais - As variáveis globais podem ser chamadas em todo o código.

A declaração de variáveis segue o mesmo padrão das outras, usando o =, porém no Python não é necessário declaras o tipo,
pois o mesmo usufrui da tipagem dinâmica, onde o tipo depende do valor declarada da variável.

nome_variavel = valor_variavel

Como o Python trabalha com tipo de variável dinâmica, ela também nos fornece uma possibilidade bem legal de reatribuição
de variável, porém deve ser usada com cautela, porque pode mudar a lógica do sistema.
"""

num = 42
print(num)
print(type(num))

# Reatribuição de variável
print("==============Reatribuição de variável================")
num = "Reatribuicao de variável"
print(num)
print(type(num))
var = "global"


def escopo_var():
    # A variável local só vai existir se entrar dentro do if
    var = "local"
    print(var)
    print(type(var))


print("===================Variável Local=====================")
escopo_var()
print("===================Variável Global=====================")
print(var)
print(type(var))
