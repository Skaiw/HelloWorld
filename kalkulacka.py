#!/usr/bin/env python3

print("Kalkulačka\n")
pokracovat = True
def nacti_cislo(text_zadani, text_chyba):
    spatne = True
    while spatne:
        try:
            cislo = float(input(text_zadani))
            spatne = False
        except ValueError:
            print(text_chyba)
        else:
            return cislo
def dalsi_priklad():
    nezadano = True
    while nezadano:
        odpoved = input("\nPřejete si zadat další příklad? y / n: ")
        if (odpoved == "y" or odpoved == "Y"):
            return True
        elif (odpoved == "n" or odpoved == "N"):
            return False
        else:
            pass
while pokracovat:
    prvni_cislo = int(input("Zadejte první číslo: "))
    druhe_cislo = int(input("Zadejte druhé číslo: "))
    print("1 - sčítání")
    print("2 - odčítání")
    print("3 - násobení")
    print("4 - dělení")
    print("5 - umocňování")
    cislo_operace = int(input("Zadejte číslo operace: "))
    if cislo_operace == 1:
        print("Jejich součet je:", prvni_cislo + druhe_cislo)
    elif cislo_operace == 2:
        print("Jejich rozdíl je:", prvni_cislo - druhe_cislo)
    elif cislo_operace == 3:
        print("Jejich součin je:", prvni_cislo * druhe_cislo)
    elif cislo_operace == 4:
        print("Jejich podíl je:", prvni_cislo / druhe_cislo)
    elif cislo_operace == 5:
        print(prvni_cislo, "na", druhe_cislo, "je:", prvni_cislo ** druhe_cislo)
    else:
        print("Neplatná volba!")
    nezadano = True
    while nezadano:
        odpoved = input("\nPřejete si zadat další příklad? y / n: ")
        if (odpoved == "y" or odpoved == "Y"):
            nezadano = False
        elif (odpoved == "n" or odpoved == "n"):
            nezadano = False
            pokracovat = False
        else:
            pass
input("\nStiskněte klávesu Enter...")