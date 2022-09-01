import random

Endurance = 0
CR = 0

Luck = 0

Endurance = random.randint(5,50)
CR = random.randint(5, 25)
Luck = random.randint(5, 15)
print("Your charcater's stats are as follows: \n")
print("\Endurance:", Endurance)
print("Combat Rating:", CR)
print("Luck", Luck)