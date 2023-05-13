from dedicnost import Clovek
from dedicnost import Programator

programator = Programator("Jirka", 58, "CSS")
programator.pozdrav("buubbubuubu")
programator.pozdrav()

lide = [Clovek("Karel",54), Programator("Pepan",16,"Py"), Programator("Jitka",24,"CSS")]
for clovek in lide:
    clovek.pozdrav("asdasdasd")
    clovek.pozdrav()
print(lide[2].jazyk) #číslo určuje pořadí objektu v řetězci

skaiw=Clovek("Lukáš",34)

print(skaiw)