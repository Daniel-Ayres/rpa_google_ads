
"""
  Define e prepara os diretórios base do projeto para armazenar arquivos gerados.

    - Cria a estrutura de pastas 'data/imagens' para salvar imagens baixadas.
    - Define o caminho do arquivo Excel onde os produtos serão registrados.
    - Cria a pasta 'logs' e define o caminho do arquivo de log de execução.
    - Garante que as pastas sejam criadas automaticamente se não existirem.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_IMAGENS = os.path.join(BASE_DIR, "data", "imagens")
ARQUIVO_EXCEL = os.path.join(BASE_DIR, "data", "produtos.xlsx")
ARQUIVO_LOG = os.path.join(BASE_DIR, "logs", "execucao.log")

os.makedirs(PASTA_IMAGENS, exist_ok=True)
os.makedirs(os.path.dirname(ARQUIVO_LOG), exist_ok=True)
