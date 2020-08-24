class Congressman:

    def __init__(self, congressman_id: int, name: str, party: str, state: str):
        self._congressman_id = congressman_id
        self._name = name
        self._party = party
        self._state = state
        self._party_score = 0
        self._voting_times = 0
        self._score_percent = 0

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
    def party_score(self, party_score: float):
        self._party_score = party_score

    @property
    def voting_times(self):
        return self._voting_times

    @voting_times.setter
    def voting_times(self, voting_times: int):
        self._voting_times = voting_times

    @property
    def score_percent(self):
        return self._score_percent

    @score_percent.setter
    def score_percent(self, score_percent):
        self._score_percent = score_percent
