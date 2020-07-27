from tkinter import *

from PIL import ImageGrab


class Paint(object):
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = '#F4D03F'

    def __init__(self):
        self.root = Tk()
        self.root.title("Создание нового макета")
        self.forest = Button(self.root, text="Лес", command=self.forest)
        self.forest.grid(row=0, column=0)

        self.sep = Button(self.root, text='Препятствие', command=self.sep)
        self.sep.grid(row=0, column=1)

        self.land = Button(self.root, text='Земля', command=self.land)
        self.land.grid(row=0, column=2)

        self.options = Text(self.root, height=3, width=25)
        self.options.insert(INSERT, "Цвет земли -    " + "\n" + "Цвет леса -     " + "\n" + f"Цвет препятствий -     ")
        self.options.tag_add("yell", "1.13", "1.16")
        self.options.tag_add("zel", "2.12", "2.15")
        self.options.tag_add("blue", "3.19", "3.22")
        self.options.tag_config("yell", background='#F4D03F')
        self.options.tag_config("zel", background='#145A32')
        self.options.tag_config("blue", background='#4A235A')
        self.options.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=15, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.yellow = Text(width=50, height=10)

        self.c = Canvas(self.root, bg='#F4D03F', width=500, height=500)
        self.c.grid(row=1, columnspan=5)

        self.save = Button(self.root, text="Сохранить", command=self.save)
        self.save.grid(row=2, column=3)

        self.label = Label(self.root, text="Название файла")
        self.label.grid(row=2, column=1)

        self.entry = Entry(self.root)
        self.entry.grid(row=2, column=2)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.land_on = False
        self.sep_on = False
        self.forest_on = False
        self.active_button = self.forest
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def save(self):
        name = self.entry.get()
        x = self.c.winfo_rootx()
        y = self.c.winfo_rooty()
        x1 = x + self.c.winfo_width()
        y1 = y + self.c.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(f"makets/{name}.png")
        self.root.destroy()

    def forest(self):
        self.activate_button(self.forest, forest_mode=True)

    def sep(self):
        self.activate_button(self.sep, sep_mode=True)

    def land(self):
        self.activate_button(self.land, land_mode=True)

    def activate_button(self, some_button, land_mode=False, sep_mode=False, forest_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.land_on = land_mode
        self.sep_on = sep_mode
        self.forest_on = forest_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        if self.land_on:
            paint_color = '#F4D03F'
        elif self.forest_on:
            paint_color = '#145A32'
        else:
            paint_color = '#4A235A'
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()
