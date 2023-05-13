#palindrom = input("Zadej palindrom: \n")  # získání řetězce od uživatele
#palindrom = palindrom.lower()  # převod řetězce na malá písmena (pro ověření palindromu je to důležité)
#if palindrom == palindrom[::-1]:  # porovnání řetězce se svým reverzním řetězcem
#    print("Ano, je to palindrom")
#else:
#    print("Ne, není to palindrom")


print("ASCII tabulka")
print("=============")

for i in range(256):
    print(str(i) + ':' + str(chr(i)) + '\t', end='')
input()