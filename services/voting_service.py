from services.request_service import RequestService
from requests.exceptions import HTTPError


class VotingService(RequestService):

    def __init__(self, propositions: list):
        super().__init__()
        self._ENDPOINT = '/ObterVotacaoProposicao'
        self._propositions = propositions

    @property
    def propositions(self):
        return self._propositions

    @propositions.setter
    def propositions(self, propositions: list):
        self._propositions = propositions

    def get_from_ws(self):
        result = []
        for year in self._propositions:
            for proposition in year:
                try:
                    response = self.request.get(self.url + self._ENDPOINT,
                                                {'ano': proposition.year,
                                                 'tipo': proposition.type,
                                                 'numero': proposition.number})
                    result.append(response.status_code)
                except HTTPError as error:
                    result.append('Erro na requisição da votação de {}: {}'.format(proposition.name, error))
        return result

    def parse_voting_list(self):
        return

    def parse_bench_list(self):
        return

    def parse_congressman_list(self):
        return

    def calculate_scores(self):
        party_score, government_score = 0
        return party_score, government_score
