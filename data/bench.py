class Bench:

    def __init__(self, initials: str, orientation: str):
        self._initials = initials.strip()
        self._orientation = orientation.strip()
        self._spectrum = ""

    @property
    def initials(self):
        return self._initials

    @initials.setter
    def initials(self, initials: str):
        self._initials = initials

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self._orientation = orientation

    @property
    def spectrum(self):
        return self._spectrum

    @spectrum.setter
    def spectrum(self, spectrum):
        self._spectrum = spectrum