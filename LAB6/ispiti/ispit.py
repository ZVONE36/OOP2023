class Ispit:
    def __init__(self, kolegij, datum):
        self.__kolegij = kolegij
        self.__datum = datum

    @property
    def kolegij(self):
        return self.__kolegij

    @kolegij.setter
    def kolegij(self, kolegij):
        self.__kolegij=kolegij

    @property
    def datum(self):
        return self.__datum

    @datum.setter
    def datum(self, datum):
        self.__datum=datum

    def ispis(self):
        print(f"Ispit iz kolegija {self.kolegij}, koji nosi {self.datum} ECTS bododva")