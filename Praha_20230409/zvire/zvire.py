class Zvire():
    def __init__(self,jmeno, vaha):
        self.jmeno = jmeno
        self.vaha = vaha

    def mluv(self):
        return ""
    def __str__(self):
        return "jsem zvíře"

    def nakrm(self, jidlo):
        if self.vaha + jidlo < 9:
            print (f" létá")
        else:
            print (f" je moc těžké, aby létalo")

    def get_leta(self,nakrm):
        if self.vaha + nakrm <=9:
            return print(f" může létat")
        else:
            print(f"nemůže létat")

class Had(Zvire):
    def __init__(self, jmeno, vaha):
        super().__init__(self,jmeno, vaha)
    def mluv(self):
        return "sss"

class Kachna(Zvire):
    def __init__(self, jmeno, vaha):
        super().__init__(self,jmeno, vaha)
    def mluv(self):
        return "GAGA"

class Ryba(Zvire):
    def __init__(self, jmeno, vaha,jazyk):
        super().__init__(self,jmeno, vaha)
        self.jazyk = jazyk
    def mluv(self):
        return "°°°°°°"

pole_zvirat = [Had(5,5),Kachna(4,"asdsa"),Ryba(3,2)]

zvirata=[]

zvirata.append(Had(3,True))
zvirata.append(Kachna)

for zvire in pole_zvirat:
    print(zvire,pole_zvirat)