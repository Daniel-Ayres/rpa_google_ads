"""
  Fornece utilitários para manipulação de nomes de arquivos e download de imagens.

    - limpar_nome_arquivo(nome): remove caracteres inválidos e limita o tamanho do nome.
    - salvar_imagem(url_img, caminho): baixa a imagem a partir de uma URL e salva localmente em formato PNG.

    Recursos:
      • Utiliza expressões regulares para sanitizar nomes de arquivo.
      • Faz requisição HTTP com timeout de 10 segundos.
      • Usa a biblioteca Pillow (PIL) para abrir e salvar imagens.
      • Retorna True se o download e salvamento forem bem-sucedidos, caso contrário False.
"""

import re
import os
from io import BytesIO
import requests
from PIL import Image

def limpar_nome_arquivo(nome):
    nome_limpo = re.sub(r'[\\/*?"<>|]', "", nome)
    return nome_limpo[:80]

def salvar_imagem(url_img, caminho):
    try:
        resp = requests.get(url_img, timeout=10)
        if resp.status_code == 200:
            image = Image.open(BytesIO(resp.content)).convert("RGBA")
            image.save(caminho)
            return True
    except Exception as e:
        print(f"Erro ao salvar imagem: {e}")
    return False
