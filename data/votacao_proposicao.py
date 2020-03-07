# Conter:
#     sigla
#     numero
#     ano
#     votacoes -> List<Votacao>


class VotacaoProposicao:

    def __init__(self, sigla: str, numero: int, ano: int, votacoes: list):
        self._sigla = sigla
        self._numero = numero
        self._ano = ano
        self._votacoes = votacoes

    @property
    def sigla(self):
        return self._sigla

    @sigla.setter
    def sigla(self, sigla):
        self._sigla = sigla

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        self._ano = ano

    @property
    def votacoes(self):
        return self._votacoes

    @votacoes.setter
    def votacoes(self, votacoes):
        self._votacoes = votacoes
