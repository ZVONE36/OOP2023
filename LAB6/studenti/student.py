class Student:
    def __init__(self, ime, prezime, ispit):
        self.ime = ime
        self.prezime = prezime
        self.ispit = ispit

    def ispis(self):
        print(f"\t Student {self.ime} {self.prezime} je prijavio:")
        self.ispit.ispis()