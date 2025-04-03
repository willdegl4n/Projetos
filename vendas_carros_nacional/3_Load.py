#%% importando as bibliotecas
import pandas as pd
import glob  # Para buscar arquivos no diretório

#%% Buscar todos os arquivos .parquet no diretório atual
arquivos_parquet = glob.glob("*.parquet")

arquivos_parquet

#%% Dicionário para armazenar os DataFrames
dataframes = {}

#%% Carregar cada arquivo .parquet em um DataFrame
for arquivo in arquivos_parquet:
    # Extrai o nome da UF do arquivo (ex: "SP.parquet" -> "SP")
    uf = arquivo.replace(".parquet", "")

    # Lê o arquivo Parquet e armazena no dicionário
    dataframes[uf] = pd.read_parquet(arquivo)

    print(f"Arquivo '{arquivo}' carregado para DataFrame com sucesso!")

print("Todos os arquivos .parquet foram carregados!")

#%% acessando os dataframes
sp = dataframes["SP"]  # DataFrame de São Paulo
sp
#%%
rj = dataframes["RJ"]  # DataFrame do Rio de Janeiro
rj
