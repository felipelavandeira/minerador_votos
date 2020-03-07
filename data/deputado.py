# Conter:
#     dados do deputado:
#         id
#         nome
#         partido
#         uf
#     score_pro_partido
#     score_pro_governo


class Deputado:

    def __init__(self, id: int, nome: str, partido: str, uf: str):
        self._id = id
        self._nome = nome
        self._partido = partido
        self._uf = uf
        self._score_partido = 0
        self._score_governo = 0

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: str):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def partido(self):
        return self._partido

    @partido.setter
    def partido(self, partido: str):
        self._partido = partido

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, uf: str):
        self._uf = uf

    @property
    def score_partido(self):
        return self._score_partido

    @score_partido.setter
    def score_partido(self, score_partido: int):
        self._score_partido = score_partido

    @property
    def score_governo(self):
        return self._score_governo

    @score_governo.setter
    def score_governo(self, score_governo: int):
        self._score_governo = score_governo
