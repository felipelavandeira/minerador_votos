class Bancada:

    def __init__(self, sigla: str, orientacao: str):
        self._sigla = sigla
        self._orientacao = orientacao

    @property
    def sigla(self):
        return self._sigla

    @sigla.setter
    def sigla(self, sigla: str):
        self._sigla = sigla

    @property
    def orientacao(self):
        return self._orientacao

    @orientacao.setter
    def orientacao(self, orientacao: str):
        self._orientacao = orientacao
