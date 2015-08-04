#!/usr/bin/env python

import Tkinter as tk

options = ("one","two","three", "four","five")
selects=[]

def ok():
    print "you now select : %s" % selects[0].get()

root = tk.Tk()
f = tk.Frame(root)
f.pack()

select = tk.StringVar(root)
select.set(options[0])
selects.append(select)

opMenu = tk.OptionMenu(f, select, *options)
opMenu.pack()

button = tk.Button(root, text="ok",command=ok)
button.pack()

tk.mainloop()
