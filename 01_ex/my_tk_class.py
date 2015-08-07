#!/usr/bin/env python3

import tkinter as tk
from PIL import ImageTk, Image

class sw_btn_img(tk.Button):

    def __init__(self,root,img_on,img_off):
        tk.Button.__init__(self=self,master=root,text="",command=self.command,image=img_off)
        self.img_on  = img_on
        self.img_off = img_off
        self.condition = False

    def command(self):
        self.condition = False if self.condition else True
        self.config(image=self.img_on if self.condition else self.img_off)

if __name__=="__main__":
    root = tk.Tk()
    im_on = Image.open('./pic/btn_sw_on.gif')
    img_on = ImageTk.PhotoImage(im_on)
    im_off = Image.open('./pic/btn_sw_off.gif')
    img_off = ImageTk.PhotoImage(im_off)
    btn = sw_btn_img(root,img_on, img_off)
    btn.pack()
    root.mainloop()
