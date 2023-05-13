from hra import Hra
hra = Hra()
prikaz = ""

while prikaz.lower() != "konec":
    print(hra.vrat_auktualni_lokaci())
    print("Zadej příkaz: ", end="")
    prikaz = input()
    hra.zpracuj_prikaz(prikaz)