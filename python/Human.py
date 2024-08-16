from Animal import Animal
from main_values import main_values


class Human(Animal):
    def __init__(self, wrld, yy, xx, stre=5, abi=0):
        self.strength = stre
        self.initiative = 4
        self.y = yy
        self.x = xx
        self.appearance = 1
        self.state = True
        self.py = self.y
        self.px = self.x
        self.ability = abi
        self.escape = 0
        wrld.mapChange(self.y, self.x, self.appearance)

    def humanAlive(self):
        if self.state or self.ability > 0:
            return True
        else:
            return False

    def save(self):
        s = ""
        s += str(self.appearance) + "\n"
        s += str(self.y) + "\n"
        s += str(self.x) + "\n"
        s += str(self.strength) + "\n"
        s += str(self.ability) + "\n"
        s += "-"
        return s

    def action(self, wrld, direction):
        if self.ability > 0:
            self.state = True
        if self.state:
            self.py = self.y
            self.px = self.x
            if direction == 0 and self.y-1 >= 0:
                self.y -= 1
            if direction == 1 and self.y+1 < main_values["height"]:
                self.y += 1
            if direction == 2 and self.x+1 < main_values["width"]:
                self.x += 1
            if direction == 3 and self.x-1 >= 0:
                self.x -= 1
            
            if direction == 4:
                self.ability = 6

            if self.ability > 0:
                self.ability -= 1
            wrld.mapChange(self.py, self.px, 0)
            wrld.mapChange(self.y, self.x, self.appearance)
        else:
            wrld.mapChange(self.y, self.x, 0)
        return 0

    
    def collision(self, wrld, o, cn):
        # setting new escape route
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
        if self.strength > o.S() or (self.strength == o.S() and cn):
            o.die()
        elif self.ability > 0 and self.escape > 0:
            # escaping
            wrld.mapChange(self.y, self.x, o.A())
            if self.escape == 1:
                self.y -= 1
            if self.escape == 2:
                self.y += 1
            if self.escape == 3:
                self.x += 1
            if self.escape == 4:
                self.x -= 1
            self.state = True
            cn = False
            wrld.mapChange(self.y, self.x, self.appearance)
        elif self.ability > 0 and self.escape == 0:
            self.state = True
            if cn:
                self.moveBack(wrld)
            else:
                o.moveBack(wrld)
                wrld.mapChange(self.y, self.x, self.appearance)
        if cn:
            o.collision(wrld, self, False)
        if self.state:
            wrld.mapChange(self.y, self.x, self.appearance)
        return 0
