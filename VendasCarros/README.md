# Projeto Vendas Carros - ETL com Python
### Foi criado um script para gerar de forma aleatoria, dados de vendas de veiculos para algumas UFs 
* gerardados.py

### O gerardados.py resultou em uma planilha excel vendas_carros_uf.xlsx, com os dados de vendas para as UFs com os campos:
* Marca
* Modelo
* Ano
* CorPreço

### com a planilha criada, constui um codico para buscar cada sheet da planilha e criar um arquivo parquet no diretorio 'ufs'
* CriandoDataframes.py

```
#%% Criando os arquivos parquet de acordo com cada sheet da planilha vendas_carros_uf.xlsx
import pandas as pd

# Carrega o arquivo Excel
xls = pd.ExcelFile("vendas_carros_uf.xlsx", engine="openpyxl")

# Percorre todas as abas e salva cada uma como um arquivo Parquet
for sheet in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet, engine="openpyxl")
    df.to_parquet(f"ufs/{sheet}.parquet", index=False)

print("Arquivos Parquet gerados com sucesso!")
```

contruindo...

