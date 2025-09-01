# 📊 Projeto de Engenharia de Dados - Campeonato Brasileiro 2025

## 🎯 Objetivo
Este projeto tem como objetivo criar um **pipeline de engenharia de dados em Databricks (Free Edition)** utilizando a **arquitetura medalhão (bronze, silver, gold)** para análise dos dados do **Campeonato Brasileiro Série A 2025**.

Com ele será possível:
- Coletar dados do Brasileirão por meio de **raspagem pública de sites** (ge.globo).  
- Armazenar os dados em camadas organizadas (raw/bronze/silver/gold).  
- Tratar, padronizar e enriquecer as informações.  
- Criar **KPIs e métricas** como classificação, artilharia e estatísticas de partidas.  
- Disponibilizar dados prontos para análise em **dashboards (Databricks/Power BI)**.

> ⚠️ Diferente de APIs privadas, este projeto **não exige autenticação** e utiliza **dados públicos**.

---

## 🏗️ Arquitetura

```bash
📂 brasileirao2025
│
├── 📂 raw        # Dados brutos extraídos via scraping do ge.globo
├── 📂 bronze     # Dados ingeridos no Databricks (sem transformação complexa)
├── 📂 silver     # Dados tratados e padronizados
├── 📂 gold       # Dados prontos para análise/KPIs
│
├── 📄 1_bronze_raspagem.py   # Notebook: coleta de dados do ge.globo e gravação em raw/bronze
├── 📄 2_silver_tratamento.py # Notebook: tratamento e normalização dos dados
├── 📄 3_gold_analise.py      # Notebook: criação de KPIs e análises
└── 📄 README.md              # Documentação do projeto
```

---

## ⚙️ Ferramentas Utilizadas
- **Databricks Free Edition**
- **Python (PySpark + requests + BeautifulSoup + pandas)**
- **Scraping público** → [ge.globo.com](https://ge.globo.com/futebol/brasileirao-serie-a/)
- **Formato de armazenamento:** CSV / Delta Tables
- **Visualização:** Databricks SQL / Power BI (opcional)

---

## 🔄 Etapas do Pipeline

### 1. Ingestão (Bronze)
- Raspagem pública dos dados da **rodada atual do Brasileirão 2025** no ge.globo: partidas, times, placar, data, estádio.  
- Salvar dados brutos em formato **CSV/JSON** em `/mnt/brasileirao/raw`.  
- Criar tabela `tb_partidas_bronze`.

### 2. Transformação (Silver)
- Padronizar datas, nomes de times e placares.  
- Tratar valores nulos e inconsistências.  
- Normalizar tabelas relacionais:  
  - `tb_partidas_silver`  
  - `tb_classificacao_silver`  

### 3. Enriquecimento e KPIs (Gold)
- Criar métricas principais:  
  - Classificação por pontos, vitórias, empates, derrotas.  
  - Aproveitamento (%) por time.  
  - Artilharia (se disponível nos dados).  
  - Desempenho como mandante/visitante.  
- Salvar em tabelas otimizadas:  
  - `tb_classificacao_gold`  
  - `tb_artilharia_gold`  
  - `tb_estatisticas_gold`  

### 4. Visualização
- Criar dashboards no **Databricks SQL** ou integrar com **Power BI**:  
  - Tabela de classificação em tempo real.  
  - Evolução rodada a rodada.  
  - Top 10 artilheiros.

---

## 🚀 Como Executar

1. Criar conta no [Databricks Free Edition](https://community.cloud.databricks.com/).  
2. Instalar bibliotecas Python necessárias (`requests`, `BeautifulSoup4`, `pandas`, `pyspark`).  
3. Criar diretórios no DBFS:
   ```python
   dbutils.fs.mkdirs("/mnt/brasileirao/raw")
   dbutils.fs.mkdirs("/mnt/brasileirao/bronze")
   dbutils.fs.mkdirs("/mnt/brasileirao/silver")
   dbutils.fs.mkdirs("/mnt/brasileirao/gold")
   ```
4. Executar os notebooks na ordem:
   - `1_bronze_raspagem.py`
   - `2_silver_tratamento.py`
   - `3_gold_analise.py`

---

## 📈 Exemplos de KPIs
- **Classificação atualizada**: tabela por pontos.  
- **Média de gols por partida**.  
- **Top artilheiros**.  
- **Time com melhor ataque/defesa**.  
- **Aproveitamento em casa e fora**.

---

## 🧑‍💻 Autor
**Willdeglan S. S.**  
Data Engineer & DBA | Criador do **SQL Dicas**  
[LinkedIn - @sqldicas](https://www.linkedin.com/in/sqldicas)

---
