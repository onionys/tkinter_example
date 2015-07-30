#!/usr/bin/env python3

import tkinter


btn_stat = 0
btn_list = []



def btn_call_back():
    global btn_stat 
    if btn_stat:
        btn_stat = 0
        btn_list[0]["text"] = "hello world"
    else:
        btn_stat = 1
        btn_list[0]["text"] = "this ex is boring."

if __name__ == "__main__":
    print("Hello World. This is the first example of Tkinter.")
    root = tkinter.Tk()
    button = tkinter.Button(master=root,text="hello", command=btn_call_back)
    button.pack()
    #button.grid(row=0,column=0)
    btn_list.append(button)
    root.mainloop()
