import json

with open("dados.json", encoding='utf-8') as my_json:
    dados = json.load(my_json)

menor = dados[0]['valor']
maior = dados[0]['valor']

for item in dados:
    if(item['valor'] < menor):
        menor = item['valor']
    if(item['valor'] > maior):
        maior = item['valor']

print('O maior faturamento foi: ', maior)
print('O menor faturamento foi: ', menor)

soma = 0
contador = 0

for item in dados:
    if(item['valor'] != 0):
        soma = soma + item['valor']
        contador = contador + 1

media = soma / contador

print('A média é de: ', media)

superiorMedia = 0

for item in dados:
    if(item['valor'] > media):
        superiorMedia = superiorMedia + 1

print('O faturamento foi maior que média em ', superiorMedia, ' dias')
