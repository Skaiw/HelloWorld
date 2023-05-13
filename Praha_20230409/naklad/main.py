from naklad import Naklad

try:
    auto = Naklad()
    auto.nakladka(2000)
    auto.vykladka(1500)
    auto.nakladka(-500)
    auto.vykladka(501)
    auto.nakladka(3500)

except Exception as e:
    print(e)
finally:
    pass
auto.aktualni_stav()