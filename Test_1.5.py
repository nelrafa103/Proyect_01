entry = input()
import os

class properies(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
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
        self.toy()
        self.walk(self.x)
        if self.game:
            print('This is a new game')
        else:
            print('Im sorry,but you duck is it a toy')
            print(self.color)


toys_ducks = rubber_duck(30, 20, 9)


class real_duck(properies):
    os.system('clear')
    def duck(self,number):
        if self.game :
            if self.x > 0:
             print ('This duck is real' + 'and' + 'its' + ' ' + str(self.x))
             return self.duck(self.substration(toys_ducks))
            else:
             return 'Im sorry but you duck die'
        else:
            return (toys_ducks.message())

true_duck = real_duck(int(entry), 20, entry)
print(true_duck.duck(true_duck.x))
