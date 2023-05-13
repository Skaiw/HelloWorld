class Naklad():
    def __init__(self):
        self.nosnost = 3000
        self.nalozeno = 0
    def nakladka(self, naklad):
        if naklad < 0:
            print("Nemůžeš naložit zápornou hodnotu")
        elif naklad >= 3000:
            print("Náklad má větší hmotnost než je nostnost auta")
        else:
            self.nalozeno += naklad
            print(f"{self.nalozeno}")

    def vykladka(self, vyloz):
        if self.nalozeno - vyloz < 0:
           raise Exception("nemůžeš vyložit víc než máš naloženo")
        else:
            self.nalozeno -= vyloz
        return (f"Vezeš {self.nalozeno}")

    def aktualni_stav(self):
        print(f"Vezeš {self.nalozeno}")