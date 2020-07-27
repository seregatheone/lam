from tkinter import *

from PIL import Image

col = 0


def res():
#    amo / col
    vroot = Tk()
    vroot.geometry("400x100")
    label = Label(vroot, text="Пикселей на бота : ")
    label.place(relx=.4, rely=.5, anchor="c")

    vabel = Label(vroot, text=str(amo / col))
    vabel.place(relx=.7, rely=.5, anchor="c")


def work(maket):
    global amo
    img = Image.open(f'{maket}')
    img = img.convert("RGBA")
    amo = 0
    pixdata = img.load()

    width, height = img.size

    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (74, 35, 90, 255):
                pixdata[x, y] = (0, 0, 0, 0)
                amo += 1

    amo = 504 ** 2 - amo
    img.save("last/{}.png".format(eval(maket[maket.rindex("/") + 1: -4])))


def amount():
    broot = Tk()
    broot.geometry("500x100")
    amoun = Label(broot, text='Какое количетво ботов : ')
    amoun.place(relx=.35, rely=.3, anchor="c")

    def got():
        global col
        col = int(entry.get())
        broot.destroy()
        res()

    entry = Entry(broot)
    entry.place(relx=.65, rely=.3, anchor="c")

    got = Button(broot, text="Сохранить", command=got)
    got.place(relx=.5, rely=.7, anchor="c")

