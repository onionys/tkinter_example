#!/usr/bin/env python3

import tkinter


def btn_call_back():
    print("hello world.")

def hide_me(event):
    event.widget.pack_forget()

if __name__ == "__main__":
    print("Hello World. This is the first example of Tkinter.")
    root = tkinter.Tk()
    button = tkinter.Button(master=root,text="hello", command=btn_call_back)
    button.pack()
    button.bind('<Button-1>', hide_me)
    root.mainloop()
