# Criando um ELT com dados fictício  


🎯 **_1_gerardados.py_** - O que esse código faz?
- Gera dados para todas os 26 Estados brasileiros mais o Distrito Federal.
- Cria um arquivo Excel separado para cada UF (ex: vendas_SP.xlsx, vendas_RJ.xlsx).
- Cada arquivo tem apenas uma sheet (inicialmente eu pensei em um arwuivo .CSV ou .JSON), com os dados da respectiva UF.
- O número de registros varia aleatoriamente entre 15.000 e 35.000 por UF, trazendo uma ideia mais real.

![image](https://github.com/user-attachments/assets/971d0209-9a5b-45a6-9dd7-3f32020effa9)


🎯 **_2_Extract.py_** - O que esse código faz?
- Lista todos os arquivos Excel (vendas_*.xlsx) no diretório atual.
- Extrai a sigla da UF do nome do arquivo.
- Lê os arquivos Excel.
- Salva o DataFrame em formato .parquet, mantendo o nome da UF.

![image](https://github.com/user-attachments/assets/a92ab8fe-b012-4119-a0f9-82ba6e2ed954)


🎯 **_3_Load.py_** - O que esse código faz?
- Lista todos os arquivos .parquet no diretório atual.
- Cria um dicionário ufs_completos para mapear a sigla do estado para o nome completo.
- Lê cada arquivo .parquet, adiciona a coluna "UF" com o nome completo do estado.
- Armazena o DataFrame no dicionário dataframes, usando a sigla da UF como chave.
- Exibe uma mensagem de sucesso para cada arquivo carregado.

![image](https://github.com/user-attachments/assets/74209755-3a36-46bd-8544-f34c8ac6d2ac)


~~~
# Acessando o dataframe do estado do Maranhão

ma = dataframes["MA"]  
ma
~~~

![image](https://github.com/user-attachments/assets/fd8986f7-1741-4331-97d0-0d8dd3c9b0ba)

