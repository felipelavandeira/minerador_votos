class PropositionVoting:

    def __init__(self, initials: str, number: int, year: int, votings: list, author_bench: str):
        self._initials = initials
        self._number = number
        self._year = year
        self._votings = votings
        self._author_bench = author_bench

    @property
    def initials(self):
        return self._initials

    @initials.setter
    def initials(self, initials):
        self._initials = initials

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def votings(self):
        return self._votings

    @votings.setter
    def votings(self, votings):
        self._votings = votings

    @property
    def author_bench(self):
        return self._author_bench

    @author_bench.setter
    def author_bench(self, author_bench):
        self._author_bench = author_bench