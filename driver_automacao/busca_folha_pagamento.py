from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import time


diretorio_temp = (
    Path(__file__).resolve().parent.parent / "dir_download/folha_pagamento/"
)
print(f"{diretorio_temp}")
chrome_options = Options()

preferences = {
    "download.default_directory": f"{diretorio_temp}",
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True,
    "profile.default_content_settings.popups": 0,
}
chrome_options.add_experimental_option("prefs", preferences)

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
navegador.maximize_window()
__URL = "https://servicos.santanadeparnaiba.sp.gov.br/cecam_transparencia/Pages/Geral/wfFolhaPagamentoServidor.aspx"
__XPATH_CAMPO_DT_INICIAL = '//*[@id="cphConteudo_rpnCadastro_detInicial_I"]'
__XPATH_CAMPO_DT_FINAL = '//*[@id="cphConteudo_rpnCadastro_detFinal_I"]'
__XPATH_BTN_PESQUISAR = '//*[@id="cphConteudo_btnPesquisarImg"]'
__XPATH_BTN_EXPORTAR = '//div[@title="Exportar"]'
__XPATH_BTN_EXPORTA_CSV = (
    '//*[@id="cphConteudo_ucFormatoDownload_ppcDownload_rpnucDownload_btnCSV"]'
)
__XPATH_BLOQ_TELA = '//*[@id="btnMsgOKImg"]'


def clica(driver, by, elemento):
    print(f"Clicando no elemento: {elemento}")
    tentativa = 0
    element = driver.find_element(by, elemento)
    if element.is_displayed():
        print("Elemento Disponível para click")
        element.click()
        time.sleep(3)
    else:
        while element.is_displayed():
            time.sleep(5)
            tentativa += 1
            print(f"Tentativa {tentativa} de clicar no botão")
            if tentativa > 3:
                return


def clica_tela_bloqueio(driver, by, elemento):
    time.sleep(3)
    print(f"Aguardando {3} segundos")
    print(f"Clicando no elemento tela bloqueio: {elemento}")
    tentativa = 0
    element = driver.find_element(by, elemento)
    if element.is_displayed():
        print("Elemento Disponível para click")
        element.click()
        time.sleep(3)
    else:
        while element.is_displayed():
            time.sleep(5)
            tentativa += 1
            print(f"Tentativa {tentativa} de clicar no botão")
            if tentativa > 3:
                return


def limpa_campo(driver, by, elemento):
    driver.find_element(by, elemento).clear()
    time.sleep(1)
    print(f"Limpando campo do elemento: {elemento}")


def escreve(driver, by, elemento, texto):
    driver.find_element(by, elemento).send_keys(texto)
    time.sleep(2)
    print(f"Escrevendo texto {texto} no elemento: {elemento}")


def start_busca_relatorio_despesas():
    print("---Iniciando busca do relatorio de despesa---")
    navegador.get(__URL)
    time.sleep(3)

    limpa_campo(navegador, By.XPATH, __XPATH_CAMPO_DT_INICIAL)
    escreve(navegador, By.XPATH, __XPATH_CAMPO_DT_INICIAL, "01/01/2024")

    # WebDriverWait.until(ExpectedCondition())
    limpa_campo(navegador, By.XPATH, __XPATH_CAMPO_DT_FINAL)
    escreve(navegador, By.XPATH, __XPATH_CAMPO_DT_FINAL, "31/01/2024")

    clica(navegador, By.XPATH, __XPATH_BTN_PESQUISAR)

    clica(navegador, By.XPATH, __XPATH_BTN_EXPORTAR)

    clica_tela_bloqueio(navegador, By.XPATH, __XPATH_BLOQ_TELA)

    clica(navegador, By.XPATH, __XPATH_BTN_EXPORTA_CSV)
    time.sleep(20)
    print("---Fim da busca do relatorio de despesa---")


start_busca_relatorio_despesas()
