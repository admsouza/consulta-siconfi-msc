import requests
import pandas as pd


# URL da API
# API_URL = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/msc_patrimonial"
API_URL = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/msc_orcamentaria"


params = {
    "id_ente": "2509909",
    "an_referencia": "2023",
    "me_referencia": "1",
    "co_tipo_matriz": "MSCC",
    "classe_conta": "6",
    "id_tv": "period_change"
}


headers = {
    "Accept": "application/json"
}

response = requests.get(API_URL, params=params, headers=headers)


if response.status_code == 200:
    # Extraindo os dados JSON
    data = response.json()

    # Verificando a estrutura dos dados
    print("Resposta da API:", data)


    datasiconfi = []

    # Verifique se 'items' está na resposta e é uma lista
    if isinstance(data, dict) and 'items' in data and isinstance(data['items'], list):
        # Iterando sobre cada item da lista

        for item in data['items']:

            if isinstance(item, dict):
                # conta_contabil = item.get("conta_contabil")
                # fonte_recursos = item.get("fonte_recursos")
                  poder_orgao = item.get("poder_orgao")

                # Filtrar dadoss
            if (poder_orgao == "20231"):

                    apitce = {
                    "tipo_matriz": item.get("tipo_matriz"),
                    "cod_ibge": item.get("cod_ibge"),
                    # "classe_conta": item.get("classe_conta"),
                    "conta_contabil": item.get("conta_contabil"),
                    "poder_orgao": item.get("poder_orgao"),
                    # "financeiro_permanente": item.get("financeiro_permanente"),
                    # "ano_fonte_recursos": item.get("ano_fonte_recursos"),
                    "fonte_recursos": item.get("fonte_recursos"),
                    # "exercicio": item.get("exercicio"),
                    # "mes_referencia": item.get("mes_referencia"),
                    # "divida_consolidada": item.get("divida_consolidada"),
                    # "data_referencia": item.get("data_referencia"),
                    # "entrada_msc": item.get("entrada_msc"),
                    # "valor": item.get("valor"),
                    # "natureza_conta": item.get("natureza_conta"),
                    # "tipo_valor": item.get("tipo_valor"),
                    # "complemento_fonte": item.get("complemento_fonte"),
                }
                    datasiconfi.append(apitce)

        # Convertendo os dados para um DataFrame do Pandas
        if datasiconfi:
            df = pd.DataFrame(datasiconfi)
            filename = f"Dados retornados.xlsx"


            # Exportando os dados para um arquivo Excel
            df.to_excel(filename, index=False)

            print("Dados exportados com sucesso")
        else:
            print("Nenhum dado válido para exportar")
    else:
        print("Erro: 'items' não encontrado ou a estrutura não é uma lista")
else:
    print(f"Erro na requisição: {response.status_code} - {response.text}")
