#!/usr/bin/env python3

import tkinter


label_text_list = []

def btn_call_back():
    label_text_list[0].set("Words have been changed.")

if __name__ == "__main__":
    print("Hello World. This is the first example of Tkinter.")
    root = tkinter.Tk()
    button = tkinter.Button(master=root,text="hello", command=btn_call_back).pack()

    ## alloc the label_text (tkinter.StringVar)
    label_text = tkinter.StringVar()
    label_text.set("Initial Words")
    label_text_list.append(label_text)

    ## alloc the label objext tkinter.StringVar
    label = tkinter.Label(master=root,textvariable=label_text).pack()

    root.mainloop()
