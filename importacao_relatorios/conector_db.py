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


def insere_dados(registros, tipo_relatorio):
    """Função para inserir registros no banco de dados - # insert"""
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


def busca_dados(tipo_relatorio):
    """Função para buscar registros no banco de dados - # select"""

    dados_consulta = []

    conexao = cria_conexao()
    cursor = conexao.cursor()
    if "teste" in tipo_relatorio:
        cursor.execute("SELECT * FROM TESTE")
        for row in cursor.fetchall():
            dados_consulta.append(row)

    return dados_consulta


def atualiza_dados():
    """# update"""
    return


def teste():
    """Metodo para teste de insert no banco"""
    dados = [7, "teste 5"]
    operacao = "teste"
    insere_dados(dados, operacao)


"""
resultado_teste = busca_dados("teste")
for i in range(len(resultado_teste)):
    print(resultado_teste[i])
"""

# Ler e exibir os resultados
# for row in cursor.fetchall():
#    print(row)
