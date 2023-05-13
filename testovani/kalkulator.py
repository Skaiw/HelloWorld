class Kalkulator:
    def to_the_power_of(self, a,b):
        return a ** b

    def scitani(self,a,b):
        return a + b

    def odecitani(self,a,b):
        return a - b

    def nasobeni(self, a, b):
        return a * b

    def deleni(self, a, b):
        if b == 0:
            print("Špatné zadání, nedá se dělit nulou")
            return None
        return a / b



