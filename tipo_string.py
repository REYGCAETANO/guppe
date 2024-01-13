"""
Tipo String
    O tipo string normalmente está entre aspas, mas no Python além de simples, podem ser aspas duoplas ou triplas.
    Ex.: "Teste", 'Teste', '''Teste''' """"teste""""
"""
palintromo = "Socorram me subino onibus em marrocos"
print("-----------------------Aspas Simples-----------------------------")
print('Geek')
print('Upper Geek'.upper())
print("Lower Geek".lower())
print("Title Geek".title())
print("Split Geek University".split())
print("Split[0] Geek".split()[0])
print("Slice Geek"[1:5])
print("Replace Geek".replace('e', 'a'))

print("-----------------------Aspas Duplas------------------------------")
print("University")
print("Upper University".upper())
print("Lower University".lower())
print("Title University".title())
print("Split University".split())
print("Split[0] Title University".split()[0])
print("Slice University"[0:3])
print("Slice University"[::-1])
print("Replace University".replace('i', 'y'))

print("-----------------------Aspas Triplas-----------------------------")
print("""Python""")
print("Upper Python".upper())
print("Lower Python".lower())
print("Title Python".title())
print("Split Python".split())
print("Split[0] Python".split()[0])
print("Slice Python"[0:4])
print("Slice Python"[::-1])
print("Replace Python".replace('th', 'x'))

print(palintromo)
print(palintromo[::-1])
