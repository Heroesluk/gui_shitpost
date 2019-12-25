tab = [2, 2, 2,
       2, 1, 2,
       2, 2, 1]






def check(tab):
    i = 0
    for v in range(3):
        if tab[i] == tab[i + 1] == tab[i + 2]:
            print('tak, poziomo')
            return


        i += 3

    for v in range(3):
        if tab[v] == tab[v+3] == tab[v+6]:
            print('tak, pionowo')
            return

check(tab)