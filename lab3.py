from datetime import date

kolegiji = []

broj_kolegija = int(input("Unesite broj kolegija: "))
for i in range(1, broj_kolegija+1):
    kolegij = {}
    kolegij['ime'] = input(f"Unesite ime {i}. kolegija: ").upper()
    kolegij['ECTS'] = int(input(f"Unesite ECTS bodove za {i}. kolegij: "))
    kolegiji.append(kolegij)

ispiti = []

broj_ispita = int(input("Unesite broj ispita: "))
for i in range(1, broj_ispita+1):

    ispit = {}

    print("Popis svih kolegija: ")

    for j, kolegij in enumerate(kolegiji, start=1):
        print(f"\t{j}. {kolegij['ime']}")

    odabrani_kolegij = int(input("Unesite kolegij: "))
    ispit['kolegij'] = kolegiji[odabrani_kolegij-1]

    dan = int(input(f"Unesite dan {i}. ispita: "))
    mjesec = int(input(f"Unesite mjesec {i}. ispita: "))
    godina = int(input(f"Unesite godinu {i}. ispita: "))

    ispit['datum'] = date(godina,mjesec,dan)

    ispiti.append(ispit)

studenti = []

broj_studenata = int(input("Unesite broj studenata: "))
for i in range(1, broj_studenata+1):
    student = {}
    student['ime'] = input(f"Unesite ime {i}. studenta: ").capitalize()
    student['prezime'] = input(f"Unesite prezime {i}. studenta: ").capitalize()

    for j, kolegij in enumerate(ispiti, start=1):
        print(f"\t{i}. Ispit iz kolegija {ispit['kolegij']['ime']}")
    odabrani_ispit = int(input("Unesite kolegij: "))
    student['ispit'] = ispiti[odabrani_ispit-1]
    studenti.append(student)

print("Popis svih studenata: ")
for student in studenti:
    print(f"\t Student {student['ime']} {student['prezime']} je prijavio:")
    print(f"\t\t Ispit iz kolegija {student['ispit']['kolegij']['ime']} koji ce se odrzati", student['ispit']['datum'])

