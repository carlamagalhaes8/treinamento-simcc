class Producao:

    def __init__(
        self,
        producoes_id=None,
        pesquisadores_id=None,
        issn=None,
        nomeartigo=None,
        anoartigo=None
    ):
        self.producoes_id = producoes_id
        self.pesquisadores_id = pesquisadores_id
        self.issn = issn
        self.nomeartigo = nomeartigo
        self.anoartigo = anoartigo

    def gerar_json(self):
        return {
            "producoes_id": self.producoes_id,
            "pesquisadores_id": self.pesquisadores_id,
            "issn": self.issn,
            "nomeartigo": self.nomeartigo,
            "anoartigo": self.anoartigo
        }