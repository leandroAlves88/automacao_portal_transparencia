"""
Realiza operacoes no banco de dados

funcoes:
    insere_dados
    busca_dados

"""

import conector_db as conector


def insere_dados(registros, tipo_relatorio):
    """Função para inserir registros no banco de dados - # insert"""
    try:
        conexao = conector.cria_conexao()
        cursor = conexao.cursor()

        data_list = registros.to_records(index=False).tolist()
        print("Gravando registro(s) no banco de dados")
        for row in data_list:
            if "receita" in tipo_relatorio:
                print("Inserindo Registro de despesas")
                print("Registros:\n", row)
                query = "INSERT INTO DB_PC.TB_RECEITA(Ano,Data_receita,Ficha_Receita,Conta_Contabil,Descricao,Codigo_DR,Descricao_DR,Orcado,Lancado,Arrecadado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(query, row)

            if "despesas" in tipo_relatorio:
                print("Inserindo Registro de despesas")
                print("Registros:\n", row)
                query = "INSERT INTO DB_PC.despesas (Empenho, Data_Despesa , CPFCNPJ , CredorFornecedor , Descricao , Mod_Lic , Licitacao, Empenhado , Liquidado , Pago) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(query, row)

            if "folha_pagamento" in tipo_relatorio:
                print("Inserindo Registro de folha de pagamento")
                print("Registros:\n", row)
                query = "INSERT INTO DB_PC.folha_pagamento (Nome_funcionario, Data_Admissao , Departamento, Cargo_Funcao , Salario_Base, Sexo) VALUES (%s,%s,%s,%s,%s,%s)"
                cursor.execute(query, row)

            if "holerite" in tipo_relatorio:
                print("Inserindo Registro de folha de pagamento")
                print("Registros:\n", row)
                query = "INSERT INTO DB_PC.folha_pagamento_holerite (Codigo_funcionario, Data_Admissao , Departamento, Cargo_Funcao , Salario_Base, Salario_Bruto, Vlr_Adiant, Vlr_Liquido) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(query, row)

        conexao.commit()
        return True

    except Exception as e:
        print(f"Erro ao Gravar Registro: {e}")
        return False
    finally:
        conector.fecha_conexao(cursor, conexao)


def busca_dados(tipo_relatorio):
    """Função para buscar registros no banco de dados - # select"""

    dados_consulta = []

    conexao = conector.cria_conexao()
    cursor = conexao.cursor()
    if "teste" in tipo_relatorio:
        cursor.execute("SELECT * FROM TESTE")
        for row in cursor.fetchall():
            dados_consulta.append(row)
    conector.fecha_conexao(cursor, conexao)
    return dados_consulta


def atualiza_dados():
    """# update"""
    return


def deleta_dados():
    """Função para inserir registros no banco de dados - # insert"""
    try:
        conexao = conector.cria_conexao()
        cursor = conexao.cursor()

        query = "DELETE FROM despesas"
        cursor.execute(query)
        conexao.commit()
        conector.fecha_conexao(cursor, conexao)

    except:
        conector.fecha_conexao(cursor, conexao)


def teste():
    """Metodo para teste de insert no banco"""
    dados = [7, "teste 5"]
    operacao = "teste"
    conector.insere_dados(dados, operacao)


__all__ = ["insere_dados", "busca_dados"]


# deleta_dados()

"""
resultado_teste = busca_dados("teste")
for i in range(len(resultado_teste)):
    print(resultado_teste[i])
"""

# Ler e exibir os resultados
# for row in cursor.fetchall():
#    print(row)
