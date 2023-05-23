import customtkinter
import tkinter
from datetime import datetime, time
import requests
import json

class prayerTimes(customtkinter.CTkFrame):

    def __init__(self, master):

        master.geometry("320x480")
        master.title("Home Assistant")
        
        jsonTimes = open('rpiAssistant/prayerTimes.json')
        timesParsed = json.load(jsonTimes)

        if datetime.today().date() > datetime.strptime(timesParsed["date"], '%Y-%m-%d').date():
            url = "http://www.londonprayertimes.com/api/times/?format=json&key=GET YOUR OWN KEY&24hours=true"
            response = requests.request("GET", url)
            data = response.json()
            with open ("rpiAssistant/prayerTimes.json", "w") as jsonTimes:
                json.dump(data, jsonTimes)

            print("Made API call")
            jsonTimes = open('rpiAssistant/prayerTimes.json')
            timesParsed = json.load(jsonTimes)

############################################################################################################
############ Code for the taskbar, contains a timer and the current date.                               ####
############################################################################################################
        taskbar = customtkinter.CTkFrame(master, height = 60)
        taskbar.pack(side='top', fill='x')

        timeLabel = customtkinter.CTkLabel(taskbar, text = "", font = ("Roboto", 18))
        timeLabel.pack(side='left', padx=10)

        dateLabel = customtkinter.CTkLabel(taskbar, text = "", font = ("Roboto", 18))
        dateLabel.pack(side='right', padx=10)  

        def update():
            now = datetime.now()
            currentTime = now.strftime("%H:%M")
            currentDate = now.strftime("%d/%m/%Y")
            timeLabel.configure(text=currentTime)
            dateLabel.configure(text=currentDate)
            master.after(3000, update)


        titleLabel = customtkinter.CTkLabel(master, text = "PRAYER TIMES", font = ("Roboto", 23))
        titleLabel.pack(side='top', pady=15)

        fajrFrame = customtkinter.CTkFrame(master, width=250, height=45)
        fajrFrame.pack(side='top', pady=15)
        fajrFrame.grid_propagate(False)

        fajrLabel = customtkinter.CTkLabel(fajrFrame, text = "Fajr:", font = ("Roboto", 18))
        fajrTime = customtkinter.CTkLabel(fajrFrame, text = timesParsed["fajr"],  font = ("Roboto", 18))
        fajrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
        fajrTime.grid(row=0, column = 5, padx = (130, 0), pady=9)


        dhuhrFrame = customtkinter.CTkFrame(master, width=250, height=45)
        dhuhrFrame.pack(side='top', pady=15)
        dhuhrFrame.grid_propagate(False)

        dhuhrLabel = customtkinter.CTkLabel(dhuhrFrame, text = "Dhuhr:", font = ("Roboto", 18))
        dhuhrTime = customtkinter.CTkLabel(dhuhrFrame, text = timesParsed["dhuhr"],  font = ("Roboto", 18))
        dhuhrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
        dhuhrTime.grid(row=0, column = 5, padx = (110, 0), pady=9)


        asrFrame = customtkinter.CTkFrame(master, width=250, height=45)
        asrFrame.pack(side='top', pady=15)
        asrFrame.grid_propagate(False)

        asrLabel = customtkinter.CTkLabel(asrFrame, text = "Asr:", font = ("Roboto", 18))
        asrTime = customtkinter.CTkLabel(asrFrame, text = timesParsed["asr"],  font = ("Roboto", 18))
        asrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)    
        asrTime.grid(row=0, column = 5, padx = (131, 0), pady=9)


        maghribFrame = customtkinter.CTkFrame(master, width=250, height=45)
        maghribFrame.pack(side='top', pady=15)
        maghribFrame.grid_propagate(False)

        maghribLabel = customtkinter.CTkLabel(maghribFrame, text = "Maghrib:", font = ("Roboto", 18))
        maghribTime = customtkinter.CTkLabel(maghribFrame, text = timesParsed["magrib"],  font = ("Roboto", 18))
        maghribTime.grid(row=0, column = 5, padx = (90, 0), pady=9)
        maghribLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)


        ishaFrame = customtkinter.CTkFrame(master, width=250, height=45)
        ishaFrame.pack(side='top', pady=15)
        ishaFrame.grid_propagate(False)

        ishaLabel = customtkinter.CTkLabel(ishaFrame, text = "Isha:", font = ("Roboto", 18))
        ishaTime = customtkinter.CTkLabel(ishaFrame, text = timesParsed["isha"],  font = ("Roboto", 18))
        ishaLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
        ishaTime.grid(row=0, column = 5, padx = (123, 0), pady=9)


        update()
        master.mainloop()