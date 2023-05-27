import customtkinter
from tkinter import *
from datetime import datetime, time
import requests
import json
from urllib import request

class prayerTimes(customtkinter.CTkFrame):
    
    def __init__(self, master):
        self.master = master
        self.master.geometry("320x480")
        self.master.title("Home Assistant")

############################################################################################################
############ Code for the taskbar, contains a timer and the current date.                               ####
############################################################################################################
        self.taskbar = customtkinter.CTkFrame(self.master, height = 60)
        self.taskbar.pack(side='top', fill='x')

        self.timeLabel = customtkinter.CTkLabel(taskbar, text = "", font = ("Roboto", 18))
        self.timeLabel.pack(side='left', padx=10)

        self.homeIcon = PhotoImage(file='rpiAssistant/images/homeIcon.png')

        self.homeButton = customtkinter.CTkButton(self.root, image=self.homeIcon, text = "", command=lambda: self.goHome())
        self.homeButton.configure(height=20, width=20)
        self.homeButton.place(x= 140, y = 0)


        self.dateLabel = customtkinter.CTkLabel(taskbar, text = "", font = ("Roboto", 18))
        self.dateLabel.pack(side='right', padx=10)

        try:
            request.urlopen('https://www.google.co.uk', timeout=1)
            self.requestData()
        except request.URLError as err: 
            print("No Internet connection")
            self.wifiFrame = customtkinter.CTkFrame(self.master, width=250, height=45)
            self.wifiFrame.pack(side='top', pady=15)
            self.wifiFrame.grid_propagate(False)

            self.wifiLabel = customtkinter.CTkLabel(self.wifiFrame, text = "NO INTERNET CONNECTION.", font = ("Roboto", 18))
            self.wifiLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)

            self.wifiFrame2 = customtkinter.CTkFrame(self.master, width=310, height=45)
            self.wifiFrame2.pack(side='top', pady=20)
            self.wifiFrame2.grid_propagate(False)

            self.wifiLabel2 = customtkinter.CTkLabel(self.wifiFrame2, text = "SHOWING LAST GATHERED TIMES.", font = ("Roboto", 18))
            self.wifiLabel2.grid(row=0, column = 0, padx = (10, 0), pady=9)

            self.master.after(4000, self.noInternet)
        
        self.update()
        self.master.mainloop()
    
############################################################################################################
############################################################################################################
    def requestData(self):
        jsonTimes = open('rpiAssistant/prayerTimes.json')
        self.timesParsed = json.load(jsonTimes)

        if datetime.today().date() > datetime.strptime(self.timesParsed["date"], '%Y-%m-%d').date():
            url = "http://www.londonprayertimes.com/api/times/?format=json&key=GET YOUR OWN KEY&24hours=true"
            response = requests.request("GET", url)
            data = response.json()

            if "error" in data:
                print("Error with API call.")
                errorFrame = customtkinter.CTkFrame(self.master, width=250, height=45)
                errorFrame.pack(side='top', pady=15)
                errorFrame.grid_propagate(False)

                self.errorLabel = customtkinter.CTkLabel(errorFrame, text = "ERROR. API CALL FAILED.", font = ("Roboto", 18))
                self.errorLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
                
            else:
                with open ("rpiAssistant/prayerTimes.json", "w") as jsonTimes:
                    json.dump(data, jsonTimes)
                print("Made API call successfully")
                jsonTimes = open('rpiAssistant/prayerTimes.json')
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
        self.titleLabel = customtkinter.CTkLabel(self.master, text = "PRAYER TIMES", font = ("Roboto", 23))
        self.titleLabel.pack(side='top', pady=15)

        self.fajrFrame = customtkinter.CTkFrame(self.master, width=250, height=45)
        self.fajrFrame.pack(side='top', pady=15)
        self.fajrFrame.grid_propagate(False)

        self.fajrLabel = customtkinter.CTkLabel(self.fajrFrame, text = "Fajr:", font = ("Roboto", 18))
        self.fajrTime = customtkinter.CTkLabel(self.fajrFrame, text = self.timesParsed["fajr"],  font = ("Roboto", 18))
        self.fajrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
        self.fajrTime.grid(row=0, column = 5, padx = (130, 0), pady=9)


        self.dhuhrFrame = customtkinter.CTkFrame(self.master, width=250, height=45)
        self.dhuhrFrame.pack(side='top', pady=15)
        self.dhuhrFrame.grid_propagate(False)

        self.dhuhrLabel = customtkinter.CTkLabel(self.dhuhrFrame, text = "Dhuhr:", font = ("Roboto", 18))
        self.dhuhrTime = customtkinter.CTkLabel(self.dhuhrFrame, text = self.timesParsed["dhuhr"],  font = ("Roboto", 18))
        self.dhuhrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
        self.dhuhrTime.grid(row=0, column = 5, padx = (110, 0), pady=9)


        self.asrFrame = customtkinter.CTkFrame(self.master, width=250, height=45)
        self.asrFrame.pack(side='top', pady=15)
        self.asrFrame.grid_propagate(False)

        self.asrLabel = customtkinter.CTkLabel(self.asrFrame, text = "Asr:", font = ("Roboto", 18))
        self.asrTime = customtkinter.CTkLabel(self.asrFrame, text = self.timesParsed["asr"],  font = ("Roboto", 18))
        self.asrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)    
        self.asrTime.grid(row=0, column = 5, padx = (131, 0), pady=9)


        self.maghribFrame = customtkinter.CTkFrame(self.master, width=250, height=45)
        self.maghribFrame.pack(side='top', pady=15)
        self.maghribFrame.grid_propagate(False)

        self.maghribLabel = customtkinter.CTkLabel(self.maghribFrame, text = "Maghrib:", font = ("Roboto", 18))
        self.maghribTime = customtkinter.CTkLabel(self.maghribFrame, text = self.timesParsed["magrib"],  font = ("Roboto", 18))
        self.maghribTime.grid(row=0, column = 5, padx = (90, 0), pady=9)
        self.maghribLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)


        self.ishaFrame = customtkinter.CTkFrame(self.master, width=250, height=45)
        self.ishaFrame.pack(side='top', pady=15)
        self.ishaFrame.grid_propagate(False)

        self.ishaLabel = customtkinter.CTkLabel(self.ishaFrame, text = "Isha:", font = ("Roboto", 18))
        self.ishaTime = customtkinter.CTkLabel(self.ishaFrame, text = self.timesParsed["isha"],  font = ("Roboto", 18))
        self.ishaLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
        self.ishaTime.grid(row=0, column = 5, padx = (123, 0), pady=9)
    
    def noInternet(self):
        self.wifiLabel.destroy()
        self.wifiFrame.destroy()
        self.wifiLabel2.destroy()
        self.wifiFrame2.destroy()
        print("Removed error labels")

        jsonTimes = open('rpiAssistant/prayerTimes.json')
        self.timesParsed = json.load(jsonTimes)
        self.packTimes()

    def goHome(self):
        self.taskbar.destroy()
        self.titleLabel.destroy()
        self.fajrFrame.destroy()
        self.fajrLabel.destroy()
        self.dhuhrFrame.destroy()
        self.dhuhrLabel.destroy()
        self.asrFrame.destroy()
        self.asrLabel.destroy()
        self.maghribFrame.destroy()
        self.maghribLabel.destroy()
        self.ishaFrame.destroy()
        self.ishaLabel.destroy()