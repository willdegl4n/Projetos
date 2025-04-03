#%% teste de gravação de parquet
import pandas as pd

# Carrega o arquivo Excel
xls = pd.ExcelFile("vendas_carros_uf.xlsx", engine="openpyxl")

# Percorre todas as abas e salva cada uma como um arquivo Parquet
for sheet in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet, engine="openpyxl")
    df.to_parquet(f"ufs/{sheet}.parquet", index=False)

print("Arquivos Parquet gerados com sucesso!")