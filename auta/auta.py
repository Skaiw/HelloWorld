class Auto():

    def __init__(self, spz, barva):
        self.spz = spz
        self.barva = barva

    def Zaparkuj(self, garaz):
        garaz.auto = self

