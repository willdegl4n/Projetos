# Projeto Vendas Carros - ETL com Python
- [x] Criar os arquivos de Extração
- [x] Criar os dataframes e salvar como arquivos
- [ ] Manipular os DFs inserindo dados não existentes
- [ ] Manipular dados ja exitentes

### Foi criado um script para gerar de forma aleatoria, dados de vendas de veiculos para algumas UFs 
* gerardados.py
```
#%%
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

# %% Número de registros por cidade
num_registros = {
    "DF": random.randint(1500, 3500),
    "SP": random.randint(1500, 3500),
    "GO": random.randint(1500, 3500),
    "PR": random.randint(1500, 3500),
    "MA": random.randint(1500, 3500),
    "MG": random.randint(1500, 3500),
    "RJ": random.randint(1500, 3500),
    "MS": random.randint(1500, 3500),
}

# %% Gerar os dados para cada cidade
dados_uf = {}
for uf, qtd in num_registros.items():
    registros = []
    for _ in range(qtd):
        marca = random.choice(marcas)
        modelo = random.choice(modelos[marca])
        ano = random.choice(anos)
        cor = random.choice(cores)
        preco = round(random.uniform(30000, 200000), 2)  # Preço entre 30k e 200k
        
        registros.append([marca, modelo, ano, cor, preco])
    
    dados_uf[uf] = pd.DataFrame(registros, columns=["Marca", "Modelo", "Ano", "Cor", "Preço"])

# %% Criar e salvar o arquivo Excel
file_path = "vendas_carros_uf.xlsx"
with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
    for cidade, df in dados_uf.items():
        df.to_excel(writer, sheet_name=cidade, index=False)

file_path

```


### O gerardados.py resultou em uma planilha excel vendas_carros_uf.xlsx, com os dados de vendas para as UFs com os campos:
* Marca
* Modelo
* Ano
* CorPreço
  
![image](https://github.com/user-attachments/assets/1019d92b-65b8-4788-a4cc-a10c1034cab0)

### Com a planilha criada, constui um codico para buscar cada sheet da planilha e criar um arquivo parquet no diretorio 'ufs'
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

![image](https://github.com/user-attachments/assets/7f7e404d-7956-4866-b347-ad9aacb098b1)




contruindo...

