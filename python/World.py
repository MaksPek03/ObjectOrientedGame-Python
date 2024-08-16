from main_values import main_values
from Human import Human
from Sheep import Sheep
from Wolf import Wolf
from Fox import Fox
from Turtle import Turtle
from Antelope import Antelope
from CyberSheep import CyberSheep
from Grass import Grass
from SowThistle import SowThistle
from Guarana import Guarana
from Balledona import Balledona
from SosnovskysHogweed import SosnovskysHogweed


class World:

    def addBeing(self, o):
        if o != 0:
            self.addNotification(o.A(), False)
            if len(self.organisms) == 0:
                self.organisms.append(o)
            else:
                for i in range(len(self.organisms)):
                    if self.organisms[i].I() < o.I():
                        self.organisms.insert(i, o)
                        break
                    elif i == len(self.organisms)-1:
                        self.organisms.append(o)
    
    def __init__(self):
        self.decision = 10
        self.selectedAnimal = 0
        self.humanAlive = True
        self.organisms = []
        self.mapa = [
            [0 for y in range(main_values["height"])] for x in range(main_values["width"])
        ]
        self.organisms.append(Human(self, 3, 3))
        self.addBeing(Wolf(self, 10, 1, 9))
        self.addBeing(Wolf(self, 12, 1, 9))
        self.addBeing(Antelope(self, 5, 5, 4))
        self.addBeing(Antelope(self, 11, 12, 4))
        self.addBeing(Antelope(self, 2, 12, 4))
        self.addBeing(Balledona(self, 7, 7, 99))
        self.addBeing(Fox(self, 8, 2, 3))
        self.addBeing(Fox(self, 12, 2, 3))
        self.addBeing(Fox(self, 1, 10, 3))
        self.addBeing(Grass(self, 4, 8, 0))
        self.addBeing(Grass(self, 6, 5, 0))
        self.addBeing(Guarana(self, 9, 1, 0))
        self.addBeing(Sheep(self, 9, 5, 4))
        self.addBeing(Sheep(self, 10,6, 4))
        self.addBeing(SosnovskysHogweed(self, 10, 10, 10))
        self.addBeing(SowThistle(self, 1, 1, 0))
        self.addBeing(Turtle(self, 8, 4, 2))
        self.addBeing(Turtle(self, 11, 4, 2))
        self.addBeing(Turtle(self, 2, 12, 2))
        self.addBeing(Turtle(self, 2, 5, 2))
        self.addBeing(Guarana(self, 1, 8, 0))

    def addNotification(self, appearance, happening):
        s = ""
        if appearance == 1:
            s += "Human "
        elif appearance == 2:
            s += "Sheep "
        elif appearance == 3:
            s += "Wolf  "
        elif appearance == 4:
            s += "Fox "
        elif appearance == 5:
            s += "Turtle "
        elif appearance == 6:
            s += "Antelope "
        elif appearance == 7:
            s += "Cyber Sheep "
        elif appearance == 8:
            s += "Grass "
        elif appearance == 9:
            s += "Sow Thistle "
        elif appearance == 10:
            s += "Guarana "
        elif appearance == 11:
            s += "Balledona "
        elif appearance == 12:
            s += "Sosnovskys Hogweed "
        else:
            s += "Organism"

        if happening:
            s += "died"
        elif appearance <= 7:
            s += "breeded"
        else:
            s += "sawed"

        print(s)


    def load(self):
        # returning to starting conditions
        self.organisms.clear()
        for y in range(main_values["height"]):
            for x in range(main_values["width"]):
                self.mapa[y][x] = 0
        self.humanAlive = True
        # file reading and adding organisms
        file = open("save.txt", "r")
        yy = 0
        xx = 0
        stre = 0
        abi = 0
        cnt = 0
        while True:
            line = file.readline()
            line2 = ""
            for i in range(len(line)):
                if line[i] != '\n':
                    line2 += line[i]
            line = line2
            if line == "--":
                break
            elif line == "-":
                self.addByClick(yy, xx, stre, True, abi)
                cnt = -1
            elif cnt == 0:
                self.selectedAnimal = int(line)
            elif cnt == 1:
                yy = int(line)
            elif cnt == 2:
                xx = int(line)
            elif cnt == 3:
                stre = int(line)
            elif cnt == 4:
                abi = int(line)
            cnt += 1
        file.close()
        # final touches
        self.decision = 10
        self.selectedAnimal = 0

    def save(self):
        file = open("save.txt", "w")
        for i in range(len(self.organisms)):
            print(self.organisms[i].save(), file=file)
        print("--", file=file)
        file.close()

    def mainLoop(self, Interface):
        while self.humanAlive:
            i = 0
            while i < len(self.organisms):
                if self.organisms[i].A() == main_values["human"]:
                    self.decision = 10
                    self.humanAlive = self.organisms[i].humanAlive()
                    Interface.display(self)
                    while self.decision > 4:
                        Interface.root.update()
                        if self.decision == 5:
                            self.save()
                            self.decision = 10
                        elif self.decision == 7 or self.decision == 6:
                            break
                    if self.decision == 7 or self.decision == 6:
                        break
                    else:
                        self.organisms[i].action(self, self.decision)
                # COMMON ORGANISM CASE
                elif self.organisms[i].alive():
                    if self.organisms[i].A() == main_values["sowthistle"]:
                        for k in [1, 2, 3]:
                            self.addBeing(self.organisms[i].action(self, 0))
                    else:
                        self.addBeing(self.organisms[i].action(self, 0))
                # COLLISION
                for j in range(len(self.organisms)):
                    if self.organisms[i].doCollide(self.organisms[j]):
                        self.addBeing(self.organisms[i].collision(self, self.organisms[j], True))
                # loop movement
                i += 1
            # REMOVING KILLED OBJECTS
            for i in sorted(range(len(self.organisms)), reverse=True):
                if self.organisms[i].A() != main_values["human"] and not self.organisms[i].alive():
                    self.addNotification(self.organisms[i].A(), True)
                    self.organisms.remove(self.organisms[i])
            # loading
            if self.decision == 6:
                self.load()
            # exiting
            elif self.decision == 7:
                break


    def decisionChange(self, d):
        self.decision = d

    def selectedAnimalChange(self, d):
        self.selectedAnimal = d

    def addByClick(self, yy, xx, stre=0, save=False, abi=0):
        if not self.selectedAnimal == 0:
            if self.selectedAnimal == 1:
                if not save:
                    stre = 5
                self.addBeing(Human(self, yy, xx, stre, abi))
            if self.selectedAnimal == 2:
                if not save:
                    stre = 4
                self.addBeing(Sheep(self, yy, xx, stre))
            if self.selectedAnimal == 3:
                if not save:
                    stre = 9
                self.addBeing(Wolf(self, yy, xx, stre))
            if self.selectedAnimal == 4:
                if not save:
                    stre = 3
                self.addBeing(Fox(self, yy, xx, stre))
            if self.selectedAnimal == 5:
                if not save:
                    stre = 2
                self.addBeing(Turtle(self, yy, xx, stre))
            if self.selectedAnimal == 6:
                if not save:
                    stre = 4
                self.addBeing(Antelope(self, yy, xx, stre))
            if self.selectedAnimal == 7:
                if not save:
                    stre = 11
                self.addBeing(CyberSheep(self, yy, xx, stre))
            if self.selectedAnimal == 8:
                if not save:
                    stre = 0
                self.addBeing(Grass(self, yy, xx, stre))
            if self.selectedAnimal == 9:
                if not save:
                    stre = 0
                self.addBeing(SowThistle(self, yy, xx, stre))
            if self.selectedAnimal == 10:
                if not save:
                    stre = 0
                self.addBeing(Guarana(self, yy, xx, stre))
            if self.selectedAnimal == 11:
                if not save:
                    stre = 99
                self.addBeing(Balledona(self, yy, xx, stre))
            if self.selectedAnimal == 12:
                if not save:
                    stre = 10
                self.addBeing(SosnovskysHogweed(self, yy, xx, stre))

    def mapChange(self, yy, xx, c):
        if 0 <= yy < main_values["height"] and 0 <= xx < main_values["width"]:
            self.mapa[yy][xx] = c
