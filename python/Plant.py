from Organism import Organism
from random import randint


class Plant(Organism):
    def __init__(self, wrld, yy, xx, stre):
        super().__init__(wrld, yy, xx, stre)

    def action(self, wrld, direction):
        c = randint(0, 9)
        if c == 0:
            return self.breed(wrld)
        return 0

    
    def collision(self, wrld, o, cn):
        if self.strength > o.S():
            o.die()
        if self.state:
            wrld.mapChange(self.y, self.x, self.appearance)
        return 0
