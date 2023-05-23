####################################################################################################
#### My home assistant.                                                                         ####
#### Specifically written for my LCD touchscreen optimised for 320x480 resolution               ####
####################################################################################################
import customtkinter
import tkinter
from datetime import datetime, time

from calendarPy import calendarMenu
from prayerTimes import prayerTimes

####################################################################################################
#### Set properties of window
####################################################################################################
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Home Assistant")
root.geometry("320x480")
#root.attributes('-fullscreen', True)

####################################################################################################
#### Code for the taskbar, contains a timer and the current date.
####################################################################################################
taskbar = customtkinter.CTkFrame(root, height = 60)
taskbar.pack(side='top', fill='x')

timeLabel = customtkinter.CTkLabel(taskbar, text = "", font = ("Roboto", 18))
timeLabel.pack(side='left', padx=10)

dateLabel = customtkinter.CTkLabel(taskbar, text = "", font = ("Roboto", 18))
dateLabel.pack(side='right', padx=10)  

####################################################################################################
#### Greeting changes depending on the time of day.
####################################################################################################
greetingLabel = customtkinter.CTkLabel(root, text = "", font = ("Roboto", 23))
greetingLabel.pack(side='top', pady=15)


def update():
    now = datetime.now()
    currentTime = now.strftime("%H:%M")
    currentDate = now.strftime("%d/%m/%Y")
    timeLabel.configure(text=currentTime)
    dateLabel.configure(text=currentDate)
    root.after(3000, update)

    if (now.time() < time(12,00)): greetingLabel.configure(text="Good morning!")
    elif (now.time() >= time(12,00) and now.time() < time(18,30)): greetingLabel.configure(text="Good afternoon!")
    else: greetingLabel.configure(text="Good evening!")

####################################################################################################
#### Frame for the temperature and humidity sensor, values are taken from DHT
#### sensor connected to RPI. MUST BE ADDED.
####################################################################################################
rectFrame = customtkinter.CTkFrame(root, width=250, height=75)
rectFrame.place(relx=0.5, rely=0.3, anchor='center')
rectFrame.grid_propagate(False) # Prevents size of rectangle from being reduced when adding

tempLabel = customtkinter.CTkLabel(rectFrame, text = "Temperature: ", font = ("Roboto", 18))
humidLabel = customtkinter.CTkLabel(rectFrame, text = "Humidity: ", font = ("Roboto", 18))

tempLabel.grid(row=0, column = 0, padx = (10, 0))
humidLabel.grid(row=1, column = 0, pady = (10, 0))

####################################################################################################
#### Buttons for different menus
####################################################################################################
def openCalendar():
    taskbar.pack_forget()
    greetingLabel.pack_forget()
    rectFrame.place_forget()
    calendarButton.place_forget()
    piHoleButton.place_forget()
    prayerButton.place_forget()
    lightControlButton.place_forget()
    calendarMenu(root)

def openPrayer():
    taskbar.pack_forget()
    greetingLabel.pack_forget()
    rectFrame.place_forget()
    calendarButton.place_forget()
    piHoleButton.place_forget()
    prayerButton.place_forget()
    lightControlButton.place_forget()
    prayerTimes(root)


calendarButton = customtkinter.CTkButton(root, text="Calendar", height = 75, width = 90, font = ("Roberto", 18), command=lambda: openCalendar())
calendarButton.place(x=50, y=220)
piHoleButton = customtkinter.CTkButton(root, text="Pi-Hole", height = 75, width = 90, font = ("Roberto", 18))
piHoleButton.place(x=180, y=220)

prayerButton = customtkinter.CTkButton(root, text="Prayer\nTimes", height = 75, width = 90, font = ("Roberto", 18), command=lambda: openPrayer())
prayerButton.place(x=50, y=320)
lightControlButton = customtkinter.CTkButton(root, text="Light\nControl", height = 75, width = 90, font = ("Roberto", 18))
lightControlButton.place(x=180, y=320)

update()
root.mainloop()