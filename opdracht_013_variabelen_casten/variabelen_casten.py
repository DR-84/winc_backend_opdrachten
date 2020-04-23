preiPrijs = 2
print("Prei kost " + str(preiPrijs) + " Euro per kilo")

bestelling = "prei 4"
prei_totaalprijs = int(
    bestelling[bestelling.find(' ')+1:])*preiPrijs
print(prei_totaalprijs)

broccoli_prijs = 2.34
bestelling_broccoli = "broccoli 1.6"
bestelling_broccoli_kg = bestelling_broccoli[bestelling_broccoli.find(' '):]
broccoli_totaalprijs = float(
    bestelling_broccoli_kg)*broccoli_prijs

print(bestelling_broccoli_kg + " kilo broccoli kost " +
      str(round(broccoli_totaalprijs, 2)) + " euro")
