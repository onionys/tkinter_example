#!/usr/bin/env python3

import tkinter


def btn_call_back():
    print("Hello World.")

if __name__ == "__main__":
    print("Hello World. This is the first example of Tkinter.")
    root = tkinter.Tk()
    button = tkinter.Button(master=root,text="hello", command=btn_call_back)
    button.pack()
    #button.grid(row=0,column=0)
    root.mainloop()
