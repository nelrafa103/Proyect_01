import random
import os
entry = input('Introduce a number :')
#entry_2 = str(input('Introduce a color :'))


class entity(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def unrandom_color(self):
        return self.color

    def random_color(self):
        return random.choice(self.color)


class properies(entity):
    def __init__(self, x, y, color):
        entity.__init__(self, x, y, color)
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
        self.favorite_number = 25
        print(self.favorite_number)
        if self.game:
            return self.unrandom_color()
            return('This is a new game')
        else:
            return('Im sorry,but you duck is it a toy')


toys_ducks = rubber_duck(10, 20, 'yellow')
print (toys_ducks.message())


class real_duck(properies):
    os.system('clear')
    favorite_number = 24

    def duck(self, number):
        #  self.walk(self.x)
        if self.game:
            if self.x > 0:
                print('This duck is real and it :' +
                      ' ' + str(self.x) + ' years old')
                return self.duck(self.substration(toys_ducks))
            else:
               # return self.random_color(entity.colors)
                return self.random_color()
                return 'Im sorry but you duck die'
        else:
            return (toys_ducks.message())


true_duck = real_duck(entry, 20, ['White', 'Black', 'Green'])
true_duck_2 = real_duck(50, 50, ['White', 'Grey', 'Blue'])
print(true_duck.duck(true_duck.x))
print(true_duck_2.duck(true_duck_2.x))
print (true_duck_2.favorite_number)
