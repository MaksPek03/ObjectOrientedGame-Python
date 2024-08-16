from Plant import Plant


class Balledona(Plant):
    def __init__(self, wrld, yy, xx, stre=99):
        super().__init__(wrld, yy, xx, stre)
        self.initiative = 0
        self.appearance = 11
        wrld.mapChange(self.y, self.x, self.appearance)

   
    def birth(self, wrld, yy, xx):
        return Balledona(wrld, yy, xx)

    def collision(self, wrld, o, cn):
        if self.strength > o.S():
            o.die()
        if not self.state:
            o.die()
            wrld.mapChange(self.y, self.x, 0)
        else:
            wrld.mapChange(self.y, self.x, self.appearance)
        return 0
