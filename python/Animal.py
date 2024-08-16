from main_values import main_values
from Organism import Organism
from random import randint


class Animal(Organism):
    def __init__(self, wrld, yy, xx, stre):
        super().__init__(wrld, yy, xx, stre)
        self.py = self.y
        self.px = self.x

   
    def action(self, wrld, direction):
        self.py = self.y
        self.px = self.x
        while True:
            c = randint(0, 3)
            if c == 0 and self.y-1 >= 0:
                self.y -= 1
                break
            if c == 1 and self.y+1 < main_values["height"]:
                self.y += 1
                break
            if c == 2 and self.x+1 < main_values["width"]:
                self.x += 1
                break
            if c == 3 and self.x-1 >= 0:
                self.x -= 1
                break
        wrld.mapChange(self.py, self.px, 0)
        wrld.mapChange(self.y, self.x, self.appearance)
        return 0

    def moveBack(self, wrld):
        wrld.mapChange(self.py, self.px, self.appearance)
        self.x = self.px
        self.y = self.py

    def collision(self, wrld, o, cn):
        if self.appearance == o.A():
            self.moveBack(wrld)
            return self.breed(wrld)
        elif self.strength > o.S() or (self.strength == o.S() and cn):
            o.die()
        if cn:
            o.collision(wrld, self, False)
        if self.state:
            wrld.mapChange(self.y, self.x, self.appearance)
        return 0
