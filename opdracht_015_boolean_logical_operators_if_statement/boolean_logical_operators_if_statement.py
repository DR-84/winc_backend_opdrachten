""" **Factoren**

- regen
- zonneschijn
- het is overdag
- de koeien zijn op het weiland
- er staat veel wind
- de gierput is vol
- de koeien moeten gemolken worden
- het is herfst

**Acties**

- haal de koeien naar binnen
- melk de koeien
- bemest het land
- maai het gras voor hooi """

rain = False
sun = True
daytime = True
cows_are_out = True
too_windy = True
poop_overload = True
got_milk = True
got_pumpkin_spice = True

get_cows_inside = 'haal de koeien naar binnen'
milk_the_cows = 'melk de koeien'
cows_can_stay_out = 'koeien kunnen buiten blijven'


# Als de koeien gemolken moeten worden dan moeten ze naar binnen gehaald worden en vervolgens gemolken.
if cows_are_out and got_milk == True:
    print(get_cows_inside + ' & ' + milk_the_cows+'.')
elif cows_are_out == False and got_milk == True:
    print(milk_the_cows)
else:
    print(cows_can_stay_out)

# Als de koeien 's nachts op het weiland staan en het regent dan moeten ze naar binnen gehaald worden.
if cows_are_out and rain == True and daytime == False:
    print(get_cows_inside)
else:
    print(cows_can_stay_out)

# Als de koeien op het weiland staan en er staat veel wind dan moeten ze binnen gehaald worden, als ze ook nog gemolken moeten worden, doe dat dan vervolgens.
if cows_are_out and too_windy == True and got_milk == False:
    print(get_cows_inside)
elif cows_are_out and too_windy and got_milk == True:
    print(get_cows_inside + ' & ' + milk_the_cows+'.')
else:
    print(cows_can_stay_out)

# Als de gierput vol en het regent moet het land bemest worden. Denk aan de koeien.
if
