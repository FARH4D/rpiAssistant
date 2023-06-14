####################################################################################################
#### My home assistant.                                                                         ####
#### Specifically written for my LCD touchscreen optimised for 768x1024 resolution              ####
####################################################################################################
import customtkinter
from tkinter import *
from datetime import datetime, time
import subprocess
import sys

class home(customtkinter.CTkFrame):

    def __init__(self, root):
        super().__init__(root)
    ####################################################################################################
    #### Set properties of window
    ####################################################################################################
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = root
        self.root.title("Home Assistant")
        self.root.geometry("768x1024")
        #self.root.attributes('-fullscreen', True)

    ####################################################################################################
    #### Code for the taskbar, contains a timer and the current date.
    ####################################################################################################
        self.taskbar = customtkinter.CTkFrame(self.root, height = 180)
        self.taskbar.pack(side='top', fill='x')

        self.homeIcon = PhotoImage(file='images/homeIcon.png')

        self.homeButton = customtkinter.CTkButton(self.root, image=self.homeIcon, text = "")
        self.homeButton.configure(height=30, width=30)
        self.homeButton.place(x= 355, y = 0)

        self.timeLabel = customtkinter.CTkLabel(self.taskbar, text = "", font = ("Roboto", 29))
        self.timeLabel.pack(side='left', padx=10)


        self.dateLabel = customtkinter.CTkLabel(self.taskbar, text = "", font = ("Roboto", 29))
        self.dateLabel.pack(side='right', padx=10)  

        ####################################################################################################
        #### Greeting changes depending on the time of day.
        ####################################################################################################
        self.greetingLabel = customtkinter.CTkLabel(self.root, text = "", font = ("Roboto", 35))
        self.greetingLabel.pack(side='top', pady=15)

    ####################################################################################################
    #### Frame for the temperature and humidity sensor, values are taken from DHT
    #### sensor connected to RPI. MUST BE ADDED.
    ####################################################################################################
        self.rectFrame = customtkinter.CTkFrame(self.root, width=500, height=100)
        self.rectFrame.pack(side='top', pady = '50')
        self.rectFrame.grid_propagate(False) # Prevents size of rectangle from being reduced when adding

        self.tempLabel = customtkinter.CTkLabel(self.rectFrame, text = "Temperature: ", font = ("Roboto", 30))
        self.humidLabel = customtkinter.CTkLabel(self.rectFrame, text = "Humidity: ", font = ("Roboto", 30))

        self.tempLabel.grid(row=0, column = 0, padx = (15,0), pady = (10,0))
        self.humidLabel.grid(row=1, column = 0)

        self.update()

    def update(self):
        now = datetime.now()
        currentTime = now.strftime("%H:%M")
        currentDate = now.strftime("%d/%m/%Y")
        self.timeLabel.configure(text=currentTime)
        self.dateLabel.configure(text=currentDate)
        self.root.after(3000, self.update)

        if (now.time() < time(12,00)): self.greetingLabel.configure(text="Good morning!")
        elif (now.time() >= time(12,00) and now.time() < time(18,30)): self.greetingLabel.configure(text="Good afternoon!")
        else: self.greetingLabel.configure(text="Good evening!")

    ####################################################################################################
    #### Buttons for different menus
    ####################################################################################################
    def openCalendar(self):
        subprocess.call([sys.executable, 'calendarPy.py'])

    def openPrayer(self):
        subprocess.call([sys.executable, 'prayerTimes.py'])

    def openInterval(self):
        subprocess.call([sys.executable, 'intervalTimer.py'])

    def createButtons(self):

        self.calendarButton = customtkinter.CTkButton(self.root, text="Calendar", height = 100, width = 120, font = ("Roboto", 29), command=lambda: self.openCalendar())
        self.calendarButton.place(x=200, y=320)
        self.piHoleButton = customtkinter.CTkButton(self.root, text="Pi-Hole", height = 100, width = 120, font = ("Roboto", 29))
        self.piHoleButton.place(x=450, y=320)

        self.prayerButton = customtkinter.CTkButton(self.root, text="Prayer\nTimes", height = 100, width = 120, font = ("Roboto", 29), command=lambda: self.openPrayer())
        self.prayerButton.place(x=200, y=470)
        self.lightControlButton = customtkinter.CTkButton(self.root, text="Light\nControl", height = 100, width = 120, font = ("Roboto", 29))
        self.lightControlButton.place(x=450, y=470)

        self.intervalButton = customtkinter.CTkButton(self.root, text="Interval Timer", height = 60, width = 300, font = ("Roboto", 29), command=lambda: self.openInterval())
        self.intervalButton.place(x=235, y=620)

    def run(self):
        self.createButtons()
        self.root.mainloop()

root = customtkinter.CTk()
Home = home(root)
Home.run()