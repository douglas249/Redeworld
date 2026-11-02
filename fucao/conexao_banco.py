import psycopg
from rich import print


def conectar():

    return  psycopg.connect(
    host= "localhost",
    port=5432,
    dbname= "reworld",
    user= "reworld_user",
    password= "MinhaSenhaLocal_2026")


try:
    with conectar() as conexao:
        print('[green]CONEXÃO ESTABELECIDA COM SUCESSO![/]')

except:
    print('[red]ERRO AO ESTABELECER CONEXÃO[/]')



 
