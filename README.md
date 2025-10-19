# 🛒 RPA Google Shopping Ads

Este projeto é uma automação RPA desenvolvida em Python que realiza pesquisas no Google Shopping, coleta automaticamente informações sobre produtos (título, preço, loja, link e imagem), salva os dados em uma planilha Excel e baixa as imagens localmente.
Todo o processo é registrado por logs, garantindo rastreabilidade da execução.

⚙️ Observação: no momento, o script está fixo para realizar pesquisas sobre “Ar condicionado” em geral, mas pode ser facilmente adaptado para outros produtos modificando o parâmetro termo_pesquisa no arquivo main.py.

---

## 📌 Funcionalidades

- Navegação automatizada com Selenium (via undetected_chromedriver)

- Extração de título, preço, loja, URL e imagem de cada produto

- Download automático das imagens em pasta local

- Exportação dos dados para planilha .xlsx

- Leitura e ordenação dos produtos por preço

- Registro completo da execução em arquivo de log

---

## 🧱 Estrutura do Projeto

```bash
rpa_google_ads/
│
├── data/                     # Armazena as planilhas e imagens baixadas (não versionadas)
├── logs/                     # Contém os arquivos de log da execução (não versionadas)
│
├── src/                      # Código-fonte organizado por responsabilidade
│   ├── __pycache__/          # (Gerado automaticamente pelo Python)
│   ├── browser.py            # Inicializa o navegador com undetected_chromedriver
│   ├── config.py             # Define caminhos e cria pastas automaticamente
│   ├── excel_exporter.py     # Ordena e exibe os produtos do Excel
│   ├── extractor.py          # Extrai dados dos produtos do Google Shopping
│   ├── logger.py             # Configura o sistema de logs
│   └── utils.py              # Funções auxiliares (ex: limpar nome e salvar imagem)
│
├── venv/                     # Ambiente virtual (não versionado)
│
├── main.py                   # Ponto de entrada principal da automação
├── README.md                 # Documentação do projeto
└── requirements.txt          # Lista de dependências do projeto
                
```

## 🚀 Como Executar

### **1️⃣ Clone o repositório**

```bash
git clone https://github.com/Daniel-Ayres/rpa_google_ads.git
cd rpa_google_ads
```

### 2️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```
### 3️⃣ Execute o script principal

```bash
python main.py
```
### 4️⃣ Após a execução

### 📁 A planilha será gerada em:

```bash
data/produtos.xlsx
```
### 🖼️ As imagens serão salvas em:

```bash
data/imagens/
```

### 🪵 O log estará disponível em:
```bash
logs/execucao.log
```


## 📦 Bibliotecas Utilizadas

| Biblioteca | Descrição |
|-------------|------------|
| **undetected-chromedriver** | Evita bloqueios automáticos do Google durante o uso do Selenium. |
| **selenium** | Controla o navegador Chrome para navegar e extrair informações da página. |
| **beautifulsoup4** | Faz o parsing do HTML para identificar e extrair dados estruturados. |
| **pandas** | Organiza os dados coletados em formato tabular e exporta para Excel. |
| **openpyxl** | Engine usada pelo `pandas` para salvar os dados em planilhas `.xlsx`. |
| **requests** | Baixa as imagens dos produtos a partir das URLs obtidas. |
| **pillow (PIL)** | Manipula e salva as imagens no formato `.png`. |
| **logging** | Gera logs detalhados da execução, permitindo rastrear cada etapa. |
| **os** | Manipula diretórios e caminhos de arquivos, criando automaticamente as pastas `data/` e `logs/`. |
| **time** | Controla os intervalos de espera entre as ações automatizadas. |
| **re** | Limpa caracteres inválidos nos nomes dos arquivos de imagem. |


## ❓ Por que essas bibliotecas?

- **🧭 undetected-chromedriver** — Evita bloqueios automáticos do Google que ocorrem com o Selenium padrão, permitindo uma navegação mais estável e confiável durante a raspagem.  

- **🧠 selenium** — Controla o navegador Chrome em tempo real, possibilitando interações com páginas dinâmicas e elementos carregados via JavaScript.  

- **🪄 beautifulsoup4** — Simplifica a extração de dados do HTML renderizado, permitindo localizar e estruturar facilmente as informações de cada produto.  

- **📊 pandas** — Facilita a **manipulação e organização dos dados coletados**, além de permitir exportá-los rapidamente para planilhas Excel.  

- **📘 openpyxl** — É a **engine recomendada pelo pandas** para leitura e escrita de arquivos `.xlsx`, garantindo compatibilidade com o Excel.  

- **🖼️ pillow e requests** — Trabalham em conjunto para **baixar e salvar imagens dos produtos automaticamente**, convertendo-as para formatos padronizados como `.png`.  

- **🧾 logging** — Responsável por **registrar toda a execução da automação**, incluindo informações, avisos e possíveis erros, garantindo rastreabilidade completa.  

- **📂 os / re / time** — Utilitários essenciais para **manipular arquivos, limpar nomes de imagens e controlar os intervalos de espera** durante o processo de extração.  



## 🧪 Exemplo de Saída no Terminal

```bash

--------------------------------------------------------------------------------
Iniciando RPA Google Ads...


Buscando produtos de: Ar condicionado


Produtos ordenados do mais barato para o mais caro:
--------------------------------------------------------------------------------

#01

Título   : Ar condicionado janela 7500 BTUsConsul frio com design moderno - CCB07FB 220V
Preço    : R$ 1.439,00
Loja     : Amazon.com.br
URL Loja     : https://www.amazon.com.br/condicionado-janela-Consul-design-moderno/dp/B0BZ2DBPZT?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A3LGV2SX75WN63
Imagem URL   : https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcR7idpv8_yQo0u5RTiBIwpq1FKiBK1bu_EuDw3pmK-C0T3K7xiQUQ2qs6fES1XsvWQHMsCtPSkTJGMF4_dwWaWoNXgYT318_vPUvEAcTZRWDW_rc4Xdp0wpgWBibfBdzDgQ-YD3PcFmUg&usqp=CAc
--------------------------------------------------------------------------------

#02

Título   : Ar Condicionado Janela 7500BTUs Frio 127V Mecânico Midea
Preço    : R$ 1.476,90
Loja     : Leroy Merlin
URL Loja     : https://www.leroymerlin.com.br/ar-condicionado-janela-7500-btus-frio-branco-127v--110v--mecanico-midea_92031555?store_code=57
Imagem URL   : https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcThkQy8KO1LlADlJAlA2gSprV2OlLB-xufBNSDvaGXXQADMNtK5csVRAJWoQdSe7XdRgMHYe-dfhg8TINIszteTYcIcGmBKUVaW0CcWt4LfMsGIjA4Wd8mvttkBPNrXXy5HuaRQ9nLE_FI&usqp=CAc
--------------------------------------------------------------------------------


...

```


## 🧑‍💻 Autor

Projeto desenvolvido por [Daniel Ayres] para fins de estudo e prática de automação RPA com Python,
focando em raspagem de dados (Web Scraping), manipulação de planilhas e processos automatizados de coleta de informações.
