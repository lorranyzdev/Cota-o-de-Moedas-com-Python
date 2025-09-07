import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

# Requisição GET(pegar os dados)
resposta = requests.get(link)

# Transformando em dicionário
dic_resposta = resposta.json()

# Exibindo as moedas
for moeda in dic_resposta:
    dic_conversao_moeda = dic_resposta[moeda]  # dicionário da conversão da moeda
    valor_moeda = dic_conversao_moeda["bid"]   # preço de compra
    print(moeda, valor_moeda)
