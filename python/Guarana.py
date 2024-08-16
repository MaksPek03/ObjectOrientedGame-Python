from Plant import Plant


class Guarana(Plant):
    def __init__(self, wrld, yy, xx, stre=0):
        super().__init__(wrld, yy, xx, stre)
        self.initiative = 0
        self.appearance = 10
        wrld.mapChange(self.y, self.x, self.appearance)

    
    def birth(self, wrld, yy, xx):
        return Guarana(wrld, yy, xx)

    def collision(self, wrld, o, cn):
        if self.strength > o.S():
            o.die()
        if not self.state:
            o.upgradeS()
            o.upgradeS()
            o.upgradeS()
        else:
            wrld.mapChange(self.y, self.x, self.appearance)
        return 0
