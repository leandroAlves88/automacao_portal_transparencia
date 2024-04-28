import numpy as np
import pandas as pd
from pathlib import Path
import csv
import time
import operacoes_db as operacoes
from datetime import datetime

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
    time.sleep(3)
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
    df["Data"] = formata_data(df["Data"])
    df["CPF/CNPJ"] = remove_tabulacao(df["CPF/CNPJ"])
    df["Descrição"] = remove_tabulacao(df["Descrição"])
    df["Mod. Lic."] = remove_tabulacao(df["Mod. Lic."])
    df["Credor/Fornecedor"] = remove_tabulacao(df["Credor/Fornecedor"])
    df["Empenhado"] = converte_decimal(df["Empenhado"])
    df["Liquidado"] = converte_decimal(df["Liquidado"])
    df["Pago"] = converte_decimal(df["Pago"])
    return df


def converte_decimal(dados):
    print("Conversão para decimal")
    contador = 0
    data_list = dados.values
    nova_data_list = []
    for row in data_list:
        string_decimal_brasileiro = str(row[0])
        string_sem_ponto_e_virgula = string_decimal_brasileiro.replace(".", "").replace(
            ",", ""
        )
        string_com_ponto_decimal = (
            string_sem_ponto_e_virgula[:-2] + "." + string_sem_ponto_e_virgula[-2:]
        )
        brazilian_decimal_value = float(string_com_ponto_decimal)
        us_decimal_string = "{:.2f}".format(brazilian_decimal_value)
        nova_data_list.append(us_decimal_string)
        contador += contador
    print("Conversão finalizada")
    return nova_data_list


def remove_tabulacao(dados):
    print("Retirada de tabulacao")
    data_list = dados.values
    nova_data_list = []
    for row in data_list:
        valor_tabulado = str(row[0])
        valor_sem_tabulacao = valor_tabulado.replace("      ", "")
        nova_data_list.append(str(valor_sem_tabulacao))
    print("Tabulacao Removida")
    print("Tabulacao Removida: ", data_list)
    return nova_data_list


def formata_data(dados):
    print("Formatacao de data")
    data_list = dados.values
    nova_data_list = []
    for row in data_list:
        valor_data = str(row[0])
        print("Data Inicial: ", row)
        data_formatada = datetime.strptime(valor_data, "%d/%m/%Y").strftime("%Y-%m-%d")
        print("Data Convertida: ", data_formatada)
        nova_data_list.append(data_formatada)

    print("Tabulacao Removida")
    print("Tabulacao Removida: ", data_list)
    return nova_data_list


importa_csv()
