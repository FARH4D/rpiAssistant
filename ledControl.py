import customtkinter as ctk
from tkinter import *
from datetime import datetime, time
import piir
from PyP100 import PyP100

class ledControl(ctk.CTkFrame):

    def __init__(self, master, back_callback):
        super().__init__(master)
        self.master = master
        self.back_callback = back_callback
        #self.master.attributes('-fullscreen', True)
        self.packItems()
        self.update()


    def update(self):
        if self.updateCycle:
            now = datetime.now()
            currentTime = now.strftime("%H:%M")
            currentDate = now.strftime("%d/%m/%Y")
            self.timeLabel.configure(text=currentTime)
            self.dateLabel.configure(text=currentDate)
            self.master.after(3000, self.update)
    
############################################################################################################
############ Code for the taskbar, contains a timer and the current date.                               ####
############################################################################################################
    def packItems(self):
        self.updateCycle = True
        self.taskbar = ctk.CTkFrame(self.master, height = 180)
        self.taskbar.pack(side='top', fill='x')

        self.homeIcon = PhotoImage(file='images/homeIcon.png')

        self.homeButton = ctk.CTkButton(self.taskbar, image=self.homeIcon, text = "", command=lambda: self.back_to_home())
        self.homeButton.configure(height=30, width=30)
        self.homeButton.place(x= 355, y = 0)

        self.timeLabel = ctk.CTkLabel(self.taskbar, text = "", font = ("Roboto", 29))
        self.timeLabel.pack(side='left', padx=10)

        self.dateLabel = ctk.CTkLabel(self.taskbar, text = "", font = ("Roboto", 29))
        self.dateLabel.pack(side='right', padx=10)

    def back_to_home(self):
        self.taskbar.pack_forget()
        self.back_callback()