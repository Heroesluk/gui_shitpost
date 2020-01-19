from tkinter import *


class Game:
    turn_index = 1

    def __init__(self, *args):
        self.root = root
        self.root.title = 'dziala'
        self.root.geometry('915x915')

        self.game_state = []
        self.state = False

        self.photo_O = PhotoImage(file='OBT.png')
        self.photo_X = PhotoImage(file='XBT.png')
        self.photo_def = PhotoImage(file='default.png')

        self.game_frame = Frame(self.root)

        self.button0 = Button(self.game_frame, command=lambda: self.change(0))
        self.button1 = Button(self.game_frame, command=lambda: self.change(1))
        self.button2 = Button(self.game_frame , command=lambda: self.change(2))

        self.button3 = Button(self.game_frame, command=lambda: self.change(3))
        self.button4 = Button(self.game_frame, command=lambda: self.change(4))
        self.button5 = Button(self.game_frame, command=lambda: self.change(5))

        self.button6 = Button(self.game_frame, command=lambda: self.change(6))
        self.button7 = Button(self.game_frame, command=lambda: self.change(7))
        self.button8 = Button(self.game_frame, command=lambda: self.change(8))

        self.game_frame.pack(side='top', fill='both', expand=True)

        self.button_list = [self.button0, self.button1, self.button2, self.button3, self.button4, self.button5,
                            self.button6, self.button7, self.button8]

        for i in self.button_list:
            i['image'] = self.photo_def

        self.button0.grid(row=0, column=0)
        self.button1.grid(row=0, column=1)
        self.button2.grid(row=0, column=2)

        self.button3.grid(row=1, column=0)
        self.button4.grid(row=1, column=1)
        self.button5.grid(row=1, column=2)

        self.button6.grid(row=2, column=0)
        self.button7.grid(row=2, column=1)
        self.button8.grid(row=2, column=2)

    def change(self, index):
        if self.button_list[index]['image'] == 'pyimage3':

            if self.turn_index % 2 == 0:
                self.button_list[index]['image'] = self.photo_X
            else:
                self.button_list[index]['image'] = self.photo_O

            self.turn_index += 1
            self.check()

    def check(self):
        i = 0
        for v in range(3):
            if self.button_list[i]['image'] == self.button_list[i + 1]['image'] == self.button_list[i + 2]['image'] and \
                    self.button_list[i]['image'] != 'pyimage3':
                print('wygranko')
                self.win(True)
            i += 3

        for v in range(3):
            if self.button_list[v]['image'] == self.button_list[v + 3]['image'] == self.button_list[v + 6]['image'] and \
                    self.button_list[v]['image'] != 'pyimage3':
                print('wygranko2')
                self.win(True)


        if self.button_list[4]['image'] != 'pyimage3' and self.button_list[0]['image'] == self.button_list[4][
            'image'] == self.button_list[8]['image'] or \
                self.button_list[4]['image'] != 'pyimage3' and self.button_list[2]['image'] == self.button_list[4][
            'image'] == self.button_list[6]['image']:
            print('skos')
            self.win(False)

        if self.turn_index == 8:
            print('remis')

    def win(self, state):
        self.win_frame = Frame(self.root)
        self.won = Label(self.win_frame, text='wygrales')
        self.won.pack()
        self.win_frame.tkraise()
        self.win_frame.pack()









root = Tk()
game = Game(root)

print('tak')
#game.command()
root.mainloop()
print('dziala')

