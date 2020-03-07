import datetime


class Proposicao:

    def __init__(self, codigo: int, nome: str, tipo: str, numero: int, ano: int, dt_votacao: datetime.date):
        self._codigo = codigo
        self._nome = nome
        self._tipo = tipo
        self._numero = numero
        self._ano = ano
        self._dt_votacao = dt_votacao

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self._codigo = codigo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self._tipo = tipo

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero: int):
        self._numero = numero

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano: int):
        self._ano = ano

    @property
    def dt_votacao(self):
        return self._dt_votacao

    @dt_votacao.setter
    def dt_votacao(self, dt_votacao: datetime.date):
        self._dt_votacao = dt_votacao
