#!/usr/bin/env python

import Tkinter as tk
from threading import Thread
from time import sleep






class seg_head:
    def __init__(self,root):
        self.frame = root
        self.prog_label = tk.Label(master=self.frame, text = " Prog# " )
        self.seg_label = tk.Label(master=self.frame, text = " Seg# " )
        self.seg_type_label = tk.Label(master=self.frame, text = " Seg_type# " )
        self.seg_target = tk.Label(master=self.frame, text = " target SP " )
        self.seg_time = tk.Label(master=self.frame, text = " duration or rate " )
        self.seg_prog_num = tk.Label(master=self.frame, text = " Call Prog Num " )
        self.seg_call_cycle = tk.Label(master=self.frame, text = " Call Cycle " )

        self.prog_label.grid(row=0,column=0)
        self.seg_label.grid(row=0,column=1)
        self.seg_type_label.grid(row=0,column=2)
        self.seg_target.grid(row=0,column=3)
        self.seg_time.grid(row=0,column=4)
        self.seg_prog_num.grid(row=0,column=5)
        self.seg_call_cycle.grid(row=0,column=6)




class seg_line:

    def __init__(self, root,prog,seg , _row):

        self.frame = root
        self.seg_type_options = ("0","1","2", "3","4","5")

        self.prog = prog
        self.seg = seg
        self.seg_type = 0
        self.seg_target_sp = 0.0

        self.prog_label = tk.Label(master=self.frame, text = " %d " % self.prog)
        self.seg_label = tk.Label(master=self.frame, text = " %d " % self.seg)

        self.seg_type_var = tk.StringVar(root)
        self.seg_type_var.set(self.seg_type_options[self.seg_type])
        self.seg_type_optionmenu= tk.OptionMenu(self.frame, self.seg_type_var, *self.seg_type_options)

        self.seg_target_sp_var = tk.StringVar(self.frame)
        self.seg_target_sp_var.set("%f" % self.seg_target_sp) 
        self.seg_target_sp = tk.Entry(self.frame, textvariable=self.seg_target_sp_var)

        #self.seg_time_var

        self.prog_label.grid(         row=_row,column=0)
        self.seg_label.grid(          row=_row,column=1)
        self.seg_type_optionmenu.grid(row=_row,column=2)
        self.seg_target_sp.grid(      row=_row,column=3)


    def load_data(self):
        print "todo"







if __name__ == "__main__":
    root = tk.Tk()
    seg_h = seg_head(root)
    segs = []
    for i in range(1,16+1):
        segs.append( seg_line(root,1,1,i))

    tk.mainloop()
