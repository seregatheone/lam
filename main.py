
from tkinter import *
from tkinter import filedialog

from PIL import Image

import making_area
import roy

maket = "null"


def choice():
    global maket
    try:
        root.filename = filedialog.askopenfilename(initialdir="/lam/makets", title="Select file",
                                                   filetypes=(("png files", "*.png"), ("all files", "*.*")))
        maket = root.filename
        image = Image.open(f'{maket}')
        image.show()
    except AttributeError:
        maket = "null"


def make():
    making_area.Paint()


def work():
    if maket == "null":
        choice()
    roy.work(maket)
    roy.amount()



root = Tk()
root.geometry("400x300")
forest = Button(root, text="Создать новый макет", command=make)
forest.place(relx=.5, rely=.4, anchor="c")

choiceb = Button(root, text='Выбрать для анализа имеющийся макет', command=choice)
choiceb.place(relx=.5, rely=.5, anchor="c")

land = Button(root, text='Работа управление роем', command=work)
land.place(relx=.5, rely=.6, anchor="c")

root.mainloop()
