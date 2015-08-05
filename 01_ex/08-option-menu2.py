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
        self.seg_target_pulse = tk.Label(master=self.frame, text = " Laser Target Pulse " )
        self.seg_pulse_freq  = tk.Label(master=self.frame, text = " Laser Pulse Freq " )
        self.seg_target_pos = tk.Label(master=self.frame, text = " Target positon " )


        self.prog_label.grid(row=0,column=0)
        self.seg_label.grid(row=0,column=1)
        self.seg_type_label.grid(row=0,column=2)
        self.seg_target.grid(row=0,column=3)
        self.seg_time.grid(row=0,column=4)
        self.seg_prog_num.grid(row=0,column=5)
        self.seg_call_cycle.grid(row=0,column=6)
        self.seg_target_pulse.grid(row=0,column=7)
        self.seg_pulse_freq.grid(row=0,column=8)
        self.seg_target_pos.grid(row=0,column=9)




class seg_line:

    def __init__(self, root,prog,seg , _row):

        self.frame = root

        self.prog = prog
        self.seg = seg
        self.seg_type = 0
        self.seg_target_sp = 0.0
        self.seg_time = 0.0
        self.seg_call_prog = 2
        self.seg_call_cycle = 0
        self.seg_target_pulse = 10
        self.seg_pulse_freq = 1
        self.seg_target_pos = "A"

        self.prog_label = tk.Label(master=self.frame, text = " %d " % self.prog)
        self.seg_label = tk.Label(master=self.frame, text = " %d " % self.seg)

        self.seg_type_var = tk.StringVar(root)
        self.seg_type_var.set("%d" % self.seg_type)
        self.seg_type_entry = tk.Entry(self.frame, textvariable=self.seg_type_var)

        self.seg_target_sp_var = tk.StringVar(self.frame)
        self.seg_target_sp_var.set("%f" % self.seg_target_sp) 
        self.seg_target_sp_entry = tk.Entry(self.frame, textvariable=self.seg_target_sp_var)

        self.seg_time_var = tk.StringVar(self.frame)
        self.seg_time_var.set("%f" % self.seg_time)
        self.seg_time_entry = tk.Entry(self.frame, textvariable=self.seg_time_var)

        self.seg_call_prog_var = tk.StringVar(self.frame)
        self.seg_call_prog_var.set("%d" % self.seg_call_prog)
        self.seg_call_prog_entry = tk.Entry(self.frame, textvariable=self.seg_call_prog_var) 

        self.seg_call_cycle_var = tk.StringVar(self.frame)
        self.seg_call_cycle_var.set("%d" % self.seg_call_cycle)
        self.seg_call_cycle_entry = tk.Entry(self.frame, textvariable=self.seg_call_cycle_var) 


        self.seg_target_pulse_var = tk.StringVar(self.frame)
        self.seg_target_pulse_var.set("%d" % self.seg_target_pulse)
        self.seg_target_pulse_entry = tk.Entry(self.frame, textvariable=self.seg_target_pulse_var)

        self.seg_pulse_freq_var = tk.StringVar(self.frame)
        self.seg_pulse_freq_var.set("%d" % self.seg_pulse_freq)
        self.seg_pulse_freq_entry = tk.Entry(self.frame, textvariable=self.seg_pulse_freq_var)

        self.seg_target_pos_var = tk.StringVar(self.frame)
        self.seg_target_pos_var.set("%s" % self.seg_target_pos)
        self.seg_target_pos_entry = tk.Entry(self.frame, textvariable=self.seg_target_pos_var)
        #self.seg_time_var

        self.prog_label.grid(          row=_row,column=0)
        self.seg_label.grid(           row=_row,column=1)
        self.seg_type_entry.grid(      row=_row,column=2)
        self.seg_target_sp_entry.grid( row=_row,column=3)
        self.seg_time_entry.grid(      row=_row,column=4)
        self.seg_call_prog_entry.grid( row=_row,column=5)
        self.seg_call_cycle_entry.grid(row=_row,column=6)
        self.seg_target_pulse_entry.grid(row=_row,column=7)
        self.seg_pulse_freq_entry.grid(row=_row,column=8)
        self.seg_target_pos_entry.grid(row=_row,column=9)




class seg_editor:

    def __init__(self,prog):
        self.root = tk.Tk()
        self.seg_h = seg_head(self.root)
        self.segs = []
        self.prog = prog
        for i in range(1,16+1):
            self.segs.append( seg_line(self.root, prog, i,i) )
        self.prog_var = tk.StringVar(self.root)
        self.prog_var.set("%d" % self.prog)
        self.prog_entry = tk.Entry(self.root, textvariable=self.prog_var)
        self.prog_entry.grid(row=17,column=0)

    def load_data(self):
        eur_file = "/home/pi/code/savedata/eur_load_data"
        pro_file = "/home/pi/code/savedata/program.data"
        eur_data = []
        pro_data = []
        with open(eur_file) as f:
            for line in f:
                msg = line.split()
                eur_data.append(msg)

        with open(pro_file) as f:
            for line in f:
                msg = line.split()
                pro_data.append(msg)

        
        print ""





if __name__ == "__main__":
    seditor = seg_editor(10)
    seditor.root.mainloop()
