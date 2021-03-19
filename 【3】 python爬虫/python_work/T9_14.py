from random import randint 

class Die():
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        i = 1
        while i <= 10:
            x = randint(1,self.sides)
            print(str(i) + " : "+ str(x) +'\n')
            i+=1

my_sides = Die(6)
print(str(my_sides.sides) + " sides.\n")
my_sides.roll_die()

my_sides = Die(10)
print(str(my_sides.sides) + " sides.\n")
my_sides.roll_die()

my_sides = Die(20)
print(str(my_sides.sides) + " sides.\n")
my_sides.roll_die()