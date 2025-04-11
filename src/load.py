import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, dec: str):
    """
    Salva um DataFrame em um arquivo CSV.

     Parâmetros:
        df (pd.DataFrame): O DataFrame que deve ser salvo.
        nome_arquivo (str): Caminho e nome do arquivo de saída (ex: 'dados.csv').
        separador (str): Caractere usado como separador de colunas no CSV (ex: ',' ou ';').
        decimal (str): Caractere usado para representar o ponto decimal (ex: '.' ou ',').

    returns:
    O DataFrame deve ser salvo em um arquivo .csv dentro da pasta de datasets.
    """
    # Verifica se o DataFrame está vazio
    df.to_csv(nome_arquivo, sep=separador, decimal=dec)
    return


def salvarSQlite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):

    conn = sqlite3.connect(nome_banco)

    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)

    conn.close()
    return


def salvarMySQL(
    df: pd.DataFrame, usuario: str, senha: str, host: str, banco: str, nome_tabela: str
):
    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")

    df.to_sql(nome_tabela, engine, if_exists="replace", index=False)

    return
