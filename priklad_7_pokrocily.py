import statistics

cisla=[]
print("Zadávej čísla a nakonec zadej pouze ENTER pro ukončení zadávání")
while True:
    cislo= input("Zadej číslo: ")
    if cislo =="":
        break
    cislo = int(cislo)
    cisla.append(cislo)
cisla_2 = sorted(cisla)
length =len(cisla)
if length % 2 == 0: #pro sudý počet prvků vezme průměr ze dvou středních prvků
    median = (cisla_2[length//2 - 1] + cisla_2[length//2]) /2
else: #lichypocet cisel
    median = statistics.median(cisla)

for cislo in cisla:
    deviation = cislo - median
    print(f"{cislo} se od mediánu odlišuje o {deviation}")
