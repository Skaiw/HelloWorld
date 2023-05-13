# řetězec, který chceme dekódovat
s = ".-.. . --- -. .- .-. -.. ---"
print("Původní zpráva: %s" % s)
# řetězec s dekódovanou zprávou
zprava = ""

# vzorové seznamy
abecedniZnaky = "abcdefghijklmnopqrstuvwxyz"
morseovyZnaky = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
"..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",
"...-", ".--", "-..-", "-.--", "--.."]

# rozbití řetězce na znaky morzeovky
znaky = s.split(" ")

# iterace znaky morzeovky
for morseuvZnak  in znaky:
    abecedniZnak = "?"
    index = morseovyZnaky.index(morseuvZnak)
    if (index >= 0): # znak nalezen
        abecedniZnak = abecedniZnaky[index]
    zprava += abecedniZnak
print("Dekódovaná zpráva je: %s" % zprava)