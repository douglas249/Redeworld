import psycopg


def conectar():
    return  psycopg.connect(
    host="localhost",
    port=5432,
    dbname="reworld",
    user="reworld_user",
    password="MinhaSenhaLocal_2026")

try:
    with conectar() as conexao:
        print("Conexão estabelecida com sucesso!")

except psycopg.Error as erro:
    print(f'Erro ao conectar: {erro}')




