from ispiti import ispis_ispita

def ispis_studenta(student):
    print(f"\tStudent {student['ime']} {student['prezime']} je prijavio:")
    ispis_ispita(student['ispit'])

def ispis_svih_studenata(studenti):
    print('Popis svih studenata: ')
    for student in studenti:
      ispis_studenta(student)

