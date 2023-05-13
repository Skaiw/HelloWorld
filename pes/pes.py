class Pes():
    jmeno = None
    vek = 1
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def zestarni (self):
        self.vek += 1
    def __str__(self):
        return "{0} ({1})".format(self.jmeno, self.vek)
