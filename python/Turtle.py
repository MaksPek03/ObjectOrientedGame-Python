from Animal import Animal
from main_values import main_values
from random import randint


class Turtle (Animal):
    def __init__(self, wrld, yy, xx, stre=2):
        self.y = yy
        self.x = xx
        self.py = self.y
        self.px = self.x
        self.appearance = 5
        self.state = True
        self.strength = stre
        self.initiative = 1
        wrld.mapChange(self.y, self.x, self.appearance)

    def birth(self, wrld, yy, xx):
        return Turtle(wrld, yy, xx)

    def action(self, wrld, decision):
        c = randint(0, 3)
        if c == 0:
            self.py = self.y
            self.px = self.x
            while True:
                c = randint(0, 3)
                if c == 1 and self.y-1 >= 0:
                    self.y -= 1
                    break
                if c == 2 and self.y+1 < main_values["height"]:
                    self.y += 1
                    break
                if c == 3 and self.x+1 < main_values["width"]:
                    self.x += 1
                    break
                if c == 4 and self.x-1 >= 0:
                    self.x -= 1
                    break
            wrld.mapChange(self.py, self.px, 0)
            wrld.mapChange(self.y, self.x, self.appearance)
        return 0

   
    def collision(self, wrld, o, cn):
        if o.A() <= 7:
            if self.appearance == o.A():
                self.moveBack(wrld)
                return self.breed(wrld)
            elif o.S() < 5 and not cn:
                self.state = True
                o.moveBack(wrld)
            elif self.strength > o.S() or (self.strength == o.S() and cn):
                o.die()
        elif self.strength > o.S() or (self.strength == o.S() and cn):
            o.die()
        if cn:
            o.collision(wrld, self, False)
        if self.state:
            wrld.mapChange(self.y, self.x, self.appearance)
        return 0
