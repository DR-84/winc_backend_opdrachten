import random

dice_amount = int(input("hoe many dice do you want to roll?: "))
dice_number = int(input("type your dice number here: "))
rolled_numbers = []
count = dice_amount
while count > 0:
    eyes = random.randint(1, dice_number)
    rolled_numbers.append({eyes})
    count -= 1
print(rolled_numbers)
