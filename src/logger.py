"""
  Configura o sistema de logs da aplicação para registrar eventos de execução.

    - Define o arquivo de log no caminho especificado em 'ARQUIVO_LOG'.
    - Define o modo de escrita ('w') para sobrescrever logs a cada execução.
    - Registra mensagens com nível de informação (INFO) e superiores.
    - Aplica formato padrão com data, nível e mensagem.
    - Usa codificação UTF-8 para suportar caracteres especiais.
"""


import logging
from src.config import ARQUIVO_LOG

def configurar_logger():
    logging.basicConfig(
        filename=ARQUIVO_LOG,
        filemode="w",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )
    logging.info("Logger configurado com sucesso.")
