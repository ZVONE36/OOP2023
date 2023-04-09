from datetime import date

korisnici = []
kategorije = []
prodaje = []
telefoni = []

broj_telefona = int(input("Unesite broj telefona: "))
for i in range(1,broj_telefona+1):
    telefon = {}
    telefon['broj'] = int(input(f"Unesite broj {i}. telefona: "))
    telefon['pozivni'] = int(input(f"Unesite pozivni {i}. telefona: "))
    telefon['proizvodac'] = input(f"Unesite proizvodaca {i}. telefona: ")
    telefoni.append(telefon)

broj_korisnika = int(input("Unesite broj korisnika: "))
for i in range(1, broj_korisnika+1):
    korisnik = {}
    korisnik['ime'] = input(f"Unesite ime {i}. korisnika: ").title()
    korisnik['prezime'] = input(f"Unesite prezime {i}. korisnika: ").title()
    korisnik['telefon'] = int(input(f"Unesite telefon {i}. korisnika: "))
    korisnik['email'] = input(f"Unesite email {i}. korisnika: ").strip()

    print("Popis proizvodaca telefona: ")

    for j,telefon in enumerate(telefoni, start=1):
        print(f"\t{j}. {telefon['proizvodac']} ")

    odabrani_telefon=int(input("Odaberite telefon: "))-1
    korisnik['tele'] = telefoni[odabrani_telefon]
    korisnici.append(korisnik)

broj_kategorija = int(input("Unesite broj kategorija: "))
for i in range(1, broj_kategorija+1):
    kategorija = {}
    kategorija['naziv'] = input(f"Unesite naziv {i}. kategorije: ")
    artikli = []

    broj_artikla = int(input(f"Unesite broj artikla za {i}. kategoriju: "))
    for j in range(1, broj_artikla+1):
        artikl = {}
        artikl['naslov'] = input(f"Unesite naslov {j}. artikla: ")
        artikl['opis'] = input(f"Unesite opis {j}. artikla: ")
        artikl['cijena'] = float(input(f"Unesite cijenu {j}. artikla: "))
        artikli.append(artikl)
    kategorija['artikli'] = artikli
    kategorije.append(kategorija)

broj_prodaja  = int(input("Unesite broj prodaja: "))
for i in range(1, broj_prodaja+1):
    prodaja = {}
    dan = int(input(f"Unesite dan isteka {i}. prodaje: "))
    mjesec = int(input(f"Unesite mjesec isteka {i}. prodaje: "))
    godina = int(input(f"Unesite godinu isteka {i}. prodaje: "))
    prodaja['datum'] = date(godina, mjesec, dan)

#ODABIR KORISNIKA

    print(f"Odaberite korisnika {i}. prodaje: ")
    for j, korisnik in enumerate(korisnici, start=1):
        print(f"\t{j}. {korisnik['ime']} {korisnik['prezime']}")
    odabrani_korisnik = int(input("Odabrani korisnik: "))-1

#ODABIR KATEGORIJE

    print(f"Odaberite kategoriju {i}. prodaje: ")
    for k, kategorija in enumerate(kategorije, start=1):
        print(f"\t{k}. {kategorija['naziv']} ")
    odabrana_kategorija = int(input("Odabrana kategorija: "))-1

#ODABIR ARTIKLA

    print(f"Odaberite artikl {i}.prodaje: ")
    for z, artikl in enumerate(kategorije[odabrana_kategorija]['artikli'], start=1):
            print(f"\t{z}. {artikl['naslov']}")
    odabrani_artikl = int(input("Odabrani artikl: "))-1

    prodaja['korisnik'] = korisnici[odabrani_korisnik]
    prodaja['artikl'] = kategorije[odabrana_kategorija]['artikli'][odabrani_artikl]
    prodaja['telefon'] = korisnici[odabrani_telefon]
    prodaje.append(prodaja)

for i, prodaja in enumerate(prodaje, start=1):
    print(f"Prodaja {i}: ")
    print("Informacije o korisniku: ")
    print(f"\t Ime {prodaja['korisnik']['ime']}")
    print(f"\t Prezime {prodaja['korisnik']['prezime']}")
    print(f"\t Telefon {prodaja['korisnik']['telefon']}")
    print(f"\t Email {prodaja['korisnik']['email']}")
    print(f"\t Proizvodac {prodaja['korisnik']['tele']['proizvodac']}")

    print("Informacije o artiklu: ")
    print(f"\t Naslov {prodaja['artikl']['naslov']}")
    print(f"\t Opis {prodaja['artikl']['opis']}")
    print(f"\t Cijena {prodaja['artikl']['cijena']}")

    print("Datum isteka prodaje: ")
    print(f"\t Dan {prodaja['datum'].day}")
    print(f"\t Mjesec {prodaja['datum'].month}")
    print(f"\t Godina {prodaja['datum'].year}")

    print("-"*30)