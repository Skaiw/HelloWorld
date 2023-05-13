class Zdravic:
    """
    Třída reprezentuje zdravič, který slouží ke zdravení uživatele
    """
    def pozdrav(self, jmeno):
        """Vrátí pozdrav uživatele s nastaveným textem a jeho jmenem
        """
        return("{0} {1}!".format(self.text,jmeno))

class Zdar:
    """
        Třída reprezentuje zdravič, který slouží ke zdravení uživatele
        """

    def zdrec (self, name):
        """Vrátí pozdrav uživatele s nastaveným textem a jeho jmenem
        """
        return ("{0} {1}!".format(self.text1, name))

zdrec = Zdravic()
zdrec.text="ouje"
print(zdrec.pozdrav("bububu"))
ahoj = Zdar()
ahoj.text1 = "zdarec"
print(ahoj.zdrec("Lukas"))
zdravic = Zdravic()
zdravic.text = "Ahoj uživateli"
print(zdravic.pozdrav("Karel"))
print(zdravic.pozdrav("Petr"))
zdravic.text = "Vítám tě tu programátore"
print(zdravic.pozdrav("Richard"))