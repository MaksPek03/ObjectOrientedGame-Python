from Animal import Animal
from main_values import main_values
from random import randint


class Fox (Animal):
    def __init__(self, wrld, yy, xx, stre=3):
        self.y = yy
        self.x = xx
        self.py = self.y
        self.px = self.x
        self.appearance = 4
        self.state = True
        self.strength = stre
        self.initiative = 7
        wrld.mapChange(self.y, self.x, self.appearance)

    def birth(self, wrld, yy, xx):
        return Fox(wrld, yy, xx)

    def atos(self, m):
        if m == 1:
            return 5
        elif m == 2 or m == 6:
            return 4
        elif m == 3:
            return 9
        elif m == 4:
            return 3
        elif m == 5:
            return 2
        elif m == 7:
            return 11
        elif m == 11:
            return 99
        elif m == 12:
            return 10
        else:
            return 0

   
    def action(self, wrld, direction):
        self.py = self.y
        self.px = self.x
        d = [False, False, False, False]

        if self.y - 1 > 0:
            if self.atos(wrld.mapa[self.y - 1][self.x]) <= self.strength:
                d[0] = True
        if self.y + 1 < main_values["height"]:
            if self.atos(wrld.mapa[self.y + 1][self.x]) <= self.strength:
                d[1] = True
        if self.x + 1 < main_values["width"]:
            if self.atos(wrld.mapa[self.y][self.x + 1]) <= self.strength:
                d[2] = True
        if self.x - 1 > 0:
            if self.atos(wrld.mapa[self.y][self.x - 1]) <= self.strength:
                d[3] = True

        if d[0] or d[1] or d[2] or d[3]:
            while True:
                c = randint(0, 3)
                if c == 0 and d[0]:
                    self.y -= 1
                    break
                elif c == 1 and d[1]:
                    self.y += 1
                    break
                elif c == 2 and d[2]:
                    self.x += 1
                    break
                elif c == 3 and d[3]:
                    self.x -= 1
                    break

        wrld.mapChange(self.py, self.px, 0)
        wrld.mapChange(self.y, self.x, self.appearance)
        return 0
