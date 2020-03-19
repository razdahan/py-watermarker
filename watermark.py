import os
import PIL.Image
import argparse
from tkinter import filedialog, simpledialog
from tkinter import *
from tkinter import messagebox
import ntpath
import pathlib


def main(data):
    sq_fit_size = 300
    print(data.logo)
    logo_name = ntpath.basename(data.logo)
    logoIm = PIL.Image.open(data.logo).convert("RGBA")
    logoWidth, logoHeight = logoIm.size
    counter = 1
    new_fldr = simpledialog.askstring('new folder name',
                                      'What is your new photos folder name?')
    os.mkdir(new_fldr)
    for filename in data.images:
        filename = ntpath.basename(filename)
        if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == logo_name:
            continue
        im = PIL.Image.open('./photos/'+filename).convert("RGBA")
        width, height = im.size
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
        im.save(f'./{new_fldr}/{("%04d" % counter)[-4:]}.png')
        messagebox.showinfo(
            "DONE", f"watermarked {counter} images\n you can find them at {pathlib.Path(__file__).parent.absolute()}\{new_fldr}")
    print(f'watermarked {counter} images')


class App(object):
    def __init__(self):
        self.photos_selector = Button(root, text='Choose photos',
                                      command=self.select_photos, width=25)
        self.photos_selector.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.logo_selector = Button(root, text='Choose logo',
                                    command=self.select_logo, width=25)
        self.logo_selector.place(relx=0.5, rely=0.25, anchor=CENTER)
        self.logo = None
        self.images = None

    def select_photos(self):
        if self.logo:
            self.images = filedialog.askopenfilenames(
                parent=root, title='Choose a photos')
            main(self)
            return

        messagebox.showinfo("ERROR", "Please select logo first")

    def select_logo(self):
        self.logo = filedialog.askopenfilename(
            parent=root, title='Choose logo')


if __name__ == '__main__':

    root = Tk()
    Frame(master=root, width=500, height=500, bg='black').pack()
    a = App()
    root.mainloop()
