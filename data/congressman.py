# Conter:
#     dados do deputado:
#         id
#         nome
#         partido
#         uf
#     score_pro_partido
#     score_pro_governo


class Congressman:

    def __init__(self, congressman_id: int, name: str, party: str, state: str):
        self._congressman_id = congressman_id
        self._name = name
        self._party = party
        self._state = state
        self._party_score = 0
        self._government_score = 0

    @property
    def congressman_id(self):
        return self._congressman_id

    @congressman_id.setter
    def congressman_id(self, congressman_id: str):
        self._congressman_id = congressman_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def party(self):
        return self._party

    @party.setter
    def party(self, party: str):
        self._party = party

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: str):
        self._state = state

    @property
    def party_score(self):
        return self._party_score

    @party_score.setter
    def party_score(self, party_score: int):
        self._party_score = party_score

    @property
    def government_score(self):
        return self._government_score

    @government_score.setter
    def government_score(self, government_score: int):
        self._government_score = government_score
