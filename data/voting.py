class Voting:

    def __init__(self, bench_orientation: list, votes: list):
        self._bench_orientation = bench_orientation
        self._votes = votes

    @property
    def bench_orientation(self):
        return self._bench_orientation

    @bench_orientation.setter
    def bench_orientation(self, bench_orientation):
        self._bench_orientation = bench_orientation

    @property
    def votes(self):
        return self._votes

    @votes.setter
    def votes(self, votes):
        self._votes = votes
