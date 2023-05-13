class Clovek:
    jmeno = None
    vek = None
#konstruktor
    def __init__(self, jmeno, vek):
        self._jmeno = jmeno #VEŘEJNÉ JMÉNO
        self._vek = vek
        #self._jmeno  = jmeno BUDE NEVEŘEJNÉ

#"Ahoj" je nepovinný parametr v pozdravu. Který se vyplní, když nezadáme něco jiného
# pokud přidám artibut (text) musím jej u každého prvku definovat nebo zadat v nepovinném parametru
    def pozdrav(self,pozdrav="Ahoj",text=" "):
        print(f"{pozdrav}, jsem {self.jmeno}, je mi {self._vek}. {text}")
    def get_jmeno(self):
        return self._jmeno

    def set_vek(self,novy_vek):
        if novy_vek > 0:
            self._vek = novy_vek
