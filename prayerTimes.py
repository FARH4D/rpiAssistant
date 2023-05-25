import customtkinter
import tkinter
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
        taskbar = customtkinter.CTkFrame(self.master, height = 60)
        taskbar.pack(side='top', fill='x')

        self.timeLabel = customtkinter.CTkLabel(taskbar, text = "", font = ("Roboto", 18))
        self.timeLabel.pack(side='left', padx=10)

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
        titleLabel = customtkinter.CTkLabel(self.master, text = "PRAYER TIMES", font = ("Roboto", 23))
        titleLabel.pack(side='top', pady=15)

        fajrFrame = customtkinter.CTkFrame(self.master, width=250, height=45)
        fajrFrame.pack(side='top', pady=15)
        fajrFrame.grid_propagate(False)

        fajrLabel = customtkinter.CTkLabel(fajrFrame, text = "Fajr:", font = ("Roboto", 18))
        fajrTime = customtkinter.CTkLabel(fajrFrame, text = self.timesParsed["fajr"],  font = ("Roboto", 18))
        fajrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
        fajrTime.grid(row=0, column = 5, padx = (130, 0), pady=9)


        dhuhrFrame = customtkinter.CTkFrame(self.master, width=250, height=45)
        dhuhrFrame.pack(side='top', pady=15)
        dhuhrFrame.grid_propagate(False)

        dhuhrLabel = customtkinter.CTkLabel(dhuhrFrame, text = "Dhuhr:", font = ("Roboto", 18))
        dhuhrTime = customtkinter.CTkLabel(dhuhrFrame, text = self.timesParsed["dhuhr"],  font = ("Roboto", 18))
        dhuhrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
        dhuhrTime.grid(row=0, column = 5, padx = (110, 0), pady=9)


        asrFrame = customtkinter.CTkFrame(self.master, width=250, height=45)
        asrFrame.pack(side='top', pady=15)
        asrFrame.grid_propagate(False)

        asrLabel = customtkinter.CTkLabel(asrFrame, text = "Asr:", font = ("Roboto", 18))
        asrTime = customtkinter.CTkLabel(asrFrame, text = self.timesParsed["asr"],  font = ("Roboto", 18))
        asrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)    
        asrTime.grid(row=0, column = 5, padx = (131, 0), pady=9)


        maghribFrame = customtkinter.CTkFrame(self.master, width=250, height=45)
        maghribFrame.pack(side='top', pady=15)
        maghribFrame.grid_propagate(False)

        maghribLabel = customtkinter.CTkLabel(maghribFrame, text = "Maghrib:", font = ("Roboto", 18))
        maghribTime = customtkinter.CTkLabel(maghribFrame, text = self.timesParsed["magrib"],  font = ("Roboto", 18))
        maghribTime.grid(row=0, column = 5, padx = (90, 0), pady=9)
        maghribLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)


        ishaFrame = customtkinter.CTkFrame(self.master, width=250, height=45)
        ishaFrame.pack(side='top', pady=15)
        ishaFrame.grid_propagate(False)

        ishaLabel = customtkinter.CTkLabel(ishaFrame, text = "Isha:", font = ("Roboto", 18))
        ishaTime = customtkinter.CTkLabel(ishaFrame, text = self.timesParsed["isha"],  font = ("Roboto", 18))
        ishaLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
        ishaTime.grid(row=0, column = 5, padx = (123, 0), pady=9)
    
    def noInternet(self):
        self.wifiLabel.destroy()
        self.wifiFrame.destroy()
        self.wifiLabel2.destroy()
        self.wifiFrame2.destroy()
        print("Removed error labels")

        jsonTimes = open('rpiAssistant/prayerTimes.json')
        self.timesParsed = json.load(jsonTimes)
        self.packTimes()