from Animal import Animal


class Sheep (Animal):
    def __init__(self, wrld, yy, xx, stre=4):
        self.y = yy
        self.x = xx
        self.py = self.y
        self.px = self.x
        self.appearance = 2
        self.state = True
        self.strength = stre
        self.initiative = 4
        wrld.mapChange(self.y, self.x, self.appearance)

    
    def birth(self, wrld, yy, xx):
        return Sheep(wrld, yy, xx)
