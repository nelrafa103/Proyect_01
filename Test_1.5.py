entry = input()

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

#duck
class rubber_duck(properies):
    def message(self):
        self.toy()
        self.walk(self.x)
        if self.game:
            print('This is a new game')
        else:
            print('Im sorry,but you duck is it a toy')
        print(self.color)


#class real_duck(properies)
# def duck(self):
# if
d = rubber_duck(30, 20, entry)
d.message()
