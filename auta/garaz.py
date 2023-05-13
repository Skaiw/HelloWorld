class Garaz:
    def __init__(self):
        self.auto = None

    def Vypis(self):
        if self.auto is None:
            print("V garáži není žádné auto.")
        else:
            print(f"V garáži je auto: {self.auto.spz}")