import psycopg2

def criar_conexao():
   try:
       conn = psycopg2.connect(
           dbname='Clinica',

           user='postgres',

           password='pp1234',

           host='localhost',

           port='5432',
        )
       
       return conn
   
   except Exception as exc:

       print(f"Erro ao conectar com o banco de dados: {exc}")
       return None