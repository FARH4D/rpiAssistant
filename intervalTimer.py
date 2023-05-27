import customtkinter
from tkinter import *
from datetime import datetime, time


class intervalTimer(customtkinter.CTkFrame):

    def __init__(self, master):

        self.master = master
        self.master.geometry("320x480")
        self.master.title("Home Assistant") 
        #self.root.attributes('-fullscreen', True)

    
############################################################################################################
############ Code for the taskbar, contains a timer and the current date.                               ####
############################################################################################################
        taskbar = customtkinter.CTkFrame(self.master, height = 60)
        taskbar.pack(side='top', fill='x')

        self.timeLabel = customtkinter.CTkLabel(taskbar, text = "", font = ("Roboto", 18))
        self.timeLabel.pack(side='left', padx=10)

        self.homeIcon = PhotoImage(file='rpiAssistant/images/homeIcon.png')

        self.homeButton = customtkinter.CTkButton(self.root, image=self.homeIcon, text = "")
        self.homeButton.configure(height=20, width=20)
        self.homeButton.place(x= 140, y = 0)


        self.dateLabel = customtkinter.CTkLabel(taskbar, text = "", font = ("Roboto", 18))
        self.dateLabel.pack(side='right', padx=10)

        self.update()
        self.packItems()
        self.packButtons()
        self.master.mainloop()

    def update(self):
        now = datetime.now()
        currentTime = now.strftime("%H:%M")
        currentDate = now.strftime("%d/%m/%Y")
        self.timeLabel.configure(text=currentTime)
        self.dateLabel.configure(text=currentDate)
        self.master.after(3000, self.update)

    def packItems(self):
        self.titleLabel = customtkinter.CTkLabel(self.master, text = "INTERVAL TIMER", font = ("Roboto", 23))
        self.titleLabel.pack(side='top', pady=15)

    def packButtons(self):
        self.timer1 = customtkinter.CTkButton(self.master, text = "1:00", height = 75, width = 80, font = ("Roboto", 23))
        self.timer1.place(x = 20, y = 150)
        self.timer2 = customtkinter.CTkButton(self.master, text = "1:30", height = 75, width = 80, font = ("Roboto", 23))
        self.timer2.place(x = 120, y = 150)
        self.timer3 = customtkinter.CTkButton(self.master, text = "2:00", height = 75, width = 80, font = ("Roboto", 23))
        self.timer3.place(x = 220, y = 150)
        self.timer4 = customtkinter.CTkButton(self.master, text = "3:00", height = 75, width = 80, font = ("Roboto", 23))
        self.timer4.place(x = 60, y = 250)
        self.timer5 = customtkinter.CTkButton(self.master, text = " Custom \n Time", height = 75, width = 80, font = ("Roboto", 23))
        self.timer5.place(x = 180, y = 250)