
def get_ispit(redni_broj, ispit):
    return f"{redni_broj}. Ispit iz kolegija {ispit.kolegij.ime}"

def ispis_svih_ispita(ispiti):
    print('Ispis svih ispita: ')
    for ispit in ispiti:
        ispit.ispis()
