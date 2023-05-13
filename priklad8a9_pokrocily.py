# zadání vstupu

retezec = input("Zadejte text k zašifrování: ")

heslo = input("Zadejte heslo: ")
sifra = ""
# průchod všemi znaky ve vstupu
for i, znak in enumerate(retezec):
    # posunu v abecedě
    x = ord(heslo[i % len(heslo)]) - (ord("a") - 1)
    # oprava přetečení přes z
    if ord(znak) + x > ord("z"):
        x -= ord("z") - ord("a") + 1
    # transformace znaku
    vysledek = chr(ord(znak) + x)
    # přidání znaku do výstupu
    sifra += vysledek
print("Výsledek:", sifra)
input()