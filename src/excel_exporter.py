
"""
  Lê os dados de produtos salvos no arquivo Excel e exibe-os ordenados por preço.

    - Carrega o arquivo Excel definido em 'ARQUIVO_EXCEL'.
    - Converte os valores de preço para formato numérico removendo símbolos e vírgulas.
    - Ordena os produtos do mais barato ao mais caro.
    - Exibe os 20 primeiros resultados com título, preço, loja, URL e imagem.
    - Retorna o DataFrame ordenado.
"""

import pandas as pd
from src.config import ARQUIVO_EXCEL

def ordenar_por_preco():
    print("\nProdutos ordenados do mais barato para o mais caro:")
    print("-" * 80)
    print("                    ")

    df = pd.read_excel(ARQUIVO_EXCEL)

    df["preco_num"] = (
        df["preco"]
        .astype(str)
        .str.replace("R$", "")
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float, errors="ignore")
    )

    df_ordenado = df.sort_values(by="preco_num", ascending=True).reset_index(drop=True)

    for i, (_, row) in enumerate(df_ordenado.iterrows(), start=1):
        print(f"#{i:02d}")
       
        print("                     ")
        print(f"Título   : {row['titulo']}")
        print(f"Preço    : {row['preco']}")
        print(f"Loja     : {row['loja']}")
        print(f"URL Loja     : {row['url_produto']}")
        print(f"Imagem URL   : {row.get('img_url', 'N/A')}")
       
        print("-" * 80)
        print("                     ")

        if i >= 20:
            break

    return df_ordenado
