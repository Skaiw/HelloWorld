#cisla = []
#for i in range(20,0,-1):
#    cisla.append(i)

#for prvek in cisla:
#    print(prvek)



zelenina = ["zelí", "okurka", "rajče", "paprika", "ředkev",
            "mrkev", "brokolice"]
ovoce = ["banán","pomeranč","mandarinka","malina","jablko","hruška","třešně"]

pocet_dotazu=0
while True:
    vstup = input("Zadej název libovolného ovoce nebo zeleniny: ")
    pocet_dotazu +=1
    if vstup in zelenina:
         print("Zadal jsi zeleninu")
    elif vstup in ovoce:
         print("Zadal jsi ovoce")
    else:
         print("Tvoje slovo nemám v seznamu")

    while True:
        pokracovani=input("Přeješ si zadat další slovo? (ano/ne)")
        if pokracovani == "ano":
            break
        elif pokracovani =="ne":
            print("Zadal jsi", pocet_dotazu, "slov")
            exit()

        else:
            print("neplatná odpověď")
