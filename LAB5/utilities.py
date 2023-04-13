def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj od {min} do {max}: "))

            if broj<min or broj>max:
                raise Exception(f"Broj nije u intervalu od {min} do {max}")

        except ValueError:
            print("Unjeli ste znak a ne cijeli broj!")

        except Exception as e:
            print(e)

        else:
            return broj