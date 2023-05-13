from pojistenec import Pojisteny
from pojistenec import Evidencer

def main():
    evidencer = Evidencer()

    while True:
        print("\nMenu:")
        print("1. Vytvorit pojisteneho")
        print("2. Zobrazit seznam pojistenych")
        print("3. Vyhledat pojisteneho")
        print("4. Konec")

        volba = input("Zadejte volbu (1-4): ")

        if volba == "1":
            jmeno = input("Jmeno: ")
            prijmeni = input("Prijmeni: ")
            vek = int(input("Vek: "))
            telefon = input("Telefonni cislo: ")
            pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
            evidencer.pridej_pojisteneho(pojisteny)
            print("Pojisteny byl uspesne vytvoren.")

        elif volba == "2":
            if len(evidencer.pojisteni) > 0:
                print("Seznam pojistenych:")
                evidencer.zobraz_seznam()
            else:
                print("Seznam pojistenych je prazdny.")

        elif volba == "3":
            jmeno = input("Jmeno: ")
            prijmeni = input("Prijmeni: ")
            pojisteny = evidencer.najdi_pojisteneho(jmeno, prijmeni)
            if pojisteny:
                print("Nalezeny pojisteny:")
                print(pojisteny)
            else:
                print("Pojisteny nebyl nalezen.")

        elif volba == "4":
            break

        else:
            print("Neplatna volba. Zadejte znovu.")


if __name__ == "__main__":
    main()






