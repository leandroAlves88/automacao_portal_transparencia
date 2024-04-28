import pandas as pd
from pathlib import Path
import csv
import operacoes_db as operacoes
import utils


diretorio_temp = Path(__file__).resolve().parent.parent / "dir_download/despesas/"

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
    sucesso = operacoes.insere_dados(dados, "despesas")
    if sucesso is True:
        print("Registro(s) Gravado com sucesso")


def tratamento_dados(datafame):
    print("Limpeza e padronização dos dados")
    df = datafame
    df = df.drop("Data", axis=1, level=0)
    df = df.drop(df.index[-1])
    df = df.rename(columns={"": "Data"})
    df["Data"] = utils.formata_data(df["Data"])
    df["CPF/CNPJ"] = utils.remove_tabulacao(df["CPF/CNPJ"])
    df["Descrição"] = utils.remove_tabulacao(df["Descrição"])
    df["Mod. Lic."] = utils.remove_tabulacao(df["Mod. Lic."])
    df["Credor/Fornecedor"] = utils.remove_tabulacao(df["Credor/Fornecedor"])
    df["Empenhado"] = utils.converte_decimal(df["Empenhado"])
    df["Liquidado"] = utils.converte_decimal(df["Liquidado"])
    df["Pago"] = utils.converte_decimal(df["Pago"])
    return df


# importa_csv()
