#!/usr/bin/env python

import Tkinter

class main_view:


    def __init__(self):
        self.root = Tkinter.Tk()
        self.plot_frame = Tkinter.Frame(master=self.root).grid(row=0,column=0)
        self.cond_frame = Tkinter.Frame(master=self.root).grid(row=0,column=1)
        self.ctrl_frame = Tkinter.Frame(master=self.root).grid(row=0,column=2)

        self.init_ctrl_frame()


    def init_ctrl_frame(self):
        _f = self.ctrl_frame
        self.ctrl_laser_frame  = Tkinter.Frame(master= _f ).pack()
        self.ctrl_eur_frame    = Tkinter.Frame(master= _f ).pack()
        self.ctrl_target_frame = Tkinter.Frame(master= _f ).pack()

        self.init_ctrl_laser_frame()
        self.init_ctrl_eur_frame()


    def init_ctrl_laser_frame(self):
        _f = self.ctrl_laser_frame
        self.ctrl_laser_target_pulse_label = Tkinter.Label(master= _f ,text= "Target Pluse" ).grid(row = 0, column = 0)
        self.ctrl_laser_target_pulse_entry = Tkinter.Entry(master= _f ).grid(row = 0, column = 1 )

        self.ctrl_laser_max_miss_pusle_label = Tkinter.Label(master= _f ,text= "Max Miss Pluse" ).grid(row = 1 ,column = 0)
        self.ctrl_laser_max_miss_pulse_entry = Tkinter.Entry(master= _f ).grid(row = 1, column = 1)

        self.ctrl_laser_start_btn = Tkinter.Button(master= _f , text= "START", command=).grid(row = 2, column = 0)
        self.ctrl_laser_stop_btn  = Tkinter.Button(master= _f , text= "STOP" , command=).grid(row = 2, column = 1)
        self.ctrl_laser_hold_btn  = Tkinter.Button(master= _f , text= "HOLD" , command=).grid(row = 3, column = 0)
        self.ctrl_laser_reset_btn = Tkinter.Button(master= _f , text= "RESET", command=).grid(row = 3, column = 1)


    def init_ctrl_eur_frame(self):
        _f = self.ctrl_eur_frame
        self.ctrl_eur_SP_label = Tkinter.Label(master= _f ,text= "Set Point" ).grid(row = 0, column = 0)
        self.ctrl_eur_SP_entry = Tkinter.Entry(master= _f ).grid(row = 0, column = 1 )

        self.ctrl_eur_OP_label = Tkinter.Label(master= _f ,text= "Output Power(%)" ).grid(row = 1, column = 0)
        self.ctrl_eur_OP_entry = Tkinter.Entry(master= _f ).grid(row = 1, column = 1 )

        self.ctrl_eur_run_btn = Tkinter.Button(master= _f , text= "RUN", command=).grid(row = 2, column = 0)
        self.ctrl_eur__btn = Tkinter.Button(master= _f , text= "RUN", command=).grid(row = 2, column = 0)
        self.ctrl_eur__btn = Tkinter.Button(master= _f , text= "RUN", command=).grid(row = 2, column = 0)
        self.ctrl_eur__btn = Tkinter.Button(master= _f , text= "RUN", command=).grid(row = 2, column = 0)
        self.ctrl_eur__btn = Tkinter.Button(master= _f , text= "RUN", command=).grid(row = 2, column = 0)

