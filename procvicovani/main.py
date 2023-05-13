import datetime

now = datetime.datetime.now()

text1 = now.strftime("%H:%M:%S")
text2 = now.strftime("Hodin:%H, Minut:%M, Sekund:%S")

text3 = now.strftime("Den:%d, Měsíc:%m, Rok:%Y")

print(text1)
print(text2)
print(text3)