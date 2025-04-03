#%% importando as bibliotecas
import pandas as pd
import random

# %% Definição de dados fictícios
marcas = ["Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen", "Hyundai", "Nissan", "Fiat", "Jeep", "Renault"]
modelos = {
    "Toyota": ["Corolla", "Hilux", "Yaris", "Etios"],
    "Honda": ["Civic", "HR-V", "Fit", "City"],
    "Ford": ["Ka", "EcoSport", "Ranger", "Fusion"],
    "Chevrolet": ["Onix", "Prisma", "Cruze", "Tracker"],
    "Volkswagen": ["Golf", "Polo", "T-Cross", "Virtus"],
    "Hyundai": ["HB20", "Creta", "Tucson", "Santa Fe"],
    "Nissan": ["Versa", "Kicks", "Sentra", "Frontier"],
    "Fiat": ["Argo", "Mobi", "Toro", "Cronos"],
    "Jeep": ["Renegade", "Compass", "Wrangler", "Cherokee"],
    "Renault": ["Kwid", "Duster", "Sandero", "Captur"],
}
cores = ["Branco", "Preto", "Prata", "Vermelho", "Azul", "Cinza", "Verde"]
anos = list(range(2015, 2024))

# %% Todas as 27 UFs do Brasil
ufs_brasil = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT",
    "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"
]

# %% Gerar e salvar os arquivos Excel separadamente
for uf in ufs_brasil:
    qtd = random.randint(15000, 35000)  # Número aleatório de registros por UF
    registros = []
    
    for _ in range(qtd):
        marca = random.choice(marcas)
        modelo = random.choice(modelos[marca])
        ano = random.choice(anos)
        cor = random.choice(cores)
        preco = round(random.uniform(30000, 200000), 2)  # Preço entre 30k e 200k
        
        registros.append([marca, modelo, ano, cor, preco])
    
    df = pd.DataFrame(registros, columns=["Marca", "Modelo", "Ano", "Cor", "Preco"])
    
    # Criando um arquivo Excel para cada UF
    file_path = f"vendas_{uf}.xlsx"
    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name=uf, index=False)
    
    print(f"Arquivo '{file_path}' gerado com sucesso!")

