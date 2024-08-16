from main_values import main_values
from random import randint


class Organism:
    def __init__(self, wrld, yy, xx, stre):
        self.strength = stre
        self.initiative = 0
        self.y = yy
        self.x = xx
        self.appearance = 0
        self.state = True

    def action(self, wrld, direction):
        pass
    def collision(self, wrld, o, cn):
        pass
    def birth(self, wrld, yy, xx):
        pass

    def S(self):
        return self.strength
    def I(self):
        return self.initiative
    def A(self):
        return self.appearance
    def Y(self):
        return self.y
    def X(self):
        return self.x
    def alive(self):
        return self.state
    def die(self):
        self.state = False
    def upgradeS(self):
        self.strength += 1

    def doCollide(self, o):
        if self != o and self.X() == o.X() and self.Y() == o.Y() and o.alive() and self.alive():
            return True
        else:
            return False

    def save(self):
        s = ""
        if self.state:
            s += str(self.appearance) + "\n"
            s += str(self.y) + "\n"
            s += str(self.x) + "\n"
            s += str(self.strength) + "\n"
            s += "-"
        return s

    
    def breed(self, wrld):
        if 0 <= self.y < main_values["height"] and 0 <= self.x < main_values["width"]:
            d = [False, False, False, False]
            kiddoY = self.y
            kiddoX = self.x

            if self.y - 1 >= 0:
                if wrld.mapa[self.y - 1][self.x] == 0:
                    d[0] = True
            if self.y + 1 < main_values["height"]:
                if wrld.mapa[self.y + 1][self.x] == 0:
                    d[1] = True
            if self.x + 1 < main_values["width"]:
                if wrld.mapa[self.y][self.x + 1] == 0:
                    d[2] = True
            if self.x - 1 >= 0:
                if wrld.mapa[self.y][self.x - 1] == 0:
                    d[3] = True

            if d[0] or d[1] or d[2] or d[3]:
                while True:
                    c = randint(0, 3)
                    if c == 0 and d[0]:
                        kiddoY -= 1
                        break
                    elif c == 1 and d[1]:
                        kiddoY += 1
                        break
                    elif c == 2 and d[2]:
                        kiddoX += 1
                        break
                    elif c == 3 and d[3]:
                        kiddoX -= 1
                        break
                return self.birth(wrld, kiddoY, kiddoX)
        return 0
