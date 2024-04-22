from driver_automacao import busca_despesas
from importacao_relatorios import importa_despesas

busca_despesas.start_busca_relatorio_despesas()
importa_despesas.importa_csv()
# importa_despesas.grava_banco()
