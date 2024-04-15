import numpy as np
import pandas as pd
from pathlib import Path
import csv
import time

arquivo = ""
diretorio_temp = Path(__file__).resolve().parent / "dir_download/receitas"

# Verifique se a pasta existe
if diretorio_temp.is_dir():
    # Liste os arquivos na pasta
    for arquivo in diretorio_temp.iterdir():
        print("Arquivo: ", arquivo)


def importa_pandas():

    print(f"Diretorio arquivo: {diretorio_temp}")

    # Leia o arquivo CSV para um DataFrame
    df = pd.read_csv("Despesas.csv", encoding="ISO-8859-1", sep=";")
    df = tratamento_dados(df)
    # Imprima as primeiras linhas do DataFrame
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
    # df = df.drop(columns=[2])
    print(f"Tamanho dos dados: {df.shape}")
    return df


importa_pandas()
# importa_csv()
grava_banco()
