from fucao.conexao_banco import conectar


class BancoDeDados:
    def __init__(self):
        self.banco = conectar()

    def criar_banco(self):
        with self.banco.cursor() as criar:
            criar.execute(
                """
                CREATE TABLE IF NOT EXISTS salvo(
                    equipamento VARCHAR(20),
                    quantidade_equipamento INTEGER,
                    area NUMERIC,
                    caixas INTEGER,
                    valor_total INTEGER
                )
                """
            )
        self.banco.commit()
        return self

    def salvar_dados(self, lista):
        if not lista:
            return 0

        with self.banco.cursor() as criar:
            criar.execute(
                """
                INSERT INTO salvo (
                    equipamento,
                    quantidade_equipamento,
                    area,
                    caixas,
                    valor_total
                )VALUES (
                        %(equipamento)s,
                        %(quantidade_equipamento)s,
                        %(area)s,
                        %(caixas)s,
                        %(valor_total)s
)
                """,
                lista,
            )
        self.banco.commit()
        return len(lista)

    def ver_projetos(self):
        with self.banco.cursor() as criar:
            criar.execute("SELECT * FROM salvo")
            return criar.fetchall()

    def fechar_banco(self):
        if self.banco is not None:
            self.banco.close()
        return None

        
              




        





