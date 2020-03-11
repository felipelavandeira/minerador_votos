from abc import abstractmethod
from requests.exceptions import HTTPError
from xml.etree import ElementTree
import requests


class RequestService:

    def __init__(self):
        self._URL = 'https://www.camara.leg.br/SitCamaraWS/Proposicoes.asmx'
        self._parser = ElementTree
        self._request = requests
        try:
            response = self._request.get(self._URL)
            response.raise_for_status()
        except HTTPError as http_error:
            print('Ocorreu um erro na conexão com o webservice da câmara: {}'.format(http_error))
        return

    @property
    def url(self):
        return self._URL

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, request):
        self._request = request

    @property
    def parser(self):
        return self._parser

    @abstractmethod
    def get_from_ws(self):
        pass
