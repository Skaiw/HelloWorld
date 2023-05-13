import _random
import random
class Generator_vet():

    podmety = ["jednorožec", "programátor", "manažer", "hroch", "T rex"]
    prisudky = ["spal", "ležel", "vařil", "uklízel", "derivoval"]
    privlastky = ["modrý", "velký", "hubený", "nejlepší", "automatizovaný"]
    prislovce = ["rychle", "s oblibou", "hodně", "málo", "se zpožděním"]
    prislovecnaUrc = ["pod stolem", "v lese", "u babičky", "v práci", "na stole"]

    def generuj_vetu(self):  # metoda musí být v třídě
        """Generuje náhodné souvětí z jednotlivých částí"""
        podmet = random.choice(self.podmety)  # přidání self
        prisudek = random.choice(self.prisudky)  # přidání self
        privlastek = random.choice(self.privlastky)  # přidání self
        prislovce = random.choice(self.prislovce)  # přejmenování proměnné a přidání self
        prislovecneUrceniMista = random.choice(self.prislovecnaUrc)  # přejmenování proměnné a přidání self

        #spojeni částí do věty
        souveti = f"{privlastek} {podmet} {prisudek} {prislovce} {prislovecneUrceniMista}."
        return souveti
