from ispiti import get_ispit
from utilities import unos_intervala
from .student import Student
def unos_studenta(ispiti, redni_broj):

    ime = input(f"Unesite ime {redni_broj}. studenta: ").capitalize()
    prezime = input(f"Unesite prezime {redni_broj}. studenta: ").capitalize()
    for j, ispit in enumerate(ispiti, start=1):
        print(get_ispit(j, ispit))

    x = len(ispiti)
    print('Za odabir ispita')
    odabrani_ispit = unos_intervala(1, x)
    ispit = ispiti[odabrani_ispit - 1]
    return Student(ime, prezime, ispit)