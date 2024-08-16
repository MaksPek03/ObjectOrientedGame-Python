from Animal import Animal
from main_values import main_values
from random import randint


class Antelope (Animal):
    def __init__(self, wrld, yy, xx, stre=4):
        self.strength = stre
        self.initiative = 4
        self.y = yy
        self.x = xx
        self.appearance = 6
        self.state = True
        self.py = self.y
        self.px = self.x
        self.escape = 0
        wrld.mapChange(self.y, self.x, self.appearance)

    def birth(self, wrld, yy, xx):
        return Antelope(wrld, yy, xx)

    def action_one(self, wrld, cameFrom):
        if cameFrom == 0:
            cameFrom = 1
        elif cameFrom == 1:
            cameFrom = 0
        elif cameFrom == 2:
            cameFrom = 3
        elif cameFrom == 3:
            cameFrom = 2
        while True:
            c = randint(0, 3)
            if c != cameFrom:
                if c == 0 and self.y-1 >= 0:
                    self.y -= 1
                    break
                elif c == 1 and self.y+1 < main_values["height"]:
                    self.y += 1
                    break
                elif c == 2 and self.x+1 < main_values["width"]:
                    self.x += 1
                    break
                elif c == 3 and self.x-1 >= 0:
                    self.x -= 1
                    break
        return c

    
    def action(self, wrld, direction):
        self.py = self.y
        self.px = self.x
        self.action_one(wrld, self.action_one(wrld, 4))
        wrld.mapChange(self.py, self.px, 0)
        wrld.mapChange(self.y, self.x, self.appearance)
        return 0

    def collision(self, wrld, o, cn):
        # setting new escape route
        c = randint(0, 1)
        self.escape = 0
        if self.y - 1 >= 0 and wrld.mapa[self.y - 1][self.x] == 0:
            self.escape = 1
        elif self.y + 1 < main_values["height"] and wrld.mapa[self.y + 1][self.x] == 0:
            self.escape = 2
        elif self.x + 1 < main_values["width"] and wrld.mapa[self.y][self.x + 1] == 0:
            self.escape = 3
        elif self.x - 1 >= 0 and wrld.mapa[self.y][self.x - 1] == 0:
            self.escape = 4
        else:
            self.escape = 0
        # collision
        if self.appearance == o.A():
            self.moveBack(wrld)
            return self.breed(wrld)
        elif c > 0 and self.escape > 0:
            wrld.mapChange(self.y, self.x, o.A())
            if self.escape == 1:
                self.y -= 1
            elif self.escape == 2:
                self.y += 1
            elif self.escape == 3:
                self.x += 1
            elif self.escape == 4:
                self.x -= 1
            self.escape = 0
            self.state = True
            cn = False
        elif self.strength > o.S() or (self.strength == o.S() and cn):
            o.die()
        if cn:
            o.collision(wrld, self, False)
        if self.state:
            wrld.mapChange(self.y, self.x, self.appearance)
        return 0
