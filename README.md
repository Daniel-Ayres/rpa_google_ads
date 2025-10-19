# 🛒 RPA Google Shopping Ads

Este projeto é uma automação RPA desenvolvida em Python que realiza pesquisas no Google Shopping, coleta automaticamente informações sobre produtos (título, preço, loja, link e imagem), salva os dados em uma planilha Excel e baixa as imagens localmente.
Todo o processo é registrado por logs, garantindo rastreabilidade da execução.

⚙️ Observação: no momento, o script está fixo para realizar pesquisas sobre “Geladeira” em geral, mas pode ser facilmente adaptado para outros produtos modificando o parâmetro termo_pesquisa no arquivo main.py.

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
├── logs/                     # Contém os arquivos de log da execução
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

Buscando produtos de: Geladeira

Produtos ordenados do mais barato para o mais caro:
--------------------------------------------------------------------------------

#01

Título   : Geladeira Refrigerador HQ Defrost 230 Litros Cinza HQ-230RDF (127V)
Preço    : R$ 1.659,98
Loja     : Amazon.com.br
URL Loja     : https://www.amazon.com.br/Geladeira-Refrigerador-HQ-Defrost-HQ-230RDF/dp/B0DVDFMXX8?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A3LGV2SX75WN63
Imagem URL   : https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcQNkba1LM3fx3_YrZaUhjn0XCzDg-SwWkP0x5neyxVPe7iC8vDMUiSEgS6H7eAUhXQSkmaWBiRGxHsol2ZGZZNbu6l9NbG4znhxjoQS7D_OBkdERTJmFfpwif8Bcudd3o4x9_VH4aM&usqp=CAc
--------------------------------------------------------------------------------

#02

Título   : Refrigerador 240L 1 Porta Classe A 110 Volts, Branco, Electrolux
Preço    : R$ 1.733,99
Loja     : Amazon.com.br
URL Loja     : https://www.amazon.com.br/Refrigerador-Degelo-Pr%C3%A1tico-Defrost-Electrolux/dp/B076BDR1P7?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A3LGV2SX75WN63
Imagem URL   : https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcTNJMSo4WKXvV9GjOtPsvSzJ6yWCvFOvIeGEqnrggR7T_nM_35PejPedbg5jhUMH1uQMUw5RLMp2bVNLJpIEwWpcVl4B_Lo4JDhBxiwm1N49bu-Y14H2z0aNbBEgJhcaiNhbv5mLKbl&usqp=CAc
--------------------------------------------------------------------------------

...

```


## 🧑‍💻 Autor

Projeto desenvolvido por [Daniel Ayres] para fins de estudo e prática de automação RPA com Python e consumo de APIs REST.
