import random
for i in range(3):
    print(random.randint(1, 100))

members =['Abad','Piku','Tanu']
leader=random.choice(members)
print(leader)



class Dice:
    def roll(self):
      first_number = random.randint(1,6)
      second_number = random.randint(1,6)
      return first_number, second_number


dice = Dice()
print(dice.roll())