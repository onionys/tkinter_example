#!/usr/bin/env python

import Tkinter as tki

def btn_func():
    root2 = tki.Tk()
    label_ = tki.Label(master=root2,text="FUCK")
    label_.pack()
    root.mainloop()

root = tki.Tk()
btn = tki.Button(master=root,command=btn_func)
btn.pack()
root.mainloop()
