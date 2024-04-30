import pandas as pd
from pathlib import Path
import csv
import operacoes_db as operacoes
import utils

TIPO_RELATORIO = "folha_pagamento"

diretorio_temp = (
    Path(__file__).resolve().parent.parent / "dir_download/folha_pagamento/folha/"
)

# Verifique se a pasta existe
if diretorio_temp.is_dir():
    # Liste os arquivos na pasta
    for dir_arquivo in diretorio_temp.iterdir():
        print("Arquivo: ", dir_arquivo)


def gera_dataframe(dados, cabecalho):
    print(cabecalho)
    df = pd.DataFrame(dados, columns=[cabecalho])
    df.head()
    return df


def importa_csv():
    print("Importando arquivo")
    with open(f"{dir_arquivo}", "r", encoding="ISO-8859-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        dados = list(reader)

    print("\n\nDeletando Cabeçalho do CSV")
    del dados[0:6]
    dados_padronizados = tratamento_dados(gera_dataframe(dados[1::], dados[0]))
    grava_banco(dados_padronizados)
    print("arquivo Importado com sucesso")


def grava_banco(dados):
    sucesso = operacoes.insere_dados(dados, TIPO_RELATORIO)
    if sucesso is True:
        print("Registro(s) Gravado com sucesso")


def tratamento_dados(datafame):
    print("Limpeza e padronização dos dados")
    df = datafame
    df = df.drop(df.index[-1])
    df["Data de Admissão"] = utils.formata_data(df["Data de Admissão"])
    df["Valor Base"] = utils.converte_decimal(df["Valor Base"])
    df["Sexo"] = utils.validacao_genero(df["Nome"])
    print(datafame)

    return df


importa_csv()
