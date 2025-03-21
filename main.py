import requests
import pandas as pd

def requestsApiBcb(data):



    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json"


    req = requests.get(url)
    dados = req.json()
    
    df2 = pd.json_normalize(dados['value'])
    return print(df2)
requestsApiBcb('20241')