class Property:
    def __init__(self):
        self._col = None

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, value):
        self._col = value

    @col.deleter
    def col(self):
        del self.col
