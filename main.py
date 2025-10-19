"""
  Ponto de entrada principal do RPA para extração de anúncios do Google Shopping.

    - Configura o sistema de logs.
    - Inicializa o navegador com o undetected_chromedriver.
    - Realiza a extração de até 20 produtos com base no termo de pesquisa.
    - Fecha o navegador após a coleta dos dados.
    - Lê e ordena os produtos extraídos do arquivo Excel por preço.
"""

from src.logger import configurar_logger
from src.browser import iniciar_navegador
from src.extractor import extrair_produtos
from src.excel_exporter import ordenar_por_preco
import logging


def main():
    configurar_logger()
    print("-" * 80)
    print("Iniciando RPA Google Ads...\n")

    driver = iniciar_navegador()
    try:
        extrair_produtos(driver, termo_pesquisa="Playstation 5", limite=20)
    finally: 
        logging.info(f"Fechando o navegador.")

    # Leitura e ordenação dos resultados salvos
    ordenar_por_preco()

if __name__ == "__main__":
    main()
