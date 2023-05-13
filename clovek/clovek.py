class Clovek():
    jmeno = None
    vek = None
    vycerpani = 20
    unava = 0
    kolo_max_zatez = 10
    odpocinek = -10

    # Konstruktor
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def behej(self, zatez):
        if self.unava >= self.vycerpani:
            print("Jsem příliš unavený")
        else:
            self.unava = min(self.vycerpani, self.unava + zatez)

    def spanek(self, zatez):
        if self.unava >= self.vycerpani:
            self.unava = max(0, self.unava - zatez + self.odpocinek)
        else:
            print("Nemohu spát, nejsem dost unavený.")

    def __str__(self):
        if self.unava >= self.vycerpani:
            return "{0} {1}".format(self.jmeno, self.vek)
        else:
            return "{0} {1}\nJsem příliš unavený".format(self.jmeno, self.vek)
