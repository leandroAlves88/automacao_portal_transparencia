import pandas as pd
from pathlib import Path
import csv
import operacoes_db as operacoes
import utils

TIPO_RELATORIO = "receita"
dir_arquivo_receita = ""
diretorio_temp = Path(__file__).resolve().parent.parent / "dir_download/receitas/"

# Verifique se a pasta existe
if diretorio_temp.is_dir():
    # Liste os arquivos na pasta
    for dir_arquivo_receita in diretorio_temp.iterdir():
        print("Arquivo receita csv: ", dir_arquivo_receita)


def gera_dataframe(dados, cabecalho):
    print(cabecalho)
    df = pd.DataFrame(dados, columns=[cabecalho])
    df.head()
    return df


def importa_csv():
    print("Importando arquivo arquivo de receita")
    with open(f"{dir_arquivo_receita}", "r", encoding="ISO-8859-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        dados = list(reader)

    print("\n\nDeletando Cabeçalho do CSV")
    # del dados[0:5]
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
    df["Data"] = utils.formata_data(df["Data"])
    df["Descrição"] = utils.remove_tabulacao(df["Descrição"])
    df["Descrição DR"] = utils.remove_tabulacao(df["Descrição DR"])
    df["Orçado (R$)"] = utils.converte_decimal(df["Orçado (R$)"])
    df["Lançado (R$)"] = utils.converte_decimal(df["Lançado (R$)"])
    df["Arrecadado (R$)"] = utils.converte_decimal(df["Arrecadado (R$)"])
    return df


# importa_csv()
