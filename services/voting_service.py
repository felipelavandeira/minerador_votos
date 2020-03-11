from services.request_service import RequestService
from requests.exceptions import HTTPError


class VotingService(RequestService):

    def __init__(self, tipo: str, numero: int, ano: int):
        super().__init__()
        self._ENDPOINT = '/ObterVotacaoProposicao'
        self._tipo = tipo
        self._numero = numero
        self._ano = ano

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

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
