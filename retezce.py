#!/usr/bin/env python3

print("Program zjistí, z čeho se skládá slovo.")
slovo = input("Zadejte slovo: ")
samohlasky = 0
souhlasky = 0
ostatni = 0
cisel = 0
for znak in slovo:
    if znak in "aáeéěiíoóuúů":
        samohlasky = samohlasky + 1
    elif znak in "bcčdďfghjklmnňpqrřsštťvwxzž":
        souhlasky = souhlasky + 1
    elif znak in "0123456789":
        cisel = cisel + 1
    else:
        ostatni = ostatni + 1
print(slovo, "má: ")
print("samohlásek", (len(slovo)))
print("souhlásek", (len(slovo)))
print("čísel", (len(slovo)))
print("ostatních znaků...", (len(slovo)))
input("\nAplikaci ukončíte stisknutím klávesy Enter...")

