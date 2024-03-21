import pyodbc

dados_conexao = (
  
    "Driver={SQL Server};"
    "server=DESKTOP-O755MAI\MSSQLSERVER1;"
    "database=CadastroClientes;"
)
## conexão com SQL

vcon = pyodbc.connect(dados_conexao)
print('conexão bem sucedida')

## conexão com SQL

cursor = vcon.cursor()
id = 3
cliente = 'sofia'
produto = 'blusa cinza'
data = '21/03/2024'
preco = 80
quantidade = 1

comando = f"""insert into Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
values
({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""


cursor.execute(comando) # executa uma ação
cursor.commit() # somente usado caso uma informação seja adicionada/alterada