from services.request_service import RequestService
from requests.exceptions import HTTPError
from data.proposition_voting import PropositionVoting
from data.voting import Voting
from data.bench import Bench


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
        result = {}
        for year in self._propositions:
            for proposition in year:
                try:
                    response = self.request.get(self.url + self._ENDPOINT,
                                                {'ano': proposition.year,
                                                 'tipo': proposition.type,
                                                 'numero': proposition.number})
                    root = self.parser.fromstring(response.text)
                    number, proposition_vote = self.parse_proposition_voting(root)
                    result.update({number: proposition_vote})
                except HTTPError as error:
                    result.update({'Erro': 'Erro na requisição da votação de {}: {}'.format(proposition.name, error)})
        return result

    def parse_proposition_voting(self, element):
        initials = ''
        number = 0
        year = 0
        votings = []
        for child in element:
            if child.tag == 'Sigla':
                initials = child.text
            elif child.tag == 'Numero':
                number = child.text
            elif child.tag == 'Ano':
                year = child.text
            else:
                votings = self.parse_voting_list(child)
        return number, PropositionVoting(initials=initials, number=number, year=year, votings=votings)

    def parse_voting_list(self, element):
        vote_list = []
        bench_list = {}
        votings = []
        for voting in element:
            for child in voting:
                if child.tag == 'orientacaoBancada':
                    bench_list = self.parse_bench_list(child)
                else:
                    vote_list = self.paser_vote_list(child)
            votings.append(Voting(bench_orientation=bench_list, votes=vote_list))
        return votings

    @staticmethod
    def parse_bench_list(bench_orientation):
        bench_list = {}
        for orientation in bench_orientation:
            bench_list.update(
                {orientation.attrib.get('Sigla'): Bench(initials=orientation.attrib.get('Sigla'),
                                                        orientation=orientation.attrib.get('orientacao'))})
        return bench_list

    @staticmethod
    def paser_vote_list(vote_xml):
        vote_list = []
        for vote in vote_xml:
            vote_list.append(vote.attrib)
        return vote_list
