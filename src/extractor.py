"""
  Realiza a extração de produtos do Google Shopping e salva os resultados em planilha.

    - Acessa o Google Shopping usando Selenium e BeautifulSoup.
    - Coleta título, preço, loja, link e imagem dos produtos encontrados.
    - Limita a extração a uma quantidade máxima de produtos (padrão: 20).
    - Baixa e salva as imagens localmente na pasta configurada.
    - Gera uma planilha Excel com os dados extraídos.
    - Registra logs do processo de execução.

    Parâmetros:
        driver (uc.Chrome): navegador ativo do Selenium.
        termo_pesquisa (str): termo a ser pesquisado no Google Shopping.
        limite (int): número máximo de produtos a coletar (padrão: 20).

    Retorna:
        str: caminho do arquivo Excel gerado com os dados dos produtos.
"""

import os
import time
import pandas as pd
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils import limpar_nome_arquivo, salvar_imagem
from src.config import PASTA_IMAGENS, ARQUIVO_EXCEL
import logging

def extrair_produtos(driver, termo_pesquisa="Geladeira", limite=20):
    logging.info(f"Iniciando extração de: {termo_pesquisa}")
    print(f"Buscando produtos de: {termo_pesquisa}")

    params = {
        "q": termo_pesquisa,
        "tbm": "shop",
        "hl": "pt-BR",
        "gl": "br",
        "udm": "28"
    }

    url = "https://www.google.com/search?" + urlencode(params)
    driver.get(url)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "pla-unit-container"))
    )

    produtos = []
    tentativas = 0

    while len(produtos) < limite and tentativas < 15:
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        itens = soup.find_all("div", class_="pla-unit-container")

        for item in itens:
            if len(produtos) >= limite:
                break

            titulo = item.find("div", class_="bXPcId")
            preco = item.find("span", class_="VbBaOe")
            loja = item.find("div", class_="UsGWMe")
            link = item.find("a", class_="plantl")
            img = item.find("div", class_="pla-unit-img-container")

            img_src = img.find("img")["src"] if img and img.find("img") else None

            if img_src and img_src.startswith("http"):
                produtos.append({
                    "titulo": titulo.get_text(strip=True) if titulo else "",
                    "preco": preco.get_text(strip=True) if preco else "",
                    "loja": loja.get_text(strip=True) if loja else "",
                    "url_produto": link["href"] if link else "",
                    "img_url": img_src
                })

        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(5)
        tentativas += 1

    logging.info(f"{len(produtos)} produtos coletados.")

    os.makedirs(PASTA_IMAGENS, exist_ok=True)

    for prod in produtos:
        nome_img = limpar_nome_arquivo(prod["titulo"]) + ".png"
        caminho_img = os.path.join(PASTA_IMAGENS, nome_img)
        salvar_imagem(prod["img_url"], caminho_img)


    df = pd.DataFrame(produtos)
    df.to_excel(ARQUIVO_EXCEL, index=False)

    logging.info(f"Planilha gerada em {ARQUIVO_EXCEL}")

    return ARQUIVO_EXCEL
