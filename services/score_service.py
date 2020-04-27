from data import *


class ScoreService:
    def __init__(self, votes_to_score: dict):
        self._votes_to_score = votes_to_score
        self._score = {}

    @property
    def votes_to_score(self):
        return self._votes_to_score

    def clean_data(self):
        for key in self._votes_to_score:
            item = self._votes_to_score.get(key)
            self.clean_votes(item.votings)

    def clean_votes(self, votes: list):
        for voting in votes:
            for item in voting.votes:
                self.strip_strings(item)
                self.calculate_score(item)

    def strip_strings(self, dict_to_clean: dict):
        for key in dict_to_clean:
            dict_to_clean[key] = dict_to_clean[key].strip()

    def calculate_score(self, item: dict):
        if item['ideCadastro'] in self._score:
            pass
        else:
            congressman = Congressman(congressman_id= item['ideCadastro'], name= item['Nome'], party= item['Partido'], state= item['UF'])
            self._score.update({item['ideCadastro']: congressman})