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


apple = Fruit("appel", 100)
pear = Fruit("pear", 75)
watermellon = Fruit("watermellon", 1600)
apple.weight = 200

print(apple.description())
print(pear.description())
print(watermellon.description())
