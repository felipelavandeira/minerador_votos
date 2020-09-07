from data import *
import csv


class ScoreService:
    def __init__(self, votes_to_score: dict, init_year: int, end_year: int):
        self._votes_to_score = votes_to_score
        self._score = {}
        self._init_year = init_year
        self._end_year = end_year
        self._spectrum = self.build_spectrum()

    @property
    def votes_to_score(self):
        return self._votes_to_score

    def calculate(self):
        for key in self._votes_to_score:
            item = self._votes_to_score.get(key)
            self.clean_votes(item.votings)
            self.calculate_percent()
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
        government_orientation, spectrum = self.findSpectrum(item, orientation)
        if item['ideCadastro'] in self._score:
            self.incrementVotingTimes(self._score.get(item['ideCadastro']))
            self.incrementScore(item, benchOrientation)
            self.incrementSpectrumScore(item, government_orientation, spectrum)
        else:
            congressman = Congressman(congressman_id=item['ideCadastro'], name=item['Nome'],
                                      party=item['Partido'], state=item['UF'])
            self.incrementVotingTimes(congressman)
            self._score.update({item['ideCadastro']: congressman})
            self.incrementScore(item, benchOrientation)
            self.incrementSpectrumScore(item, government_orientation, spectrum)

    def findOrientation(self, item: dict, orientation: dict):
        orientation = self.separateOrientation(orientation)
        for bench in orientation:
            partido = item['Partido'].lower()
            if partido == bench.lower() or 'repr.{}'.format(partido) == bench.lower():
                return orientation.get(bench)

    def findSpectrum(self, item: dict, orientation: dict):
        government_orientation = {}
        philosophy = ''
        if int(self._init_year) == 2011 and int(self._end_year) == 2012:
            government_orientation.update({'Partido': 'PT'})
        else:
            government_orientation.update({'Partido': 'PSL'})
        government_orientation = self.findOrientation(government_orientation, orientation)
        party = item['Partido'].lower()
        for party_spectrum in self._spectrum:
            if party_spectrum['partido'].lower() == party or 'repr.{}'.format(party) == party_spectrum['partido']:
                philosophy = party_spectrum['filosofia']
        return government_orientation, philosophy

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

    def incrementSpectrumScore(self, congressman: dict, government_orientation: Bench, spectrum: str):
        if government_orientation is None or not spectrum:
            return

        if spectrum == 'G' and congressman['Voto'] == government_orientation.orientation:
            congressmanToScore = self._score.get(congressman['ideCadastro'])
            congressmanToScore.spectrum_score = congressmanToScore.spectrum_score + 1

        if spectrum == 'O' and congressman['Voto'] != government_orientation.orientation:
            congressmanToScore = self._score.get(congressman['ideCadastro'])
            congressmanToScore.spectrum_score = congressmanToScore.spectrum_score + 1

    def calculate_percent(self):
        for key in self._score:
            congressman = self._score[key]
            result = congressman.party_score / congressman.voting_times
            congressman.score_percent = result
            spectrum_result = congressman.spectrum_score / congressman.voting_times
            congressman.spectrum_percent = spectrum_result

    def build_spectrum(self):
        spectrum = []
        if int(self._init_year) == 2011 and int(self._end_year) == 2012:
            file_path = 'files/dilma.csv'
        else:
            file_path = 'files/bolsonaro.csv'
        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                spectrum.append(row)
        return spectrum

    @staticmethod
    def incrementVotingTimes(congressman):
        congressman.voting_times = congressman.voting_times + 1

    @staticmethod
    def composeOrientations(keys: list, orientation: dict, bench: Bench):
        for key in keys:
            orientation.update({'P' + key: Bench(initials=bench.initials, orientation=bench.orientation)})
