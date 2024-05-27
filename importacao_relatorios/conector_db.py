"""
Conexão com o banco de dados

funcoes:
    cria_conexao
    fecha_conexao

"""

import configparser
from pathlib import Path
import mysql.connector
from mysql.connector import errorcode

diretorio_config = Path(__file__).resolve().parent.parent / "documentos/"

parser = configparser.ConfigParser()
parser.read(f"{diretorio_config}\\config.properties")

config = {
    "user": parser["mysql"]["username"],
    "password": parser["mysql"]["password"],
    "host": parser["mysql"]["server"],
    "database": parser["mysql"]["database"],
    "raise_on_warnings": True,
}


def cria_conexao():
    """Função para uma conexão com o banco de dados MySQL"""
    try:
        conn = mysql.connector.connect(**config)
        print("Conexão ao banco de dados MySQL bem-sucedida.")
        return conn
    except mysql.connector.Error as error:
        print(f"Erro ao conectar ao SQL Server: {error}")
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database não existe")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario ou senha errado")
        else:
            print(error)


def fecha_conexao(conn, conexao):
    """Função para fechar a conexão do banco"""
    conn.close()
    conexao.close()
