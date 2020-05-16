from data import *


class ScoreService:
    def __init__(self, votes_to_score: dict):
        self._votes_to_score = votes_to_score
        self._score = {}

    @property
    def votes_to_score(self):
        return self._votes_to_score

    def calculate(self):
        for key in self._votes_to_score:
            item = self._votes_to_score.get(key)
            self.clean_votes(item.votings)
        return self._score

    def clean_votes(self, votes: list):
        for voting in votes:
            orientation = voting.bench_orientation
            for item in voting.votes:
                self.strip_strings(item)
                self.calculate_score(item, orientation)

    def strip_strings(self, dict_to_clean: dict):
        for key in dict_to_clean:
            dict_to_clean[key] = dict_to_clean[key].strip()

    def calculate_score(self, item: dict, orientation: dict):
        benchOrientation = self.findOrientation(item, orientation)
        if item['ideCadastro'] in self._score:
            self.incrementVotingTimes(self._score.get(item['ideCadastro']))
            self.incrementScore(item, benchOrientation)
        else:
            congressman = Congressman(congressman_id=item['ideCadastro'], name=item['Nome'],
                                      party=item['Partido'], state=item['UF'])
            self.incrementVotingTimes(congressman)
            self._score.update({item['ideCadastro']: congressman})
            self.incrementScore(item, benchOrientation)

    def findOrientation(self, item: dict, orientation: dict):
        orientation = self.separateOrientation(orientation)
        for bench in orientation:
            partido = item['Partido'].lower()
            if partido == bench.lower() or 'repr.{}'.format(partido) == bench.lower():
                return orientation.get(bench)

    def separateOrientation(self, orientation: dict):
        keys = list(orientation.keys())
        for key in keys:
            if key.count('P') >= 2 and key.startswith('PP') is not True:
                benchOrientation = orientation.get(key)
                self.composeOrientations(key.split('P'), orientation, benchOrientation)
                orientation.pop(key)
        return orientation

    def incrementScore(self, congressman: dict, benchOrientation: Bench):
        if benchOrientation is None:
            return

        if congressman['Voto'] == benchOrientation.orientation:
            congressmanToScore = self._score.get(congressman['ideCadastro'])
            congressmanToScore.party_score = congressmanToScore.party_score + 1

    @staticmethod
    def incrementVotingTimes(congressman):
        congressman.voting_times = congressman.voting_times + 1

    @staticmethod
    def composeOrientations(keys: list, orientation: dict, bench: Bench):
        for key in keys:
            orientation.update({'P' + key: Bench(initials=bench.initials, orientation=bench.orientation)})