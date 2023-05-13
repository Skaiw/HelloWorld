from kalkulacka import Kalukacka
kalkulacka=Kalukacka()
try:
    vysledek = kalkulacka.vydel(0,0)
    print(vysledek)
except Exception as e:
    print(e)
finally:
    pass