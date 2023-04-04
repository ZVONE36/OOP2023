from datetime import date

korisnici = []
kategorije = []
prodaje = []

broj_korisnika = int(input("Unesite broj korisnika: "))
for i in range(1, broj_korisnika+1):
    korisnik = {}
    korisnik['ime'] = input(f"Unesite ime {i}. korisnika: ").capitalize()
    korisnik['prezime'] =input(f"Unesite prezime {i}. korisnika: ").capitalize()
    korisnik['telefon'] = int(input(f"Unesite telefon {i}. korisnika: "))
    korisnik['email'] = input(f"Unesite email {i}. korisnika: ")
    korisnici.append(korisnik)

broj_kategorija = int(input("Unesite broj kategorija: "))
for i in range(1, broj_kategorija+1):
    kategorija = {}
    artikli = []
    kategorija['naziv'] = input(f"Unesite naziv {i}. kategorije: ").capitalize()

    broj_artikala = int(input(f"Unesite broj artikala za {i}. kategoriju: "))
    for j in range(1, broj_artikala+1):
        artikl = {}
        artikl['naslov'] = input(f"Unesite naslov {j}. artikla: ").capitalize()
        artikl['opis'] = input(f"Unesite opis {j}. artikla: ").capitalize()
        artikl['cijena'] = float(input(f"Unesite cijenu {j}. artikla: "))
        artikli.append(artikl)

    kategorija['artikli'] = artikli
    kategorije.append(kategorija)

broj_prodaja = int(input("Unesite broj prodaja: "))
for i in range(1, broj_prodaja+1):
    prodaja = {}
    dan = int(input(f"Unesite dan isteka {i}. prodaje: "))
    mjesec = int(input(f"Unesite mjesec isteka {i}. prodaje: "))
    godina = int(input(f"Unesite godinu isteka {i}. prodaje: "))
    prodaja['datum'] = date(godina,mjesec,dan)

#ODABIR KORISNIKA

    print(f"Odaberite korisnika {i}. prodaje: ")

    for j, korisnik in enumerate(korisnici, start=1):
        print(f"\t{j}. {korisnik['ime']} {korisnik['prezime']}")

    odabrani_korisnik = int(input("Odabrani korisnik: "))-1

#ODABIR KATEGORIJE

    print(f"Odaberite kategoriju {i}. prodaje: ")

    for k, kategorija in enumerate(kategorije, start=1):
        print(f"\t {k}. {kategorija['naziv']}")

    odabrana_kategorija = int(input("Odabrana kategorija: "))-1

#ODABIR ARTIKLA

    print(f"Odaberite artikl {i}. prodaje: ")

    for z, artikl in enumerate(kategorije[odabrana_kategorija]['artikli'], start=1):
        print(f"\t {z}. {kategorije[odabrana_kategorija]['artikli'][z-1]['naslov']}")

    odabrani_artikl = int(input("Odabrani artikl: "))-1

    prodaja['korisnik'] = korisnici[odabrani_korisnik]
    prodaja['artikl'] = kategorije[odabrana_kategorija]['artikli'][odabrani_artikl]
    prodaje.append(prodaja)


for i, prodaja in enumerate(prodaje, start=1):
    print(f"Prodaja {i}: ")
    print("Informacije o korisniku: ")
    print(f"\t Ime: {prodaja['korisnik']['ime']}")
    print(f"\t Prezme: {prodaja['korisnik']['prezime']}")
    print(f"\t Telefon: {prodaja['korisnik']['telefon']}")
    print(f"\t Email: {prodaja['korisnik']['email']}")

    print("Informacije o artiklu: ")
    print(f"\t Naslov: {prodaja['artikl']['naslov']}")
    print(f"\t Opis: {prodaja['artikl']['opis']}")
    print(f"\t Cijena: {prodaja['artikl']['cijena']}")

    print("Datum isteka: ")
    print(f"\t Dan: {prodaja['datum'].day}")
    print(f"\t Mjesec: {prodaja['datum'].month}")
    print(f"\t Godina: {prodaja['datum'].year}")

    print("-"*30)




