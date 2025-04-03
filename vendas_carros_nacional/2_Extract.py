#%% importando as bibliotecas
import pandas as pd
import glob  # Para buscar arquivos no diretório

#%% Buscar todos os arquivos .xlsx no diretório atual
arquivos_excel = glob.glob("vendas_*.xlsx")

arquivos_excel
#%% Processar cada arquivo Excel
for arquivo in arquivos_excel:
    # Extrai o nome da UF do arquivo (ex: "vendas_SP.xlsx" -> "SP")
    uf = arquivo.replace("vendas_", "").replace(".xlsx", "")

    # Lê o arquivo Excel e carrega o DataFrame
    df = pd.read_excel(arquivo, engine="openpyxl")

    # Salva o DataFrame em um arquivo Parquet com o nome da UF
    df.to_parquet(f"{uf}.parquet", index=False)

    print(f"Arquivo '{uf}.parquet' gerado com sucesso!")

print("Todos os arquivos .parquet foram gerados!")

