from pes import Pes
from osoba import Osoba


karel = Osoba("Petr Optr")
lenka = Osoba("Iva Zahrídková")
azor = Pes("Azor")
karel.pes = azor
lenka.pes = azor
print(azor)

# Zestárnutí psa
karel.pes.zestarni()
lenka.pes.zestarni()

# Kontrolní výpis dat
print(azor)