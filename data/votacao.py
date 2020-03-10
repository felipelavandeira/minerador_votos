class Votacao:

    def __init__(self, orientacoes_bancada: dict, votos: dict):
        self._orientacoes_bancada = orientacoes_bancada
        self._votos = votos

    @property
    def orientacoes_bancada(self):
        return self._orientacoes_bancada

    @orientacoes_bancada.setter
    def orientacoes_bancada(self, orientacoes_bancada):
        self._orientacoes_bancada = orientacoes_bancada

    @property
    def votos(self):
        return self._votos

    @votos.setter
    def votos(self, votos):
        self._votos = votos
