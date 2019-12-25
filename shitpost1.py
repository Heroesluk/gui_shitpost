from tkinter import *

turn_index = 1
game_state = []


def finish(shape):
    if shape == 'X':
        shape = 'IKSA'
    else:
        shape = 'KOLA'

    top = Toplevel()
    top.title('GRATULACJE')
    text = Label(top, text=f'GRATULACJE GRACZ {shape} WYGRAL')
    text.config(font=("Courier", 62))
    text.grid(row=0, column=0)

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

    game_state = []
    for i in list_of_buttons:
        game_state.append(i['text'])

    def check(tab):
        i = 0
        for v in range(3):
            if tab[i] == tab[i + 1] == tab[i + 2] and tab[i] != 'D':
                print('tak, poziomo')
                finish(tab[i])
                return
            i += 3

        for v in range(3):
            if tab[v] == tab[v + 3] == tab[v + 6] and tab[v] != 'D':
                print('tak, pionowo')
                finish(tab[v])
                return

    check(game_state)


root = Tk()
root.geometry("915x915")

main_frame = Frame(root)
main_frame.pack()

photo_O = PhotoImage(file='OBT.png')
photo_X = PhotoImage(file='XBT.png')
photo_def = PhotoImage(file='default.png')

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
