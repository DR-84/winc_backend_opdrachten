""" 1. maak 3 variabelen, elke variabele naam is de naam van een product uit de supermarkt, elk product heeft een prijs in hele euro's. Voorbeeld: `broccoli = 2` / OK
2. tel de producten bij elkaar op, stop de nieuwe waarde in een variabele / OK
3. bereken de gemiddelde prijs van de producten / OK
    1. rond dit getal af tot 2 cijfers achter de komma / OK
    2. stop het resultaat in een variabele / OK
4. maak voor elk product een "aantal" variabele aan: `aantalBroccoli = 5` / OK
5. bereken de totaalprijs en stop die in een variabele / OK
6. maak een variabele `kortingPercentage` (dus tussen 0 en 100) / OK
7. bereken de totaalprijs, met korting, tot 2 cijfers achter de komma. Denk goed na over de volgorde van korting eraf halen en afronden. / OK
 """

kaas = 4  # kaas in pieces
worst = 3  # worst in pieces
sixpackAmstelRadlerNulProcentGrapefruit = 6  # sixpacks contains 6 bottles

aantalKaas = 11
aantalWorst = 7
aantalSixpackAmstelRadlerNulProcentGrapefruit = 4

kortingsPercentage = 35

boodskapjesLijst = kaas + worst + sixpackAmstelRadlerNulProcentGrapefruit
prijsGemiddeldTweecijfers = round(boodskapjesLijst / 3, 2)
print(prijsGemiddeldTweecijfers)

# total value of groceries
totaalBoodskapjes = (aantalKaas * kaas) + (aantalWorst * worst) + (
    aantalSixpackAmstelRadlerNulProcentGrapefruit*aantalSixpackAmstelRadlerNulProcentGrapefruit)
print(totaalBoodskapjes)

# calculate the total amount of discount
totaalBoodskapjesKorting = totaalBoodskapjes * ((100 - kortingsPercentage)/100)
print(totaalBoodskapjesKorting)

""" see above """
