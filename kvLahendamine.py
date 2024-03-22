from tkinter import *

aken = Tk()
aken.geometry('500x500')
aken.title("Ruutvõrrandite lahendamine")
aken.iconbitmap("icon.ico")
tekst = "Ruutvõrrandite lahendamine"
pealkiri = Label(aken,
    text = tekst,
    bg = "white",
    fg = "green",
    font = "Colibri 20",
    height = 3,
    width = len(tekst),
    cursor = "man")


kv_tekst = "x**2"
tekst_ = Label(aken,
    text = kv_tekst,
    fg = "black",
    height = 3,
    width = len(kv_tekst))


tekstbox1 = Entry(aken,
    bg = "green",
    fg = "black",
    width = 6,
    cursor = "man")


pealkiri.pack()

tekstbox1.pack(anchor = SW, pady = 20)
aken.mainloop()