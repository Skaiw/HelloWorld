class Kalkulacka:
    def vstup(self, cislo):
        return ("{0} {1}".format(self.text,cislo))


vypocet = Kalkulacka()
vypocet.cislo1 = float(input("Zadej 1. číslo: "))
vypocet.cislo2 = float(input("Zadej 2. číslo: "))
vypocet.text = "Součet:"
print(vypocet.vstup(vypocet.cislo1 + vypocet.cislo2))
vypocet.text = "Rozdíl:"
print(vypocet.vstup(vypocet.cislo1 - vypocet.cislo2))
vypocet.text = "Součin:"
print(vypocet.vstup(vypocet.cislo1 * vypocet.cislo2))
vypocet.text = "Podíl:"
print(vypocet.vstup(vypocet.cislo1 / vypocet.cislo2))