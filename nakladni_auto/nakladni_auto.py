class NakladniAuto:
    def auto(self,cislo):
        if naklad > 3000:
            print("Auto je přetížené")
        elif naklad < 0:
            print("Auto nic neveze")
        else:
            return ("Auto veze{0}".format(self,cislo))

zemina = NakladniAuto
zemina.vaha = None

naklad = 0 + zemina.vaha
