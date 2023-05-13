# inicializace proměnných
retezec = input("Zapis co chces zašifrovat bez diakritiky: ")
print("Původní zpráva:", retezec)
zprava = ""
posun = 1

# cyklus projíždějící jednotlivé znaky
for znak in retezec:
    pass
    i = ord(znak)
    i = i + posun
    znak = chr(i)
    zprava = zprava + znak
# výpis
print("Zašifrovaná zpráva:", zprava)
input()