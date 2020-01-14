from tkinter import *

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title = 'dziala'
        self.root.geometry('915x915')

        self.turn_index = 1
        self.game_state = []

        self.t1 = StringVar()
        self.t1.set('XD')

        self.t2= StringVar()
        self.t2.set('XDD')

        self.StrVarList = [self.t1,self.t2]

        self.button = Button(self.root, textvariable=self.t1, command=lambda: self.change(0))
        self.button.pack()

        self.button2 = Button(self.root, textvariable=self.t2, command=lambda: self.change(1))
        self.button2.pack()



    def change(self, index):
        self.StrVarList[index].set('tak')




















root = Tk()
game = Game(root)

#game.command()
root.mainloop()
