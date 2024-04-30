from datetime import datetime
import classificacao_nomes as class_nome


def converte_decimal(dados):
    # print("Conversão para decimal")
    contador = 0
    data_list = dados.values
    nova_data_list = []
    for row in data_list:
        string_decimal_brasileiro = str(row[0])
        string_sem_ponto_e_virgula = (
            string_decimal_brasileiro.replace(".", "")
            .replace(",", "")
            .replace("R$ ", "")
        )
        string_com_ponto_decimal = (
            string_sem_ponto_e_virgula[:-2] + "." + string_sem_ponto_e_virgula[-2:]
        )
        brazilian_decimal_value = float(string_com_ponto_decimal)
        us_decimal_string = "{:.2f}".format(brazilian_decimal_value)
        nova_data_list.append(us_decimal_string)
        contador += contador
    # print("Conversão finalizada")
    return nova_data_list


def remove_tabulacao(dados):
    # print("Retirada de tabulacao")
    data_list = dados.values
    nova_data_list = []
    for row in data_list:
        valor_tabulado = str(row[0])
        valor_sem_tabulacao = valor_tabulado.replace("      ", "")
        nova_data_list.append(str(valor_sem_tabulacao))
    # print("Tabulacao Removida")
    # print("Tabulacao Removida: ", data_list)
    return nova_data_list


def formata_data(dados):
    print("Formatacao de data")
    data_list = dados.values
    nova_data_list = []
    for row in data_list:
        valor_data = str(row[0])
        # print("Data Inicial: ", row)
        data_formatada = datetime.strptime(valor_data, "%d/%m/%Y").strftime("%Y-%m-%d")
        # print("Data Convertida: ", data_formatada)
        nova_data_list.append(data_formatada)

    # print("Tabulacao Removida")
    # print("Tabulacao Removida: ", data_list)
    return nova_data_list


def validacao_genero(dados):
    data_list = dados.values
    nova_data_list = []
    for row in data_list:
        nome = str(row[0])
        nome_split = nome.split()
        print("Nome -> ", nome_split[0], end=" | ")
        primeiro_nome = nome_split[0]
        if primeiro_nome[-1] is "O":
            print(
                "Sexo -> O",
            )
            nova_data_list.append("M")
        elif primeiro_nome[-1] is "A":
            print(
                "Sexo -> M",
            )
            nova_data_list.append("F")
        else:
            sexo = class_nome.classifica_nome(primeiro_nome)
            print("Sexo ->", sexo)
            nova_data_list.append(sexo)

    """with open("nomes_identificados.txt", "w") as arquivo:
        # Escreve cada item da lista seguido por uma quebra de linha
        for item in nova_data_list:
            arquivo.write("%s\n" % item)"""

    return nova_data_list
