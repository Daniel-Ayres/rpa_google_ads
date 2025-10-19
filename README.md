# 🛒 RPA Google Shopping Ads

Este projeto é uma automação RPA desenvolvida em Python que realiza pesquisas no Google Shopping, coleta automaticamente informações sobre produtos (título, preço, loja, link e imagem), salva os dados em uma planilha Excel e baixa as imagens localmente.
Todo o processo é registrado por logs, garantindo rastreabilidade da execução.

---

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
RPA_GOOGLE_ADS/
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
git clone https://github.com/Daniel-Ayres/rpa_google_shopping.git
cd rpa_google_shopping
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
| **requests** | Responsável por realizar as requisições HTTP para consumir a API pública do Chuck Norris. |
| **pandas** | Utilizada para manipulação e estruturação dos dados, além de facilitar a exportação para o formato Excel. |
| **openpyxl** | Engine utilizada pelo `pandas` para salvar os dados em arquivos `.xlsx`. |
| **logging** | Gerencia o registro de logs, permitindo rastrear cada etapa da execução da automação. |
| **os** | Manipula diretórios e caminhos de arquivos, criando automaticamente as pastas `data/` e `logs/`. |


## ❓ Por que essas bibliotecas?

- **🛰️ requests** — Simples e robusta para consumir **APIs RESTful**, amplamente utilizada pela comunidade Python.
  
- **📊 pandas** — Facilita a **manipulação e estruturação de dados** em formato tabular, permitindo salvar facilmente em planilhas Excel.
   
- **📘 openpyxl** — É a **engine recomendada pelo pandas** para leitura e escrita de arquivos `.xlsx` (Excel).
  
- **🧾 logging** — Permite **rastrear toda a execução da automação**, registrando informações e erros com diferentes níveis de log (`INFO`, `ERROR`, etc.).
   
- **📁 os** — Possibilita a **criação automática de diretórios**, como `data/` e `logs/`, tornando a automação independente do ambiente.  


## 🧪 Exemplo de Saída no Terminal

```bash
Buscando categorias disponíveis...
Coletando uma piada por categoria...
Salvando piadas no Excel...

Piadas por categoria:
--------------------------------------------------------------------------------
Categoria: dev
ID       : a1whrz_crhgykfuah1mrmw
URL      : https://api.chucknorris.io/jokes/a1whrz_crhgykfuah1mrmw
Piada    : Chuck Norris's programs can pass the Turing Test by staring at the interrogator.
--------------------------------------------------------------------------------
Categoria: food
ID       : 4uqhu_nmtncleixytkl0pq
URL      : https://api.chucknorris.io/jokes/4uqhu_nmtncleixytkl0pq
Piada    : Chuck Norris proceeded to eat the chips, the bag, and the man in one deft move.
--------------------------------------------------------------------------------
```


## 🧑‍💻 Autor

Projeto desenvolvido por [Daniel Ayres] para fins de estudo e prática de automação RPA com Python e consumo de APIs REST.