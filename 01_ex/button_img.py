#!/usr/bin/env python3

import tkinter as tk


btn_list = []
btn_img_list = []

def btn_call_back():
    print("Hello World.")
    btn = btn_list[0]
    btn.config(image=btn_img_list[1])

if __name__ == "__main__":
    print("Hello World. This is the first example of Tkinter.")
    root = tk.Tk()

    # prepare the image 
    button_img_1 = tk.PhotoImage(file='./pic/button.gif')
    button_img_2 = tk.PhotoImage(file='./pic/button_green.gif')
    btn_img_list.append(button_img_1)
    btn_img_list.append(button_img_2)


    button = tk.Button(master=root,text="hello", command=btn_call_back, image=button_img_1)
    btn_list.append(button)
    button.pack()
    #button.grid(row=0,column=0)
    root.mainloop()
