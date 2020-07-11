import random
import os
entry = input()
class entity(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def unrandom_color(self):
      return 'yello'
    def random_color(self,list_1):
        self.list_1 = list_1
        return random.choice(self.list_1)

    colors = ['White','Black','Green']
class properies(entity):
    def __init__(self, x, y):
        entity.__init__(self, x, y)
        self.game = True

    def toy(self):
        self.game = False
        print('Its a duck rubber')

    def walk(self, x):
        i = 0
        while i < self.x:
            i += 1
            print(i)

    def substration(self, duck):
        self.x = self.x - duck.x
# duck

class rubber_duck(properies):
    def message(self):
      #  self.walk(self.x)
        if self.game:
            return self.unrandom_color()
            return('This is a new game')
        else:
            return('Im sorry,but you duck is it a toy')
        
toys_ducks = rubber_duck(10, 20)
print (toys_ducks.message())
class real_duck(properies):
    os.system('clear')

    def duck(self, number):
      #  self.walk(self.x)
        if self.game:
            if self.x > 0:
                print('This duck is real and it :' + ' ' + str(self.x) + ' years old')
                return self.duck(self.substration(toys_ducks))
            else:
               # return self.random_color(entity.colors)
                return  toys_ducks.message()
                return 'Im sorry but you duck die'
        else:
            return (toys_ducks.message())


true_duck = real_duck(entry, 20)
print(true_duck.duck(true_duck.x))