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
daytime = False
cows_are_out = False
too_windy = False
poop_overload = False
got_milk = False
got_pumpkin_spice = True

get_cows_inside = 'haal de koeien naar binnen'
milk_the_cows = 'melk de koeien'
cows_can_stay_out = 'koeien kunnen naar buiten'
fertilize_the_land = 'bemest het land'
mow_the_lawn = 'maai het gras voor hooi'

# Als de koeien gemolken moeten worden dan moeten ze naar binnen gehaald worden en vervolgens gemolken.
if cows_are_out and got_milk:
    print(get_cows_inside + ' & ' + milk_the_cows+'.')
elif not cows_are_out and got_milk:
    print(milk_the_cows)
else:
    print(cows_can_stay_out)

# Als de koeien 's nachts op het weiland staan en het regent dan moeten ze naar binnen gehaald worden.
if cows_are_out and rain and not daytime:
    print(get_cows_inside)
else:
    print(cows_can_stay_out)

# Als de koeien op het weiland staan en er staat veel wind dan moeten ze binnen gehaald worden, als ze ook nog gemolken moeten worden, doe dat dan vervolgens.
if cows_are_out and too_windy and not got_milk:
    print(get_cows_inside)
elif cows_are_out and too_windy and got_milk:
    print(get_cows_inside + ' & ' + milk_the_cows+'.')
else:
    print(cows_can_stay_out)

# Als de gierput vol en het regent moet het land bemest worden. Denk aan de koeien.
if poop_overload and rain and cows_are_out:
    print(get_cows_inside + ' & ' + fertilize_the_land)
elif poop_overload and rain and not cows_are_out:
    print(fertilize_the_land)
else:
    print(cows_can_stay_out)

# Als het herfst is en de zon schijnt moet het gras gemaaid worden. Denk aan de koeien.
if sun and got_pumpkin_spice and not cows_are_out:
    print(mow_the_lawn)
elif sun and got_pumpkin_spice and cows_are_out:
    print(get_cows_inside + ' & ' + mow_the_lawn)
else:
    print(cows_can_stay_out)

# Als het herfst is en de zon schijnt moeten de koeien naar buiten, tenzij ze al buiten zijn.
if sun and got_pumpkin_spice and not cows_are_out:
    print(cows_can_stay_out)
else:
    print(get_cows_inside)
