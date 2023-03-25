from datetime import date

kolegij = {}

kolegij["ime"] = input("Unesite ime kolegija: ").upper()
kolegij["bodovi"] = int(input("Unesite ECTS bodove za kolegij: "))

ispit = {}

ispit["kolegij"] = kolegij


dan = int(input("Unesite dan: "))
mjesec = int(input("Unesite mjesec: "))
godina = int(input("Unesite godinu: "))

ispit["datum"] = date(godina, mjesec, dan)

student = {}

student["ispit"] = ispit


student["ime"] = input("Unesite ime studenta: ").title()
student["prezime"] = input("Unesite prezime studenta: ").title()

print("Student", student["ime"], student["prezime"])
print("je prijavio ispit iz kolegija", student["ispit"]["kolegij"]["ime"], "koji će se održati datuma: ", student["ispit"]["datum"])

