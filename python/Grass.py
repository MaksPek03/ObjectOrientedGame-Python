from Plant import Plant


class Grass(Plant):
    def __init__(self, wrld, yy, xx, stre=0):
        super().__init__(wrld, yy, xx, stre)
        self.initiative = 0
        self.appearance = 8
        wrld.mapChange(self.y, self.x, self.appearance)

    
    def birth(self, wrld, yy, xx):
        return Grass(wrld, yy, xx)
