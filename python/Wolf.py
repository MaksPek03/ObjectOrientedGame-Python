from Animal import Animal


class Wolf (Animal):
    def __init__(self, wrld, yy, xx, stre=9):
        self.y = yy
        self.x = xx
        self.py = self.y
        self.px = self.x
        self.appearance = 3
        self.state = True
        self.strength = stre
        self.initiative = 5
        wrld.mapChange(self.y, self.x, self.appearance)

    
    def birth(self, wrld, yy, xx):
        return Wolf(wrld, yy, xx)
