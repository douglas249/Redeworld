from fucao import conexao_banco
from fucao import funcionalidades
from fucao import listaderepeticao



valor_total = funcionalidades()

equipamento, quantidade_equipamento, area, caixas = listaderepeticao()

lista = [equipamento, quantidade_equipamento, area, caixas,
         valor_total]

class BancoDeDados():
    def __init__ (self):
        self.banco = conexao_banco()


        def criar_banco(self):
            with self.banco.cursor as criar:
                criar.execute("""

            CREATE TABLE salvo(
            equipamento VARCHAR(20),
            quantidade_equipamento  INTEGER,
            area NUMERIC, 
            caixas INTEGER, 
            valor_total INTEGER
            )
"""       )  

                self.banco.commit()

        def salvar_dados(self, lista):
            with self.banco.cursor as criar:
                criar.executemany( """
                INSERT INTO salvo(equipamento,quantidade_equipamento
                                ,area,caixas,valor_total) VALUES (%s,%s,%s,%s,%s,%s)

""", lista

        )   
                self.banco.commit()


        def ver_projetos(self):
            with self.banco.cursor as criar:
                criar.execute("SELCT * FROM salvo")
                resultado = self.banco.fetchall()

                return resultado


        def fechar_banco(self):
            self.banco.closer()

        
              




        





