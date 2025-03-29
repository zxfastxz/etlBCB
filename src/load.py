import pandas as pd

def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, dec:str):
    df.to_csv(nome_arquivo, sep=separador, decimal=dec)
    return
