####################################################################################################
#### My home assistant.
#### Specifically written for my LCD touchscreen optimised for 320x480 resolution
####################################################################################################
import customtkinter
import tkinter

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
#### Code for the taskbar, contains a timer and the current date. NEED TO ADD
### CODE SO THAT TIME AND DATE ARE  CURRENT
####################################################################################################
taskbar = customtkinter.CTkFrame(root, height = 60)
taskbar.pack(side='top', fill='x')

timeLabel = customtkinter.CTkLabel(taskbar, text = "13:09", font = ("Roboto", 18))
timeLabel.pack(side='left', padx=10)

dateLabel = customtkinter.CTkLabel(taskbar, text = "02/04/2023", font = ("Roboto", 18))
dateLabel.pack(side='right', padx=10)

####################################################################################################
#### Greeting WILL CHANGE DEPENDING ON THE TIME OF DAY
####################################################################################################
greetingLabel = customtkinter.CTkLabel(root, text = "Good Morning!", font = ("Roboto", 23))
greetingLabel.pack(side='top', pady=15)

####################################################################################################
#### Frame for the temperature and humidity sensor, values are taken from DHT
### sensor connected to RPI. MUST BE ADDED.
####################################################################################################
rectFrame = customtkinter.CTkFrame(root, width=250, height=75)
rectFrame.place(relx=0.5, rely=0.3, anchor='center')
rectFrame.grid_propagate(False)

tempLabel = customtkinter.CTkLabel(rectFrame, text = "Temperature: ", font = ("Roberto", 18))
humidLabel = customtkinter.CTkLabel(rectFrame, text = "Humidity: ", font = ("Roberto", 18))

tempLabel.grid(row=0, column = 0, padx = (10, 0))
humidLabel.grid(row=1, column = 0, pady = (10, 0))

####################################################################################################
#### Buttons for different menus
####################################################################################################
calendarButton = customtkinter.CTkButton(root, text="Calendar", height = 75, width = 90, font = ("Roberto", 18))
calendarButton.place(x=50, y=220)
piHoleButton = customtkinter.CTkButton(root, text="Pi-Hole", height = 75, width = 90, font = ("Roberto", 18))
piHoleButton.place(x=180, y=220)

prayerButton = customtkinter.CTkButton(root, text="Prayer\nTimes", height = 75, width = 90, font = ("Roberto", 18))
prayerButton.place(x=50, y=320)
lightControlButton = customtkinter.CTkButton(root, text="Light\nControl", height = 75, width = 90, font = ("Roberto", 18))
lightControlButton.place(x=180, y=320)

root.mainloop()