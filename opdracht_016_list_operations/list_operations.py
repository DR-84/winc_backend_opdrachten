
shane_embury = ["Shane Embury", ["bass", "backing vocals"], [1987, 2021]]
mark_greenway1 = ["Mark \"Barney\"Greenway",
                  "lead vocals",  [1989, 1996]]
mark_greenway2 = ["Mark \"Barney\"Greenway",
                  "lead vocals",  [1997, 2021]]
danny_herrera = ["Danny Herrera", "drums", [1991, 2021]]
mitch_harris = ["Mitch Harris", ["guitars, backing vocals"], [1990, 2014]]
nicholas_bullen = ["Nicholas \"Nik Napalm\" Bullen",
                   ["lead vocals", "bass"], [1981, 1986]]
miles_ratledge = ["Miles \"Rat\" Ratledge", "drums", [1981, 1985]]
simon_oppenheimer = ["Simon \"Si O\" Oppenheimer", "guitars", [1981, 1982]]
graham_robertson = ["Graham \"Grayhard\" Robertson",
                    ["guitars", "bass"], [1982, 1985]]
daryl_fedeski = ["Daryl \"Daz F\" Fedeski", "guitars", [1982, 1982]]
finbar_quinn = ["Finbar \"Fin\" Quinn", "bass", [1983, 1984]]
marian_williams = ["Marian Williams", "lead vocals", [1984, 1984]]
damien_errington = ["Damien Errington", "guitars", [1985, 1985]]
justin_broadrick = ["Justin Broadrick", [
    "guitars", "backing and lead vocals"], [1985, 1986]]
peter_shaw = ["Peter \"P-Nut\" Shaw", "bass", [1985, 1985]]
mick_harris = ["Mick Harris", ["drums", "backing vocals"], [1985, 1991]]
jim_whitely = ["Jim Whitely", "bass", [1986, 1987]]
frank_healy = ["Frank Healy", "guitars", [1986, 1986]]
bill_steer = ["Bill Steer", "guitars", [1987, 1989]]
lee_dorian = ["Lee Dorrian", "lead vocals", [1987, 1989]]
jesse_pintado = ["Jesse Pintado", "guitars",  [1989, 2004]]
phil_vane = ["Phil Vane", "lead vocals", [1996, 1997]]
erik_burke = ["Erik Burke", "guitars", [2015, 2015]]
jesper_liverod = ["Jesper Liveröd", "bass", [2017, 2017]]

all_members = [
    shane_embury, mark_greenway1, mark_greenway2, danny_herrera, mitch_harris, nicholas_bullen, miles_ratledge, simon_oppenheimer, graham_robertson, daryl_fedeski, finbar_quinn, marian_williams, damien_errington, justin_broadrick, peter_shaw, mick_harris, jim_whitely, frank_healy, bill_steer, lee_dorian, jesse_pintado, phil_vane, erik_burke, jesper_liverod]
year_to_check = 1984

for members in all_members:
    if(members[2][0] <= year_to_check and members[2][1] >= year_to_check):
        band = members
        print(band)


print("Het jaar is "+str(year_to_check)+'. ' + (band[0][0]) + " doet "+(band[0][1][0]) + " en " + (band[0][1][1])+", "+(band[1][0])+" op "
      + (band[1][1]) + ", " + (band[2][0]) + " op " + (band[2][1])+". ")

band = [nicholas_bullen, daryl_fedeski, graham_robertson, miles_ratledge]
year = 1982
print("Het jaar is "+str(year)+'. ' + (band[0][0]) + " doet "+(band[0][1][0]) + " en " + (band[0][1][1])+", "+(band[1][0])+" op "
      + (band[1][1]) + ", " + (band[2][0]) + " op " + (band[2][1][0]) + " en " + (band[2][1][1]) + ", " + (band[3][0]) + " op " + (band[3][1])+". ")

band = [nicholas_bullen, daryl_fedeski, finbar_quinn, miles_ratledge]
year = 1983
print("Het jaar is "+str(year)+'. ' + (band[0][0]) + " doet "+(band[0][1][0]) + ", "+(band[1][0])+" op "
      + (band[1][1]) + ", " + (band[2][0]) + " op " + (band[2][1]) + ", " + (band[3][0]) + " op " + (band[3][1])+". ")

band = [nicholas_bullen, daryl_fedeski, marian_williams, miles_ratledge]
year = 1984
print("Het jaar is "+str(year)+'. ' + (band[0][0]) + " doet "+(band[0][1][0]) + " en " + (band[0][1][1])+", "+(band[1][0])+" op "
      + (band[1][1]) + ", " + (band[2][0]) + " op " + (band[2][1]) + ", " + (band[3][0]) + " op " + (band[3][1])+". ")
