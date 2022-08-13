faturamento = [
                  {
                      "estado": "SP",
                      "valor": 67836.43
                  },
                  {
                      "estado": "RJ",
                      "valor": 36678.66
                  },
                  {
                      "estado": "MG",
                      "valor": 29229.88
                  },
                  {
                      "estado": "ES",
                      "valor": 27165.48
                  },
                  {
                      "estado": "Outros",
                      "valor": 19849.53
                  },
]

total = 0
for item in faturamento:
    total = total + item['valor'];

print(total)

for elem in faturamento:
    lucro = elem['valor']/(total/100)
    print(elem['estado'], ' : ', lucro, '%')
