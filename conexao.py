import mysql.connector

# conectando com o banco 
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='banco'
)

# variavel para executar meus comandos
cursor = conexao.cursor()
