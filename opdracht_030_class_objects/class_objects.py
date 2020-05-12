class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def description(self):
        vowels = ["a", "e", "i", "o", "u"]
        if self.name[0].lower() in vowels:
            return "an {} weighs {} gram.".format(self.name, self.weight)
        else:
            return "a {} weighs {} gram.".format(self.name, self.weight)


fruit_object_list = [Fruit("appel", 100), Fruit("pear", 75), Fruit("watermellon", 1600)]

# apple.weight = 200

# print(apple.description())
# print(pear.description())
# print(watermellon.description())


def print_object_list(list):
    for i in list:
        print(i.description())


print_object_list(fruit_object_list)
