from tkinter import *


class Root:
    def __init__(self, root):
        self.root = root
        self.root.title = 'dziala'
        self.root.geometry('915x915')

        self.turn_index = 1
        self.game_state = []

        self.main_frame = Frame(root)
        self.main_frame.pack()

        self.photo_O = PhotoImage(file='OBT.png')
        self.photo_X = PhotoImage(file='XBT.png')
        self.photo_def = PhotoImage(file='default.png')


        self.button_1 = Button(self.main_frame, text='D', image=self.photo_def, command=lambda: action(self.button_1))
        self.button_2 = Button(self.main_frame, text='D', image=self.photo_def, command=lambda: action(self.button_2))
        self.button_3 = Button(self.main_frame, text='D', image=self.photo_def, command=lambda: action(self.button_3))

        self.button_4 = Button(self.main_frame, text='D', image=self.photo_def, command=lambda: action(self.button_4))
        self.button_5 = Button(self.main_frame, text='D', image=self.photo_def, command=lambda: action(self.button_5,))
        self.button_6 = Button(self.main_frame, text='D', image=self.photo_def, command=lambda: action(self.button_6,))

        self.button_7 = Button(self.main_frame, text='D', image=self.photo_def, command=lambda: action(self.button_7,))
        self.button_8 = Button(self.main_frame, text='D', image=self.photo_def, command=lambda: action(self.button_8,))
        self.button_9 = Button(self.main_frame, text='D', image=self.photo_def, command=lambda: action(self.button_9,))

        list_of_buttons = [self.button_1, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6, self.button_7, self.button_8, self.button_9]

        # grid management
        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)

        self.button_4.grid(row=1, column=0)
        self. button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)

        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)

        def finish(shape):
            print(shape)
            top = Toplevel()



        def action(button):
            if button['text'] == 'D':
                if self.turn_index % 2 == 0:
                    button['image'] = self.photo_X
                    button['text'] = 'X'
                else:
                    button['image'] = self.photo_O
                    button['text'] = 'O'

                self.turn_index += 1

            game_state = [i['text'] for i in list_of_buttons]
            print(game_state)

            def check(tab, i=0):
                for v in range(3):
                    if tab[i] == tab[i + 1] == tab[i + 2] and tab[i] != 'D':
                        c = tab[i]
                        finish(c)
                    i += 3

                for v in range(3):
                    if tab[v] == tab[v + 3] == tab[v + 6] and tab[v] != 'D':
                        finish(tab[v])

                if tab[4] != 'D':
                    if tab[0] == tab[4] == tab[8] or tab[2] == tab[4] == tab[6]:
                        finish(tab[4])

                if 'D' not in tab:
                    finish('remis')

            check(game_state)






Master = Tk()
main_window = Root(Master)
Master.mainloop()


