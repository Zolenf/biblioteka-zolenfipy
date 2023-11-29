from tkinter import *

def say(tekst_in_string):
    tekst = tekst_in_string

    print(tekst)

def okno():
    tk = Tk()

    window_width = 1280
    window_height = 720

    tk.geometry(f'{window_width}x{window_height}')

    Tk.mainloop(self= tk)

