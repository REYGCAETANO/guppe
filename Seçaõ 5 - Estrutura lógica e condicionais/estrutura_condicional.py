"""
Estrutura condicionais
if, else, elif

Obs.: Os blocos de códigos de condicionais, métodos começam depois de dois pontos e 4 espaçamentos na próxima linha.
Obs.: As condições podem ser feitos somente com IF's, mas se tiver somente uma resposta, será uso de recursos sem necessidade,
pois seria mais interessante e performático usar IF, ELIF e ELSE, pois ao atender uma condição não verificaria as outras.
"""
idade = 19
if idade < 18:
    print("Menor de idade!", idade)
elif idade == 18:
    print("Você tem 18 anos")
else:
    print("Maior de idade!", idade)
