import requests
from requests.exceptions import HTTPError


class RequestService:
    URL = 'https://www.camara.leg.br/SitCamaraWS/Proposicoes.asmx'

    def __init__(self):
        try:
            initial_response = requests.get(self.URL)
            initial_response.raise_for_status()
        except HTTPError as http_error:
            print('Ocorreu um erro na conexão com o webservice da câmara: {}'.format(http_error))
        return
