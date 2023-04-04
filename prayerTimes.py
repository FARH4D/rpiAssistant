import customtkinter
import tkinter
from datetime import datetime, time
import requests

class prayerTimes(customtkinter.CTkFrame):

    def __init__(self, master):

        master.geometry("320x480")
        master.title("Home Assistant")

        ## IN THE FUTURE TO LOWER THE NUMBER OF API REQUESTS, STORE CURRENT DATA IN A DICTIONARY OR TEXT FILE, IF THE DATE
        ## IS EQUAL TO TODAY THEN KEEP THE CURRENT PRAYER TIMES, IF IT IS NOT EQUAL TO TODAY THEN MAKE ANOTHER API REQUEST

        url = "https://muslimsalat.p.rapidapi.com/Birmingham%20UK.json"

        headers = {
            'X-RapidAPI-Key': 'get your own api key buddy',
            'X-RapidAPI-Host': 'muslimsalat.p.rapidapi.com'
        }

        response = requests.request("GET", url, headers=headers)

        dataa = response.json()["items"]

        times = dataa[0]


        print(response.text)
        print(times)

        print("----------------")
        print(times["fajr"])

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

        fajrLabel = customtkinter.CTkLabel(fajrFrame, text = "Fajr:         " + times["fajr"], font = ("Roboto", 18))
        fajrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)


        sunriseFrame = customtkinter.CTkFrame(master, width=250, height=45)
        sunriseFrame.pack(side='top', pady=15)
        sunriseFrame.grid_propagate(False)

        sunriseLabel = customtkinter.CTkLabel(sunriseFrame, text = "Sunrise:        " + times["shurooq"], font = ("Roboto", 18))
        sunriseLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)


        dhuhrFrame = customtkinter.CTkFrame(master, width=250, height=45)
        dhuhrFrame.pack(side='top', pady=15)
        dhuhrFrame.grid_propagate(False)

        dhuhrLabel = customtkinter.CTkLabel(dhuhrFrame, text = "Dhuhr:          " + times["dhuhr"], font = ("Roboto", 18))
        dhuhrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)


        asrFrame = customtkinter.CTkFrame(master, width=250, height=45)
        asrFrame.pack(side='top', pady=15)
        asrFrame.grid_propagate(False)

        asrLabel = customtkinter.CTkLabel(asrFrame, text = "Asr:        " + times["asr"], font = ("Roboto", 18))
        asrLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)


        maghribFrame = customtkinter.CTkFrame(master, width=250, height=45)
        maghribFrame.pack(side='top', pady=15)
        maghribFrame.grid_propagate(False)

        maghribLabel = customtkinter.CTkLabel(maghribFrame, text = "Maghrib:", font = ("Roboto", 18))
        maghribTime = customtkinter.CTkLabel(maghribFrame, text = times["maghrib"],  font = ("Roboto", 18))
        maghribLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)
        maghribTime.grid(row=0, column = 5, padx = (90, 0), pady=9)


        ishaFrame = customtkinter.CTkFrame(master, width=250, height=45)
        ishaFrame.pack(side='top', pady=15)
        ishaFrame.grid_propagate(False)

        ishaLabel = customtkinter.CTkLabel(ishaFrame, text = "Isha:         " + times["isha"], font = ("Roboto", 18))
        ishaLabel.grid(row=0, column = 0, padx = (10, 0), pady=9)

        update()
        master.mainloop()