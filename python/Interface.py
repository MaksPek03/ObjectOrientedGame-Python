import tkinter
from PIL import ImageTk
from World import World
from main_values import main_values
from tkinter import Label


class Interface:
    
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('900x1200')
        self.icon = [
            ImageTk.PhotoImage(file='C:/Users/maksp/Desktop/github/OOP/Project_3_python_193595/Project_3_python_193595/img/empty.png'),
            ImageTk.PhotoImage(file='C:/Users/maksp/Desktop/github/OOP/Project_3_python_193595/Project_3_python_193595/img/human.png'),
            ImageTk.PhotoImage(file='C:/Users/maksp/Desktop/github/OOP/Project_3_python_193595/Project_3_python_193595/img/sheep.png'),
            ImageTk.PhotoImage(file='C:/Users/maksp/Desktop/github/OOP/Project_3_python_193595/Project_3_python_193595/img/wolf.png'),
            ImageTk.PhotoImage(file='C:/Users/maksp/Desktop/github/OOP/Project_3_python_193595/Project_3_python_193595/img/fox.png'),
            ImageTk.PhotoImage(file='C:/Users/maksp/Desktop/github/OOP/Project_3_python_193595/Project_3_python_193595/img/turtle.png'),
            ImageTk.PhotoImage(file='C:/Users/maksp/Desktop/github/OOP/Project_3_python_193595/Project_3_python_193595/img/antelope.png'),
            ImageTk.PhotoImage(file='C:/Users/maksp/Desktop/github/OOP/Project_3_python_193595/Project_3_python_193595/img/cybersheep.png'),
            ImageTk.PhotoImage(file='C:/Users/maksp/Desktop/github/OOP/Project_3_python_193595/Project_3_python_193595/img/grass.png'),
            ImageTk.PhotoImage(file='C:/Users/maksp/Desktop/github/OOP/Project_3_python_193595/Project_3_python_193595/img/sowthistle.png'),
            ImageTk.PhotoImage(file='C:/Users/maksp/Desktop/github/OOP/Project_3_python_193595/Project_3_python_193595/img/guarana.png'),
            ImageTk.PhotoImage(file='C:/Users/maksp/Desktop/github/OOP/Project_3_python_193595/Project_3_python_193595/img/balledona.png'),
            ImageTk.PhotoImage(file='C:/Users/maksp/Desktop/github/OOP/Project_3_python_193595/Project_3_python_193595/img/sosnovskyshogweed.png')
        ]
        self.box = [
            [
                tkinter.Button(self.root, height=32, width=32, background='#fcfffd', image=self.icon[0])
                for y in range(main_values["height"])
            ] for x in range(main_values["width"])
        ]
        for y in range(main_values["height"]):
            for x in range(main_values["width"]):
                self.box[y][x].configure(command=(lambda a=y, b=x: self.wrld.addByClick(a, b)))
        self.boxmen = [
            tkinter.Button(self.root, height=32, width=32, background='#fcfffd', image=self.icon[i+2])
            for i in range(11)
        ]
        for i in range(11):
            self.boxmen[i].configure(command=(lambda a=i: self.wrld.selectedAnimalChange(a+2)))
        label_box = tkinter.Label(self.root, background='#fcfffd', text='Instruction:', font=('Arial', 12))
        label_box.place(x=600, y=150)
        label_box_1 = tkinter.Label(self.root, background='#fcfffd', text='Esc - quit game', font=('Arial', 12))
        label_box_1.place(x=600, y=180)
        label_box_2 = tkinter.Label(self.root, background='#fcfffd', text='s - save game', font=('Arial', 12))
        label_box_2.place(x=600, y=210)
        label_box_3 = tkinter.Label(self.root, background='#fcfffd', text='l - load game', font=('Arial', 12))
        label_box_3.place(x=600, y=240)
        label_box_3 = tkinter.Label(self.root, background='#fcfffd', text='a - special ability (immortality)', font=('Arial', 12))
        label_box_3.place(x=600, y=270)
        label_box_4 = tkinter.Label(self.root, background='#fcfffd', text='arrows - changing position', font=('Arial', 12))
        label_box_4.place(x=600, y=300)
        self.root.bind_all('<Key>', self.key)
        self.wrld = World()
        self.root.title('OOP 3rd project - s193595')
        self.wrld.mainLoop(self)

    def display(self, wrld):
        for y in range(main_values["height"]):
            for x in range(main_values["width"]):
                self.box[y][x].configure(image=self.icon[self.wrld.mapa[y][x]])
                self.box[y][x].grid(row=y, column=x)
        for i in range(11):
            self.boxmen[i].place(y=100, x=i*40+500)
        self.root.update()

    
    def key(self, event):
        if event.keysym == 'Escape':
            self.root.destroy()
            self.wrld.decisionChange(7)
        if event.keysym == 's':
            self.wrld.decisionChange(5)
        if event.keysym == 'l':
            self.wrld.decisionChange(6)
        if event.keysym == 'a':
            self.wrld.decisionChange(4)
        if event.keysym == 'Up':
            self.wrld.decisionChange(0)
        if event.keysym == 'Down':
            self.wrld.decisionChange(1)
        if event.keysym == 'Right':
            self.wrld.decisionChange(2)
        if event.keysym == 'Left':
            self.wrld.decisionChange(3)
