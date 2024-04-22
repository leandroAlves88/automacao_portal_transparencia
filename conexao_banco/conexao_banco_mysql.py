import mysql.connector
from mysql.connector import errorcode
from pathlib import Path
import configparser

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
    conn.close()
    conexao.close()


def insere_dados(registros, tipo_relatorio):
    # insert
    conexao = cria_conexao()
    cursor = conexao.cursor()
    if "teste" in tipo_relatorio:
        print("Inserindo Registro")
        query = "INSERT INTO DB_PC.TESTE (ID_TESTE,DESC_TESTE) VALUES (%s,%s)"
        cursor.execute(query, registros)
        conexao.commit()

    if "despesas" in tipo_relatorio:
        print("Inserindo Registro")
        query = "INSERT INTO DB_PC.despesas (Empenho, Data , CPFCNPJ , CredorFornecedor , Descricao , Mod_Lic , Licitacao, Empenhado , Liquidado , Pago) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query, registros)
        conexao.commit()

    fecha_conexao(cursor, conexao)
    return


def busca_dados(cursor):
    # select
    dados_consulta = ()
    cursor.execute("SELECT * FROM TESTE")
    return dados_consulta


def atualiza_dados():
    # update
    return


dados = [7, "teste 5"]
operacao = "teste"
insere_dados(dados, operacao)
# Ler e exibir os resultados
# for row in cursor.fetchall():
#    print(row)
