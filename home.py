####################################################################################################
#### My home assistant.                                                                         ####
#### Specifically written for my LCD touchscreen optimised for 320x480 resolution               ####
####################################################################################################
import customtkinter
from tkinter import *
from datetime import datetime, time

from calendarPy import calendarMenu
from prayerTimes import prayerTimes
from intervalTimer import intervalTimer



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
        self.root.geometry("320x480")
        #self.root.attributes('-fullscreen', True)

    ####################################################################################################
    #### Code for the taskbar, contains a timer and the current date.
    ####################################################################################################
        self.taskbar = customtkinter.CTkFrame(self.root, height = 60)
        self.taskbar.pack(side='top', fill='x')

        self.homeIcon = PhotoImage(file='rpiAssistant/images/homeIcon.png')

        self.homeButton = customtkinter.CTkButton(self.root, image=self.homeIcon, text = "")
        self.homeButton.configure(height=20, width=20)
        self.homeButton.place(x= 140, y = 0)

        self.timeLabel = customtkinter.CTkLabel(self.taskbar, text = "", font = ("Roboto", 18))
        self.timeLabel.pack(side='left', padx=10)

        # self.home = customtkinter.CTkButton(self.taskbar, text = "home")
        # self.home.place(x = 120, y = 0)

        self.dateLabel = customtkinter.CTkLabel(self.taskbar, text = "", font = ("Roboto", 18))
        self.dateLabel.pack(side='right', padx=10)  

        ####################################################################################################
        #### Greeting changes depending on the time of day.
        ####################################################################################################
        self.greetingLabel = customtkinter.CTkLabel(self.root, text = "", font = ("Roboto", 23))
        self.greetingLabel.pack(side='top', pady=15)

    ####################################################################################################
    #### Frame for the temperature and humidity sensor, values are taken from DHT
    #### sensor connected to RPI. MUST BE ADDED.
    ####################################################################################################
        self.rectFrame = customtkinter.CTkFrame(self.root, width=250, height=75)
        self.rectFrame.place(relx=0.5, rely=0.3, anchor='center')
        self.rectFrame.grid_propagate(False) # Prevents size of rectangle from being reduced when adding

        self.tempLabel = customtkinter.CTkLabel(self.rectFrame, text = "Temperature: ", font = ("Roboto", 18))
        self.humidLabel = customtkinter.CTkLabel(self.rectFrame, text = "Humidity: ", font = ("Roboto", 18))

        self.tempLabel.grid(row=0, column = 0, padx = (10, 0))
        self.humidLabel.grid(row=1, column = 0, pady = (10, 0))

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
        self.taskbar.pack_forget()
        self.greetingLabel.pack_forget()
        self.rectFrame.place_forget()
        self.calendarButton.place_forget()
        self.piHoleButton.place_forget()
        self.prayerButton.place_forget()
        self.lightControlButton.place_forget()
        self.intervalButton.place_forget()
        calendarMenu(self.root)

    def openPrayer(self):
        self.taskbar.pack_forget()
        self.greetingLabel.pack_forget()
        self.rectFrame.place_forget()
        self.calendarButton.place_forget()
        self.piHoleButton.place_forget()
        self.prayerButton.place_forget()
        self.lightControlButton.place_forget()
        self.intervalButton.place_forget()
        prayerTimes(self.root)

    def openInterval(self):
        self.taskbar.pack_forget()
        self.greetingLabel.pack_forget()
        self.rectFrame.place_forget()
        self.calendarButton.place_forget()
        self.piHoleButton.place_forget()
        self.prayerButton.place_forget()
        self.lightControlButton.place_forget()
        self.intervalButton.place_forget()
        intervalTimer(self.root)

    def createButtons(self):

        self.calendarButton = customtkinter.CTkButton(self.root, text="Calendar", height = 75, width = 90, font = ("Roberto", 18), command=lambda: self.openCalendar())
        self.calendarButton.place(x=50, y=220)
        self.piHoleButton = customtkinter.CTkButton(self.root, text="Pi-Hole", height = 75, width = 90, font = ("Roberto", 18))
        self.piHoleButton.place(x=180, y=220)

        self.prayerButton = customtkinter.CTkButton(self.root, text="Prayer\nTimes", height = 75, width = 90, font = ("Roberto", 18), command=lambda: self.openPrayer())
        self.prayerButton.place(x=50, y=320)
        self.lightControlButton = customtkinter.CTkButton(self.root, text="Light\nControl", height = 75, width = 90, font = ("Roberto", 18))
        self.lightControlButton.place(x=180, y=320)

        self.intervalButton = customtkinter.CTkButton(self.root, text="Interval Timer", height = 60, width = 220, font = ("Roberto", 18), command=lambda: self.openInterval())
        self.intervalButton.place(x=50, y=410)


    def run(self):
        self.createButtons()
        self.root.mainloop()

root = customtkinter.CTk()
Home = home(root)
Home.run()