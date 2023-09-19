import customtkinter as ctk
from tkinter import *
from datetime import datetime, time
from deviceControl.ledControl import ledControl
from deviceControl.pcStatistics import pcStatistics
from PyP100 import PyP100

class deviceControl(ctk.CTkFrame):

    def __init__(self, master, back_callback):
        super().__init__(master)
        self.master = master
        self.back_callback = back_callback
        #self.master.attributes('-fullscreen', True)

        self.returnFrom = 0

        self.device1 = PyP100.P100("", "", "") # Makes a P100 plug object. Enter (device ip, username, password) as parameters
        self.device1.handshake() # Creates cookies so methods can be sent
        self.device1.login() # Credentials are sent to the plug and AES key and IV are created so program is verified to send commands

        self.device2 = PyP100.P100("", "", "")
        self.device2.handshake()
        self.device2.login()

        self.packItems()
        self.update()
        self.createButtons()
        self.mapButtons()
        

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
        
        self.button1 = ctk.CTkButton(self.master, text="LED Lights\nOn/Off", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.device1.toggleState())
        self.button1.place(x = 130, y=90, in_= self.buttonContainer, anchor = "center")
        self.button2 = ctk.CTkButton(self.master, text="LED Lights\nControl", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.openLedControl())
        self.button2.place(x=370, y=90, in_= self.buttonContainer, anchor = "center")

        self.button3 = ctk.CTkButton(self.master, text="3D Printer\nOn/Off", height = 130, width = 180, font = ("Roboto", 35), command =lambda: self.device2.toggleState())
        self.button3.place(x=130, y=270, in_= self.buttonContainer, anchor = "center")
        self.button4 = ctk.CTkButton(self.master, text="Light\nOn/Off", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.device2.toggleState())
        self.button4.place(x=370, y=270, in_= self.buttonContainer, anchor = "center")

        self.button5 = ctk.CTkButton(self.master, text="PC Statistics", height = 130, width = 40, font = ("Roboto", 35), command=lambda: self.openPcStats())
        self.button5.place(x=250, y=430, in_= self.buttonContainer, anchor = "center")

    def openLedControl(self):
        self.cleanUp()
        self.returnFrom = 1
        self.ledControlContainer = ledControl(self.master, self.show_home_menu)
        self.ledControlContainer.place(x = -3000, y = 0)

    def openPcStats(self):
        self.cleanUp()
        self.returnFrom = 2
        self.pcStatsContainer = pcStatistics(self.master, self.show_home_menu)
        self.pcStatsContainer.place(x = -3000, y = 0)

    def mapButtons(self):
        self.button_mapping = {
            1: 'ledControlContainer',
            2: 'pcStatsContainer'
        }

    def show_home_menu(self):
        if self.returnFrom in self.button_mapping:
            container_name = self.button_mapping[self.returnFrom]
            container = getattr(self, container_name)
            container.destroy()
            
        self.packItems()
        self.update()
        self.createButtons()

    def cleanUp(self):
        self.taskbar.pack_forget()
        self.rectFrame.pack_forget()
        self.buttonContainer.pack_forget()

    def back_to_home(self):
        self.cleanUp()
        self.back_callback()