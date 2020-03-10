from services.request_service import RequestService
from requests.exceptions import HTTPError
from data.proposition import Proposition
import xml
import datetime


class PropositionService(RequestService):

    def __init__(self, ano: int, tipo: str = ''):
        super().__init__()
        self._ENDPOINT = '/ListarProposicoesVotadasEmPlenario'
        self._ano = ano
        self._tipo = tipo
        self._processed_propositions = []

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano: int):
        self._ano = ano

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def processed_propositions(self):
        return self._processed_propositions

    def get_from_ws(self):
        result = []
        try:
            response = self.request.get(self.url + self._ENDPOINT, {'ano': self.ano, 'tipo': ''})
            root = self.parser.fromstring(response.text)

            for child in root:
                item = self.parse_proposition_list(child)
                if item is not None:
                    result.append(item)

        except HTTPError as http_error:
            print('Erro na Requisição: {}'.format(http_error))
        finally:
            return self.remove_duplicates(result)

    def parse_proposition_list(self, element):
        proposition_id = self.parse_id(element)
        if proposition_id not in self._processed_propositions:
            name, number, proposition_type, year = self.parse_from_name(element)
            dt_voting = self.parse_dt(element)
            self._processed_propositions.append(proposition_id)
            return Proposition(id=proposition_id, name=name, number=number, type=proposition_type, year=year,
                               dt_voting=dt_voting)

    @staticmethod
    def parse_from_name(element):
        for proposition_attr in element:
            if proposition_attr.tag == 'nomeProposicao':
                bar_index = proposition_attr.text.index('/')
                name = proposition_attr.text
                proposition_type = proposition_attr.text[0:proposition_attr.text.index(' ')]
                number = proposition_attr.text[3:bar_index]
                year = proposition_attr.text[bar_index + 1:bar_index + 5]

        return name, int(number), proposition_type, int(year)

    @staticmethod
    def parse_id(element):
        for proposition_attr in element:
            if proposition_attr.tag == 'codProposicao':
                return int(proposition_attr.text)

    @staticmethod
    def parse_dt(element):
        for proposition_attr in element:
            if proposition_attr.tag == 'dataVotacao':
                return datetime.datetime(int(proposition_attr.text[-4:]),
                                         int(proposition_attr.text[3:5]),
                                         int(proposition_attr.text[0:2]))

    @staticmethod
    def remove_duplicates(proposition_list: list):
        return set(proposition_list)
