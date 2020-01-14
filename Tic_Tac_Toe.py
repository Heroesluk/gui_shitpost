from tkinter import *

turn_index = 1
game_state = []

root = Tk()
root.geometry("915x915")

main_frame = Frame(root)
main_frame.pack()


# IN GAME upon clicking any game board button
def action(button):
    global turn_index
    global game_state
    if button['text'] == 'D':
        if turn_index % 2 == 0:
            button['image'] = photo_X
            button['text'] = 'X'
        else:
            button['image'] = photo_O
            button['text'] = 'O'

        turn_index += 1

    game_state = [i['text'] for i in list_of_buttons]

    # Checking whether the winning conditions were met after clicking button
    def check(tab, i=0):
        for v in range(3):
            if tab[i] == tab[i + 1] == tab[i + 2] and tab[i] != 'D':
                finish(tab[i])
                return
            i += 3

        for v in range(3):
            if tab[v] == tab[v + 3] == tab[v + 6] and tab[v] != 'D':
                finish(tab[v])
                return

        if tab[4] != 'D':
            if tab[0] == tab[4] == tab[8] or tab[2] == tab[4] == tab[6]:
                finish(tab[4])
                return

        if 'D' not in tab:
            finish('remis')
            return

    check(game_state)


# Action that happens when you win the game
def finish(shape):
    top = Toplevel()
    top.title('GRATULACJE')

    if shape == 'X':
        shape = 'IKSA'
        text = Label(top, text=f'GRATULACJE GRACZ {shape} WYGRAL')
    elif shape == 'O':
        shape = 'KOLA'
        text = Label(top, text=f'GRATULACJE GRACZ {shape} WYGRAL')
    else:
        text = Label(top, text='GRA ZAKONCZYLA SIE REMISEM')

    text.config(font=("Courier", 48, 'bold'))
    text.grid(row=0, column=0)

    # recreating the game when you click the retry_button
    def retry():
        global turn_index
        global game_state
        for i in list_of_buttons:
            i['image'] = photo_def
            i['text'] = 'D'
            turn_index = 1
            game_state = []
            top.destroy()

    retry_button = Button(top, text='CZY CHCESZ ZAGRAC JESZCZE RAZ', command=lambda: retry())
    retry_button.grid(row=1, column=0)


# images
photo_O = PhotoImage(file='OBT.png')
photo_X = PhotoImage(file='XBT.png')
photo_def = PhotoImage(file='default.png')

# scheme - D stands for default, blank button, photon_def is default blank image
button_1 = Button(main_frame, text='D', image=photo_def, command=lambda: action(button_1))
button_2 = Button(main_frame, text='D', image=photo_def, command=lambda: action(button_2))
button_3 = Button(main_frame, text='D', image=photo_def, command=lambda: action(button_3))

button_4 = Button(main_frame, text='D', image=photo_def, command=lambda: action(button_4))
button_5 = Button(main_frame, text='D', image=photo_def, command=lambda: action(button_5))
button_6 = Button(main_frame, text='D', image=photo_def, command=lambda: action(button_6))

button_7 = Button(main_frame, text='D', image=photo_def, command=lambda: action(button_7))
button_8 = Button(main_frame, text='D', image=photo_def, command=lambda: action(button_8))
button_9 = Button(main_frame, text='D', image=photo_def, command=lambda: action(button_9))

list_of_buttons = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

# grid management
button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)

button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

root.mainloop()
