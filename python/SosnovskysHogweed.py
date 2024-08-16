from Plant import Plant


class SosnovskysHogweed(Plant):
    def __init__(self, wrld, yy, xx, stre=10):
        super().__init__(wrld, yy, xx, stre)
        self.initiative = 0
        self.appearance = 12
        wrld.mapChange(self.y, self.x, self.appearance)
        self.yyy = [self.y-1, self.y+1, self.y, self.y]
        self.xxx = [self.x, self.x, self.x+1, self.x-1]

    def birth(self, wrld, yy, xx):
        return SosnovskysHogweed(wrld, yy, xx)

    def doCollide(self, o):
        if self != o and o.alive() and self.alive():
            yo = o.Y()
            xo = o.X()
            if yo == self.y and xo == self.x:
                return True
            elif yo == self.yyy[0] and xo == self.xxx[0]:
                return True
            elif yo == self.yyy[1] and xo == self.xxx[1]:
                return True
            elif yo == self.yyy[2] and xo == self.xxx[2]:
                return True
            elif yo == self.yyy[3] and xo == self.xxx[3]:
                return True
            else:
                return False
        else:
            return False

    
    def collision(self, wrld, o, cn):
        if o.A() < 7:
            o.die()
        if self.state:
            wrld.mapChange(self.y, self.x, self.appearance)
        return 0
