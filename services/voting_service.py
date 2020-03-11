from services.request_service import RequestService
from requests.exceptions import HTTPError


class VotingService(RequestService):

    def __init__(self, voting_type: str, number: int, year: int):
        super().__init__()
        self._ENDPOINT = '/ObterVotacaoProposicao'
        self._voting_type = voting_type
        self._number = number
        self._year = year

    @property
    def voting_type(self):
        return self._voting_type

    @voting_type.setter
    def voting_type(self, voting_type):
        self._voting_type = voting_type

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year
