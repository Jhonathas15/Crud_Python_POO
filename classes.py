from conexao import *

class Cliente:

    # Create -> Adicionar clientes ao banco
    def cadastrar_cliente(self, nome: str, email: str, senha: str) -> None:

        # Variavel com comando sql INSERT
        comando = f'INSERT INTO cliente (nome, email, senha) VALUES ("{nome}", "{email}", "{senha}")'
        # Executando comando
        cursor.execute(comando)
        conexao.commit()

        # Finalizando execução
        cursor.close()
        conexao.close()

    # Read -> Ver os clientes cadastrados
    def ver_clientes(self, campo:str='*')-> None:
        # Variavel com comando sql SELECT
        comando = f'SELECT {campo} FROM cliente'

        # Executando comando
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(resultado)

        # Finalizando execução
        cursor.close()
        conexao.close()

    #Update -> Editar um cliente do banco
    def atualizar_cliente(self, campo: str, valor: str, id: int)-> None:
        
        # Variavel com comando sql UPDATE
        comando = f'UPDATE cliente SET {campo} = "{valor}" WHERE id = {id}'

        # Executando comando
        cursor.execute(comando)
        conexao.commit()
        # Finalizando execução
        cursor.close()
        conexao.close()

    # Delete -> Deletando um cliente do banco
    def deletar_cliente(self,id:int)-> None:
        # Variavel com comando sql D    
        comando = f'DELETE FROM cliente WHERE id={id}'
        # Executando comando
        cursor.execute(comando)
        conexao.commit()

        # Finalizando execução
        cursor.close()
        conexao.close()

