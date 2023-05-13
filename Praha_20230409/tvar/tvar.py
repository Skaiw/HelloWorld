class Tvar():
    def __init__(self, pocet_sten):
        self.pocet_sten = pocet_sten

    def vypis_pocet_sten (self):
        return (f"Mám počet stěn {self.pocet_sten}")
    def __str__(self):
        return "tvar"


class Ctverec(Tvar):

    def __init__(self, pocet_sten):
        super().__init__(pocet_sten)
    def __str__(self):
        return "ctverec"

class Trojuhelnik(Tvar):
    def __init__(self, pocet_sten):
        super().__init__(pocet_sten)
    def __str__(self):
        return "trojuhelnik"

class Sestisten(Tvar):
    def __init__(self, pocet_sten):
        super().__init__(pocet_sten)

troj = Trojuhelnik(3)
ctver = Ctverec(4)
sest = Sestisten(6)
print(troj.vypis_pocet_sten() + ctver.vypis_pocet_sten())

pole_tvaru = []

pole_tvaru.append(ctver)
pole_tvaru.append(troj)
pole_tvaru.append(sest)

for tvar in pole_tvaru:
    print(tvar,tvar.vypis_pocet_sten())