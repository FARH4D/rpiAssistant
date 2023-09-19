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

    def createButtons(self):
        self.buttonContainer = ctk.CTkFrame(self.master, height = 530, width = 500)
        self.buttonContainer.pack(side='top', pady = 150)
        
        self.button1 = ctk.CTkButton(self.master, text="Fade", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.fade3())
        self.button1.place(x = 130, y=90, in_= self.buttonContainer, anchor = "center")
        self.button2 = ctk.CTkButton(self.master, text="Quick", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.quick())
        self.button2.place(x=370, y=90, in_= self.buttonContainer, anchor = "center")

        self.button3 = ctk.CTkButton(self.master, text="Red", height = 130, width = 180, font = ("Roboto", 35), command =lambda: self.red())
        self.button3.place(x=130, y=270, in_= self.buttonContainer, anchor = "center")
        self.button4 = ctk.CTkButton(self.master, text="Green", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.green())
        self.button4.place(x=370, y=270, in_= self.buttonContainer, anchor = "center")

        self.button3 = ctk.CTkButton(self.master, text="Blue", height = 130, width = 180, font = ("Roboto", 35), command =lambda: self.blue())
        self.button3.place(x=130, y=430, in_= self.buttonContainer, anchor = "center")
        self.button4 = ctk.CTkButton(self.master, text="On/Off", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.power())
        self.button4.place(x=370, y=430, in_= self.buttonContainer, anchor = "center")


    def power(self):
        remote = piir.Remote('light.json', 27)
        remote.send('Power')
        print("Signal sent.")
    
    def red(self):
        remote = piir.Remote('light.json', 27)
        remote.send('Red')
        print("Signal sent.")

    def green(self):
        remote = piir.Remote('light.json', 27)
        remote.send('Green')
        print("Signal sent.")

    def blue(self):
        remote = piir.Remote('light.json', 27)
        remote.send('Blue')
        print("Signal sent.")

    def quick(self):
        remote = piir.Remote('light.json', 27)
        remote.send('Quick')
        print("Signal sent.")

    def fade3(self):
        remote = piir.Remote('light.json', 27)
        remote.send('Fade3')
        print("Signal sent.")

    def back_to_home(self):
        self.taskbar.pack_forget()
        self.buttonContainer.pack_forget()
        self.back_callback()