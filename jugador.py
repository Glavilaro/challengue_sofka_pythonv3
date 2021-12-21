class jugador:
    def __init__(self, nombre, puntaje):
        self.name = nombre
        self.score = puntaje

    @property
    def name(self):
        return self.__nombre

    @name.setter
    def name(self, valor):
        self.__nombre = valor

    @property
    def score(self):
        return self._puntaje

    @score.setter
    def score(self, valor):
        self._puntaje = valor

    def update_score(self, puntaje):
        self.score += puntaje

    def clear_score(self):
        self.score = 0