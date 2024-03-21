import pyodbc
from pyodbc import Error
import os

dados_conexao = (
  
    "Driver={SQL Server};"
    "server=DESKTOP-O755MAI\MSSQLSERVER1;"
    "database=CadastroClientes;"
)

vcon = pyodbc.connect(dados_conexao)

def query(conexao,sql):
     try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
     except Error as ex:
        print(ex)
     finally:
        print("Operaçãp realizada com sucesso")
        conexao.close()

def consultar(conexao,sql):
     c=conexao.cursor()
     c.execute(sql)
     res=c.fetchall()
     #conexao.close()
     return res

def menuPrincipal():
    os.system("cls")
    print("1 - inserir novo registro")
    print("2 - Deletar registro")
    print("3 - Atualizar registro")
    print("4 - Consultar registro por ID")
    print("5 - Consultar registro por nome")
    print("6 - Sair")

def menuInserir():
        os.system("cls")
        codigo = input("Digite o Codigo da venda:")
        nome = input("Digite o Nome:")
        produto = input("Digite o Produto;")
        venda = input("Digite a Data da venda:")
        preço = input("Digite o Preço:")
        quantidade = input("Digite a Quantidade:")
        vsql= "insert into Vendas (id_venda) (cliente) (produto) (data_venda) (preco) (quantidade) values ('"+codigo+"', '"+nome+"', '"+produto+"', '"+venda+"', '"+preço+"', '"+quantidade+"')"
        query(vcon,vsql)



def menuDeletar():
        print()

def menuAtualizar():
        print()

def menuConsultar():
        print()

def menuConsultarNomes():
        print()

opc=0
while opc !=6:
    menuPrincipal()
    opc=int(input("Digite uma opção"))
    if opc==1:
      menuInserir()
    elif opc ==2:
      menuDeletar()
    elif opc ==3:
        menuAtualizar()
    elif opc ==4: 
        menuConsultar()
    elif opc ==5: 
        menuConsultarNomes()
    elif opc==6: 
        os.system("cls")
        print("Programa finalizado")

    else:
        os.system("cls")
        print("opção invalida")
        os.system("Pause") 
        
    vcon.close()
    os.system("pause")