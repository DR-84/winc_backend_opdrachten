hans = "Hans van Breukelen"
print(hans)
berry = "Berry van Aerle"
print(berry)
frank = "Frank Rijkaard"
print(frank)
ronald = "Ronald Koeman"
print(ronald)
adri = "Adri van Tiggelen"
print(adri)
gerald = "Gerald Vanenburg"
print(gerald)
arnold = "Arnold Mühren"
print(arnold)
jan = "Jan Wouters"
print(jan)
erwin = "Erwin Koeman"
print(erwin)
marco = "Marco van Basten"
print(marco)
ruud = "Ruud Gullit"
print(ruud)
joop = "Joop Hiele"
print(joop)
wilbert = "Wilbert Suvrijn"
print(wilbert)
johnS = "John van 't Schip"
print(johnS)
johnB = "John Bosman"
print(johnB)
wim = "Wim Kieft"
print(wim)

eersteDoelpuntMinuut = 35
print(eersteDoelpuntMinuut)
tweedeDoelpuntMinuut = 54
print(tweedeDoelpuntMinuut)

eersteDoelpuntSpeler = (
    ruud + " scoorde in de " + str(eersteDoelpuntMinuut) + "e minuut."
)
print(eersteDoelpuntSpeler)

tweedeDoelpuntSpeler = (
    marco + " scoorde in de " + str(tweedeDoelpuntMinuut) + "e minuut."
)
print(tweedeDoelpuntSpeler)

print(hans)
hans_achternaam_eerst = hans[hans.find(" ") + 1 :] + ", " + hans[0 : hans.find(" ")]
print(hans_achternaam_eerst)

hans_voornaam = hans[0 : hans.find(" ")]
print(hans_voornaam)

hans_achternaam_lengte = len(hans[hans.find(" ") + 1 :])
print(hans_achternaam_lengte)

hans_voorletter_plus_achternaam = hans[0:1] + "." + hans[hans.find(" ") :]
print(hans_voorletter_plus_achternaam)

hans_aanmoedigen = (
    len(hans[0 : hans.find(" ")]) * (hans[0 : hans.find(" ")] + "! ")
).strip(" ")

print(hans_aanmoedigen)

hans_is_there_a_endspace = hans_aanmoedigen[-1] == " "
print(hans_is_there_a_endspace)
