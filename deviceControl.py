import customtkinter as ctk
from tkinter import *
from datetime import datetime, time
import piir

class deviceControl(ctk.CTkFrame):

    def __init__(self, master, back_callback):
        super().__init__(master)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.master = master
        self.back_callback = back_callback
        #self.master.attributes('-fullscreen', True)

        self.packItems()
        self.update()
        self.createButtons()
        

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



        self.rectFrame = ctk.CTkFrame(self.master, width=500, height=100)                   # HAVE CODE FOR RASPBERRY PI TEMPS
        self.rectFrame.pack(side='top', pady = '50')                                        # AND POSSIBLY CURRENT LOAD
        self.rectFrame.grid_propagate(False) # Prevents size of rectangle from being reduced when adding


    def createButtons(self):
        self.buttonContainer = ctk.CTkFrame(self.master, height = 530, width = 500)
        self.buttonContainer.pack(side='top')
        
        self.button1 = ctk.CTkButton(self.master, text="Device 1", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.openTracker())
        self.button1.place(x = 130, y=90, in_= self.buttonContainer, anchor = "center")
        self.button2 = ctk.CTkButton(self.master, text="Device 2", height = 130, width = 180, font = ("Roboto", 35))
        self.button2.place(x=370, y=90, in_= self.buttonContainer, anchor = "center")

        self.button3 = ctk.CTkButton(self.master, text="Device 3", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.openPrayer())
        self.button3.place(x=130, y=270, in_= self.buttonContainer, anchor = "center")
        self.button4 = ctk.CTkButton(self.master, text="Device 4", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.openDevices())
        self.button4.place(x=370, y=270, in_= self.buttonContainer, anchor = "center")

        self.button5 = ctk.CTkButton(self.master, text="LED Lights\nPower", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.openPrayer())
        self.button5.place(x=130, y=450, in_= self.buttonContainer, anchor = "center")
        self.button6 = ctk.CTkButton(self.master, text="Device 6", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.openDevices())
        self.button6.place(x=370, y=450, in_= self.buttonContainer, anchor = "center")




    def back_to_home(self):
        self.taskbar.pack_forget()
        self.rectFrame.pack_forget()
        self.buttonContainer.pack_forget()
        self.back_callback()