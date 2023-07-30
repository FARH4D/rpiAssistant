import customtkinter as ctk
from tkinter import *
from datetime import datetime, time
import requests
import json
from urllib import request

class prayerTimes(ctk.CTkFrame):
    
    def __init__(self, master, back_callback):
        
        super().__init__(master)
        self.master = master
        self.back_callback = back_callback
        #self.master.attributes('-fullscreen', True)
        self.packItems()
        self.update()

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
        self.homeButton.place(x= 355, y = 0, in_=self.taskbar)

        self.timeLabel = ctk.CTkLabel(self.taskbar, text = "", font = ("Roboto", 29))
        self.timeLabel.pack(side='left', padx=10)

        self.dateLabel = ctk.CTkLabel(self.taskbar, text = "", font = ("Roboto", 29))
        self.dateLabel.pack(side='right', padx=10) 

        try:
            request.urlopen('https://www.google.co.uk', timeout=1)
            self.requestData()
        except request.URLError as err: 
            print("No Internet connection")
            self.wifiFrame = ctk.CTkFrame(self.master, width=250, height=45)
            self.wifiFrame.pack(side='top', pady=15)
            self.wifiFrame.grid_propagate(False)

            self.wifiLabel = ctk.CTkLabel(self.wifiFrame, text = "NO INTERNET CONNECTION.", font = ("Roboto", 18))
            self.wifiLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)

            self.wifiFrame2 = ctk.CTkFrame(self.master, width=310, height=45)
            self.wifiFrame2.pack(side='top', pady=20)
            self.wifiFrame2.grid_propagate(False)

            self.wifiLabel2 = ctk.CTkLabel(self.wifiFrame2, text = "SHOWING LAST GATHERED TIMES.", font = ("Roboto", 18))
            self.wifiLabel2.grid(row=0, column = 0, padx = (10, 0), pady=9)

            self.master.after(4000, self.noInternet)

    
############################################################################################################
############################################################################################################
    def requestData(self):
        jsonTimes = open('prayerTimes.json')
        self.timesParsed = json.load(jsonTimes)

        if datetime.today().date() > datetime.strptime(self.timesParsed["date"], '%Y-%m-%d').date():
            url = "http://www.londonprayertimes.com/api/times/?format=json&key=GET YOUR OWN KEY&24hours=true"
            response = requests.request("GET", url)
            data = response.json()

            if "error" in data:
                print("Error with API call.")
                errorFrame = ctk.CTkFrame(self.master, width=250, height=45)
                errorFrame.pack(side='top', pady=15)
                errorFrame.grid_propagate(False)

                self.errorLabel = ctk.CTkLabel(errorFrame, text = "ERROR. API CALL FAILED.", font = ("Roboto", 18))
                self.errorLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
                
            else:
                with open ("prayerTimes.json", "w") as jsonTimes:
                    json.dump(data, jsonTimes)
                print("Made API call successfully")
                jsonTimes = open('prayerTimes.json')
                self.timesParsed = json.load(jsonTimes)
                self.packTimes()
        else: self.packTimes()

    def update(self):
        now = datetime.now()
        currentTime = now.strftime("%H:%M")
        currentDate = now.strftime("%d/%m/%Y")
        self.timeLabel.configure(text=currentTime)
        self.dateLabel.configure(text=currentDate)
        self.master.after(3000, self.update)


    def packTimes(self):
        self.titleLabel = ctk.CTkLabel(self.master, text = "PRAYER TIMES", font = ("Roboto", 23))
        self.titleLabel.pack(side='top', pady=15)

        self.fajrFrame = ctk.CTkFrame(self.master, width=250, height=45)
        self.fajrFrame.pack(side='top', pady=15)
        self.fajrFrame.grid_propagate(False)

        self.fajrLabel = ctk.CTkLabel(self.fajrFrame, text = "Fajr:", font = ("Roboto", 18))
        self.fajrTime = ctk.CTkLabel(self.fajrFrame, text = self.timesParsed["fajr"],  font = ("Roboto", 18))
        self.fajrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
        self.fajrTime.grid(row=0, column = 5, padx = (130, 0), pady=9)


        self.dhuhrFrame = ctk.CTkFrame(self.master, width=250, height=45)
        self.dhuhrFrame.pack(side='top', pady=15)
        self.dhuhrFrame.grid_propagate(False)

        self.dhuhrLabel = ctk.CTkLabel(self.dhuhrFrame, text = "Dhuhr:", font = ("Roboto", 18))
        self.dhuhrTime = ctk.CTkLabel(self.dhuhrFrame, text = self.timesParsed["dhuhr"],  font = ("Roboto", 18))
        self.dhuhrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
        self.dhuhrTime.grid(row=0, column = 5, padx = (110, 0), pady=9)


        self.asrFrame = ctk.CTkFrame(self.master, width=250, height=45)
        self.asrFrame.pack(side='top', pady=15)
        self.asrFrame.grid_propagate(False)

        self.asrLabel = ctk.CTkLabel(self.asrFrame, text = "Asr:", font = ("Roboto", 18))
        self.asrTime = ctk.CTkLabel(self.asrFrame, text = self.timesParsed["asr"],  font = ("Roboto", 18))
        self.asrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)    
        self.asrTime.grid(row=0, column = 5, padx = (131, 0), pady=9)


        self.maghribFrame = ctk.CTkFrame(self.master, width=250, height=45)
        self.maghribFrame.pack(side='top', pady=15)
        self.maghribFrame.grid_propagate(False)

        self.maghribLabel = ctk.CTkLabel(self.maghribFrame, text = "Maghrib:", font = ("Roboto", 18))
        self.maghribTime = ctk.CTkLabel(self.maghribFrame, text = self.timesParsed["magrib"],  font = ("Roboto", 18))
        self.maghribTime.grid(row=0, column = 5, padx = (90, 0), pady=9)
        self.maghribLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)


        self.ishaFrame = ctk.CTkFrame(self.master, width=250, height=45)
        self.ishaFrame.pack(side='top', pady=15)
        self.ishaFrame.grid_propagate(False)

        self.ishaLabel = ctk.CTkLabel(self.ishaFrame, text = "Isha:", font = ("Roboto", 18))
        self.ishaTime = ctk.CTkLabel(self.ishaFrame, text = self.timesParsed["isha"],  font = ("Roboto", 18))
        self.ishaLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
        self.ishaTime.grid(row=0, column = 5, padx = (123, 0), pady=9)
    
    def noInternet(self):
        self.wifiLabel.destroy()
        self.wifiFrame.destroy()
        self.wifiLabel2.destroy()
        self.wifiFrame2.destroy()
        print("Removed error labels")

        jsonTimes = open('prayerTimes.json')
        self.timesParsed = json.load(jsonTimes)
        self.packTimes()

    def back_to_home(self):
        self.taskbar.pack_forget()
        self.titleLabel.pack_forget()
        self.fajrFrame.pack_forget()
        self.dhuhrFrame.pack_forget()  # Will clean this up and put these all into a single container when I'm not feeling lazy hehe
        self.asrFrame.pack_forget()
        self.maghribFrame.pack_forget()
        self.ishaFrame.pack_forget()

        self.back_callback()
