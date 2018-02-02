from tkinter import *


hexadecimal = ""
hex = 0
hexabc = ""
hexabc1 = ""
def show_values():
    global hex
    global hexabc
    global hexadecimal
    global hexabc1
    hex = int(w1.get()/16)
    if hex==10:
        hexabc1 = "a"
    if hex==11:
        hexabc1 = "b"
    if hex==12:
        hexabc1 = "c"
    if hex==13:
        hexabc1 = "d"
    if hex==14:
        hexabc1 = "e"
    if hex==15:
        hexabc1 = "f"

    if (w1.get()/16 - hex)*16 == 10:
        hexabc = "a"
    if (w1.get()/16 - hex)*16 == 11:
        hexabc = "b"
    if (w1.get()/16 - hex)*16 == 12:
        hexabc = "c"
    if (w1.get()/16 - hex)*16 == 13:
        hexabc = "d"
    if (w1.get()/16 - hex)*16 == 14:
        hexabc = "e"
    if (w1.get()/16 - hex)*16 == 15:
        hexabc = "f"
    if hex >= 10:
        hexadecimal=hexabc1+hexabc
    else:
        hexadecimal = str(hex)+ hexabc
    print (hexadecimal)


master = Tk()

w1 = Scale(master, from_=0, to=255)
w1.set(19)
w1.pack()
w2 = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w2.set(23)
w2.pack()
Button(master, text='Show', command=show_values).pack()
mainloop()
