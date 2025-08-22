# BPC – Análise de Judicialização, Cobertura e Prazos

O Benefício de Prestação Continuada (BPC) é um dos temas mais debatidos no âmbito da assistência social no Brasil. Voltado para pessoas idosas ou com deficiência em situação de vulnerabilidade, o BPC se diferencia de benefícios previdenciários como aposentadorias ou auxílios por incapacidade, pois não exige contribuição prévia do beneficiário. Essa característica, somada ao seu impacto social e orçamentário, o torna alvo frequente de debates políticos, ajustes fiscais e mudanças legislativas.

A concessão do BPC pode ocorrer de duas formas: **administrativa**, diretamente pelo INSS, ou **judicial**, quando o pedido inicial é negado e o requerente recorre à Justiça. A judicialização representa não apenas um aumento da demanda para o Judiciário, mas também uma oportunidade para escritórios e profissionais jurídicos identificarem regiões com maior potencial de atuação.

Compreender **quais regiões apresentam índices elevados de judicialização e como se comportam os indicadores de cobertura e prazos** permite tomadas de decisão mais estratégicas. Por exemplo:

  - No **BPC-Idoso**, que possui menos barreiras técnicas, regiões com alta judicialização e baixa cobertura podem sinalizar alto potencial de novas ações.

  - No **BPC-Deficiente**, que exige perícias e laudos mais complexos, indicadores como prazos médios e tipo de decisão ajudam a identificar áreas com maior necessidade de apoio jurídico especializado.

Este projeto aplica a **Arquitetura Medalhão (camadas bronze, silver e gold)** para organizar e analisar os dados do BPC, garantindo rastreabilidade e reprodutibilidade das análises. Com isso, indicadores estruturados e atualizados permitem monitorar a situação do benefício por unidade federativa e modalidade, ajudando gestores e advogados a agir de forma mais direcionada e eficaz.

---

# Objetivo do Projeto

- Monitorar concessões do BPC iniciadas a partir de 2024, concedidas entre janeiro e junho de 2025.
- Avaliar cobertura territorial, prazos e judicializações por tipo de benefício.
- Apoiar decisões estratégicas em advocacia previdenciária e gestão pública.
---
  
## 📂 Workspace (Notebooks / Código)
```
📂 bpc
│
├── 📂 raw
│   ├── 📄 conferindoCSVnopandas.py
│   ├── 📄 raw_bpc_raspagem.py
│   ├── 📄 raw_censo_raspagem.py
│   └── 📄 raw_uf_municipios_raspagem.py
│
├── 📂 bronze
│   ├── 📄 bronze_bpc_ingestao.py
│   ├── 📄 bronze_censo_ingestao.py
│   └── 📄 bronze_municipios_ibge_ingestao.py
│
├── 📂 silver
│   └── 🚧 (em construção)
│
└── 📂 gold
    └── 🚧 (em construção)

```
## 🗄️ Catálogo (Unity Catalog / Hive Metastore)
```
🏦 bpc
│
├── 🛢️ raw
│   └── 📂 source
│       ├── 📄 censo_2022.csv
│       ├── 📄 inss_2025_01.csv
│       ├── 📄 inss_2025_02.csv
│       ├── 📄 inss_2025_03.csv
│       ├── 📄 inss_2025_04.csv
│       ├── 📄 inss_2025_05.csv
│       ├── 📄 inss_2025_06.csv
│       ├── 📄 municipios_ibge.csv
│       ├── 📄 municipios_ibge2.csv
│       └── 📄 uf_municipios.csv
│
├── 🛢️ bronze
│   ├── 🗂️ tb_bronze_censo_2022
│   ├── 🗂️ tb_bronze_inss_bpc_2025_01a06
│   └── 🗂️ tb_bronze_municipios_ibge
│
├── 🛢️ silver
│   └── 🗂️ tb_silver_municipios_ibge
│
└── 🛢️ gold
    └── 🚧 (sem tabelas ainda)

```
### Esquema visual
```
📂 → diretório de notebooks (workspace)
📄 → notebook/arquivo Python
🛢️ → schema dentro do catálogo
🗂️ → tabela Delta
📄 (no catálogo/raw) → CSV bruto
```
---
## Fonte de Dados

Os dados utilizados no projeto foram extraídos de três principais fontes púplicas:

- **INSS**: Dados de concessões do BPC por mês, disponível em csv.
 [Fonte: INSS - Dados Abertos](https://dadosabertos.inss.gov.br/dataset/beneficios-concedidos-plano-de-dados-abertos-jun-2023-a-jun-2025)
  - Quantidade de arquivos: 6 cvs - Concessões de jan/25 a jun/25

- **IBGE (Censo 2022)**: População total por município, utilizada para cálculo de cobertura e identificação do público-alvo.  
  [Fonte: Censo IBGE 2022](https://www.ibge.gov.br/estatisticas/sociais/trabalho/22827-censo-demografico-2022.html?=&t=downloads/)
  - Quantidade de arquivos: 1 csv

- **Municípios/UF/Região**: Dados de referência com códigos de municípios, sigla UF e região geográfica.  
  [Fonte: IBGE – Tabela de Referência Territorial](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html/)
  - Quantidade de arquivos: 1 csv
    
<img width="407" height="366" alt="image" src="https://github.com/user-attachments/assets/defab5e6-5e6f-4fc5-a4ad-f29b34cfa0f8" />

---
https://github.com/fdg-fer/bpc-pipeline-databricks/tree/main
