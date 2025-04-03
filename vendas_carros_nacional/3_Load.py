#%% importando as bibliotecas
import pandas as pd
import glob  # Para buscar arquivos no diretório

#%% Buscar todos os arquivos .parquet no diretório atual
arquivos_parquet = glob.glob("*.parquet")

arquivos_parquet

#%% Dicionário para armazenar os DataFrames
dataframes = {}

#%% Mapeamento de siglas para nomes completos dos estados
ufs_completos = {
    "AC": "Acre", "AL": "Alagoas", "AM": "Amazonas", "AP": "Amapá", "BA": "Bahia",
    "CE": "Ceará", "DF": "Distrito Federal", "ES": "Espírito Santo", "GO": "Goiás",
    "MA": "Maranhão", "MG": "Minas Gerais", "MS": "Mato Grosso do Sul", "MT": "Mato Grosso",
    "PA": "Pará", "PB": "Paraíba", "PE": "Pernambuco", "PI": "Piauí", "PR": "Paraná",
    "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte", "RO": "Rondônia", "RR": "Roraima",
    "RS": "Rio Grande do Sul", "SC": "Santa Catarina", "SE": "Sergipe", "SP": "São Paulo",
    "TO": "Tocantins"
}

#%% Carregar cada arquivo .parquet em um DataFrame
for arquivo in arquivos_parquet:
    # Extrai o nome da UF do arquivo (ex: "SP.parquet" -> "SP")
    uf = arquivo.replace(".parquet", "")
 
    # Lê o arquivo Parquet e adiciona a coluna "UF"
    df = pd.read_parquet(arquivo)
    df["UF"] = ufs_completos.get(uf, uf)  # Usa o nome completo ou mantém a sigla
    
    # Armazena no dicionário
    dataframes[uf] = df

    print(f"Arquivo '{arquivo}' carregado com sucesso!")

print()
print("Os arquivos .parquet foram carregados e estão prontos para ser manipulados!")

