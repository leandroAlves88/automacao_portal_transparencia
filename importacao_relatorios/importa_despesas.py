import numpy as np
import pandas as pd
from pathlib import Path
import csv
import time

diretorio_temp = Path(__file__).resolve().parent.parent / "dir_download/despesas/"

# Verifique se a pasta existe
if diretorio_temp.is_dir():
    # Liste os arquivos na pasta
    for arquivo in diretorio_temp.iterdir():
        print("Arquivo: ", arquivo)


def importa_pandas():

    print(f"Diretorio arquivo: {diretorio_temp}")

    # Diretorio arquivo para importacao
    arquivo = f"{diretorio_temp}\Despesas.csv"
    df = pd.read_csv(arquivo, encoding="ISO-8859-1", sep=";")
    df = tratamento_dados(df)
    print(df)


def importa_csv():
    print("Importando arquivo")
    time.sleep(3)
    with open(f"{arquivo}", "r", encoding="ISO-8859-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            print(row)
    print("arquivo Importado com sucesso")


def grava_banco():
    print("Gravando no banco de dados")
    print("...")
    time.sleep(3)


def tratamento_dados(datafame):
    print("Limpeza e padronização dos dados")
    df = datafame
    df = df.drop(df.index[:6])
    df.head()
    # time.sleep(2)
    # df = df.drop(columns=[2])
    # df.iat[0, 1] = "Data"
    # novas_colunas = df.iloc[0]
    # df.columns = novas_colunas
    # df = df.drop(df.index[:1])
    print(f"Tamanho dos dados: {df.shape}")
    return df


importa_pandas()
# importa_csv()
grava_banco()
