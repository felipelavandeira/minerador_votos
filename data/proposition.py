import datetime


class Proposition:

    def __init__(self, id: int, name: str, type: str, number: int, year: int, dt_voting: datetime.date):
        self._id = id
        self._name = name
        self._type = type
        self._number = number
        self._year = year
        self._dt_voting = dt_voting

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type: str):
        self._type = type

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number: int):
        self._number = number

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year: int):
        self._year = year

    @property
    def dt_voting(self):
        return self._dt_voting

    @dt_voting.setter
    def dt_voting(self, dt_voting: datetime.date):
        self._dt_voting = dt_voting
