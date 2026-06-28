class Pesquisador:

    def __init__(
        self,
        pesquisadores_id=None,
        lattes_id=None,
        nome=None
    ):
        self.pesquisadores_id = pesquisadores_id
        self.lattes_id = lattes_id
        self.nome = nome

    def gerar_json(self):
        return {
            "pesquisadores_id": self.pesquisadores_id,
            "lattes_id": self.lattes_id,
            "nome": self.nome
        }