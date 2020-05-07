lst1 = [1, 2, 3]
lst2 = lst1
lst1[1] = 6
result = lst1[1] + lst2[1]
print(result)
# Wat is de waarde van result?
# Antwoord: result = 12
# En waarom is dat de waarde van result?
# Antwoord: list2 is list1, dan list1 tweede value aangepast naar 6,
# tel lijst[1] bij elkaar op is 12.


dict1 = {"a": 1, "b": 2}
dict2 = dict1
dict1["a"] = 8
result = dict1["a"] + dict2["a"]
print(result)
# Wat is de waarde van result?
# Antwoord: result = 16
# En waarom is dat de waarde van result?
# Antwoord: 8 + 8

lst3 = [{"c": 3, "d": 4}, {"c": 5, "d": 6}]
lst4 = lst3
lst3[0]["c"] = 7
result = 0
for lst in [lst3, lst4]:
    for dct in lst:
        for val in dct.values():
            result += val
            print(result)
# Wat is de waarde van result?
# Antwoord: result = 44 of 11,22,33,44 of 7,11,16,22,29,33,38,44 (ligt aan de plek van je print() )
# En waarom is dat de waarde van result?
# Antwoord: Je past lst3 eerste item in eerste dict aan naar 7.
# de rest blijft het zelfde en dan voor elke value in de dicts in de lists
# tel je bij result op
