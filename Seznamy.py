#cisla = list(range(1,10,2))
#for cislo in cisla:
#    print(cislo, range(1,3-1,1) #cisla[0] = 1

#cisla = list(range(1,8,2))
#print(cisla)

#cisla = list(range(1,10,3))
#for i in range(len(cisla)):
#    cisla[i] += 1
#    print(cisla)

# funkce enumerate -vypsání a seřazení seznamu
#simpsons = ["Homer","Marge","Bart","Lisa","Maggie"]
#for i, prvek in enumerate(simpsons):
#    print("%d: %s" % (i, prvek))

#vypsani seznamu
#cisla = range(10)
#print(list(cisla))
#print(list(cisla[0:5]))
#print(list(cisla[2:8]))
#print(list(cisla[1:7:2]))
#print(list(cisla[6:]))
#print(list(cisla[::2*2]))

simpsons = ["Homer" , "Marge", "Bart" , "Lisa","Maggie"]
simpson = input("Zdar, zadej svého oblíbeného Simpsona: ")
if simpson in simpsons:
    position = simpsons.index(simpson);
    print("Jo, to je můj %d. nejoblíbenější simpson!" % (position + 1))
else:
    print("Hele, tohle není Simpson!")