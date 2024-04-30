from unicodedata import normalize
from pathlib import Path
import csv

diretorio_temp = Path(__file__).resolve().parent.parent / "documentos/"

# Verifique se a pasta existe
if diretorio_temp.is_dir():
    # Liste os arquivos na pasta
    for dir_arquivo in diretorio_temp.iterdir():
        print("Arquivo: ", dir_arquivo)


def importa_csv():

    with open(f"{dir_arquivo}", "r", encoding="ISO-8859-1") as csvfile:
        reader = csv.DictReader(csvfile)
        data = {row["first_name"]: row["classification"] for row in reader}
    return data


def encode(name):
    ascii_name = (
        normalize("NFKD", name).encode("ascii", errors="ignore").decode("ascii")
    )
    return ascii_name.upper()


def classifica_nome(name):
    dados_nome = importa_csv()
    encoded_name = encode(name)

    if encoded_name in dados_nome:
        return dados_nome[encoded_name]
    else:
        return "I"
