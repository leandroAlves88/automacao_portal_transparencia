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


def gera_dataframe(dados, cabecalho):

    df = pd.DataFrame(dados, columns=[cabecalho])
    df.head()
    return df


def importa_csv():
    print("Importando arquivo")
    time.sleep(3)
    with open(f"{arquivo}", "r", encoding="ISO-8859-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        dados = list(reader)

    print("\n\nDeletando Cabeçalho")
    del dados[0:6]

    print("\n\nPrintando dados")
    for row in range(0, 10):
        print(f"{row} - {dados[row]}")

    dados_padronizados = tratamento_dados(gera_dataframe(dados[1::], dados[0]))
    grava_banco(dados_padronizados)
    print("arquivo Importado com sucesso")


def grava_banco(dados):
    print("Gravando no banco de dados")
    print(dados)
    time.sleep(3)


def tratamento_dados(datafame):
    print("Limpeza e padronização dos dados")
    df = datafame
    df = df.drop(columns=["Data"])
    df = df.rename(columns={"": "Data"})
    print(f"Tamanho dos dados: {df.shape}")
    return df


importa_csv()
