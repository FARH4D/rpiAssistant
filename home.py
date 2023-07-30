####################################################################################################
#### My home assistant.                                                                         ####
#### Specifically written for my LCD touchscreen optimised for 768x1024 resolution              ####
####################################################################################################
import customtkinter as ctk
from tkinter import *
from datetime import datetime, time
import subprocess
from intervalTimer import intervalTimer
from prayerTimes import prayerTimes
import sys
import piir
import Adafruit_DHT

class home(ctk.CTkFrame):

####################################################################################################
#### Set properties of window
####################################################################################################
    def __init__(self, master):
        super().__init__(master) ## Initializes the constructor of the master class (CTK Frame and allows it to be changed)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.master = master
        self.master.title("Home Assistant")
        self.master.geometry("768x1024")
        #self.master.attributes('-fullscreen', True)

        self.returnFrom = 0

        self.packItems()
        self.update()
        self.createButtons()
        self.mapButtons()
####################################################################################################
#### Code for the taskbar, contains a timer and the current date.
####################################################################################################
    def packItems(self):
        self.updateCycle = True
        self.taskbar = ctk.CTkFrame(self.master, height = 180)
        self.taskbar.pack(side='top', fill='x')

        self.homeIcon = PhotoImage(file='images/homeIcon.png')
        self.homeButton = ctk.CTkButton(self.taskbar, image=self.homeIcon, text = "")
        self.homeButton.configure(height=30, width=30)
        self.homeButton.place(x= 355, y = 0, in_=self.taskbar)

        self.timeLabel = ctk.CTkLabel(self.taskbar, text = "", font = ("Roboto", 29))
        self.timeLabel.pack(side='left', padx=10)

        self.dateLabel = ctk.CTkLabel(self.taskbar, text = "", font = ("Roboto", 29))
        self.dateLabel.pack(side='right', padx=10)
####################################################################################################
#### Greeting changes depending on the time of day.
####################################################################################################
        self.greetingLabel = ctk.CTkLabel(self.master, text = "", font = ("Roboto", 35))
        self.greetingLabel.pack(side='top', pady=15)

 
        # sensor = Adafruit_DHT.DHT11
        # pin = 4

        # humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        # if humidity is not None and temperature is not None:
        #     print(f"Temperature: {temperature}°C")
        #     print(f"Humidity: {humidity}%")
        # else:
        #     print("Failed to retrieve data from DHT11 sensor.")
        

####################################################################################################
#### Frame for the temperature and humidity sensor, values are taken from DHT
#### sensor connected to RPI. MUST BE ADDED.
####################################################################################################
        self.rectFrame = ctk.CTkFrame(self.master, width=500, height=100)
        self.rectFrame.pack(side='top', pady = '50')
        self.rectFrame.grid_propagate(False) # Prevents size of rectangle from being reduced when adding

        # self.tempLabel = ctk.CTkLabel(self.rectFrame, text = f"Temperature:  {temperature}°C", font = ("Roboto", 30))
        # self.humidLabel = ctk.CTkLabel(self.rectFrame, text = f"Humidity: {humidity}%", font = ("Roboto", 30))

        # self.tempLabel.grid(row=0, column = 0, padx = (15,0), pady = (10,0))
        # self.humidLabel.grid(row=1, column = 0)

    def update(self):
        now = datetime.now()
        currentTime = now.strftime("%H:%M")
        currentDate = now.strftime("%d/%m/%Y")
        self.timeLabel.configure(text=currentTime)
        self.dateLabel.configure(text=currentDate)
        self.master.after(3000, self.update)

        if (now.time() < time(12,00)): self.greetingLabel.configure(text="Good morning!")
        elif (now.time() >= time(12,00) and now.time() < time(18,30)): self.greetingLabel.configure(text="Good afternoon!")
        else: self.greetingLabel.configure(text="Good evening!")

####################################################################################################
#### Buttons for different menus
####################################################################################################
    def openTracker(self):
        self.returnFrom = 1
        pass

    def openPrayer(self):
        self.cleanUp()
        self.returnFrom = 3
        self.prayerTimeContainer = prayerTimes(self.master, self.show_home_menu)
        self.prayerTimeContainer.pack()

    def openInterval(self):
        self.cleanUp()
        self.returnFrom = 4
        self.intervalTimerContainer = intervalTimer(self.master, self.show_home_menu)
        self.intervalTimerContainer.pack()

    def openDevices(self):
        self.returnFrom = 5
        pass
        """ remote = piir.Remote('light.json', 27)
        remote.send('Power')
        print("Signal sent.") """



    def mapButtons(self):
        self.button_mapping = {
            1: 'fitnessContainer',
            2: 'piHoleContainer',
            3: 'prayerTimeContainer',
            4: 'intervalTimerContainer',
            5: 'deviceControlContainer'
        }

    def show_home_menu(self):
        if self.returnFrom in self.button_mapping:
            container_name = self.button_mapping[self.returnFrom]
            container = getattr(self, container_name)
            container.destroy()
            
        self.packItems()
        self.update()
        self.createButtons()

    def createButtons(self):
        self.buttonContainer = ctk.CTkFrame(self.master, height = 530, width = 500)
        self.buttonContainer.pack(side='top')
        
        self.fitnessButton = ctk.CTkButton(self.master, text="Fitness\nTracker", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.openTracker())
        self.fitnessButton.place(x = 130, y=90, in_= self.buttonContainer, anchor = "center")
        self.piHoleButton = ctk.CTkButton(self.master, text="Pi-Hole", height = 130, width = 180, font = ("Roboto", 35))
        self.piHoleButton.place(x=370, y=90, in_= self.buttonContainer, anchor = "center")

        self.prayerButton = ctk.CTkButton(self.master, text="Prayer\nTimes", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.openPrayer())
        self.prayerButton.place(x=130, y=270, in_= self.buttonContainer, anchor = "center")
        self.deviceButton = ctk.CTkButton(self.master, text="Device\nControl", height = 130, width = 180, font = ("Roboto", 35), command=lambda: self.openDevices())
        self.deviceButton.place(x=370, y=270, in_= self.buttonContainer, anchor = "center")

        self.intervalButton = ctk.CTkButton(self.master, text="Interval Timer", height = 100, width = 400, font = ("Roboto", 35), command=lambda: self.openInterval())
        self.intervalButton.place(x=235, y=430, in_= self.buttonContainer, anchor = "center")

    def cleanUp(self):
        self.taskbar.pack_forget()
        self.greetingLabel.pack_forget()
        self.rectFrame.pack_forget()
        self.buttonContainer.pack_forget()