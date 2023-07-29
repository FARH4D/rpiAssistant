import customtkinter as ctk
from tkinter import *
from datetime import datetime, time


class intervalTimer(ctk.CTkFrame):

    def __init__(self, master, back_callback):
        super().__init__(master)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.master = master
        self.back_callback = back_callback
        #self.master.attributes('-fullscreen', True)

        self.intervalList = [None] * 3
        self.packItems()
        self.update()
        self.packButtons()

    def update(self):
        if self.updateCycle:
            now = datetime.now()
            currentTime = now.strftime("%H:%M")
            currentDate = now.strftime("%d/%m/%Y")
            self.timeLabel.configure(text=currentTime)
            self.dateLabel.configure(text=currentDate)
            self.master.after(3000, self.update)

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

    def assignValue(self, index, value):
        self.intervalList[index] = value

    def packButtons(self):
        self.container = ctk.CTkFrame(self.master)
        self.container.pack(side='top')
        self.titleLabel = ctk.CTkLabel(self.master, text = "INTERVAL TIMER", font = ("Roboto", 35))
        self.titleLabel.pack(side='top', pady=15, in_= self.container, anchor = "center")

        self.timer1 = ctk.CTkButton(self.master, text = "1:00", height = 80, width = 100, font = ("Roboto", 29), command=lambda: self.assignValue(0, "1:00"))
        self.timer1.place(x = -100, y = 150, in_= self.container, anchor = "center")
        self.timer2 = ctk.CTkButton(self.master, text = "2:00", height = 80, width = 100, font = ("Roboto", 29), command=lambda: self.assignValue(0, "2:00"))
        self.timer2.place(x = 50, y = 150, in_= self.container, anchor = "center")
        self.timer3 = ctk.CTkButton(self.master, text = "3:00", height = 80, width = 100, font = ("Roboto", 29), command=lambda: self.assignValue(0, "3:00"))
        self.timer3.place(x = 200, y = 150, in_= self.container, anchor = "center")
        self.timer4 = ctk.CTkButton(self.master, text = "Custom", height = 80, width = 100, font = ("Roboto", 29), command=lambda: self.enterCustom("timer"))
        self.timer4.place(x = 350, y = 150, in_= self.container, anchor = "center")

        self.roundsLabel = ctk.CTkLabel(self.master, text = "ROUNDS", font = ("Roboto", 32))
        self.roundsLabel.place(x = 125, y = 260, in_= self.container, anchor = "center")
        self.rounds1 = ctk.CTkButton(self.master, text = "1", height = 80, width = 100, font = ("Roboto", 29), command=lambda: self.assignValue(1, 1))
        self.rounds1.place(x = -100, y = 350, in_= self.container, anchor = "center")
        self.rounds2 = ctk.CTkButton(self.master, text = "3", height = 80, width = 100, font = ("Roboto", 29), command=lambda: self.assignValue(1, 3))
        self.rounds2.place(x = 50, y = 350, in_= self.container, anchor = "center")
        self.rounds3 = ctk.CTkButton(self.master, text = "5", height = 80, width = 100, font = ("Roboto", 29), command=lambda: self.assignValue(1, 5))
        self.rounds3.place(x = 200, y = 350, in_= self.container, anchor = "center")
        self.rounds4 = ctk.CTkButton(self.master, text = "Custom", height = 80, width = 100, font = ("Roboto", 29), command=lambda: self.enterCustom("rounds"))
        self.rounds4.place(x = 350, y = 350, in_= self.container, anchor = "center")

        self.restLabel = ctk.CTkLabel(self.master, text = "REST PERIODS", font = ("Roboto", 32))
        self.restLabel.place(x = 130 , y = 460, in_= self.container, anchor = "center")
        self.rest1 = ctk.CTkButton(self.master, text = "00:15", height = 80, width = 100, font = ("Roboto", 29), command=lambda: self.assignValue(2, "00:15"))
        self.rest1.place(x = -100, y = 550, in_= self.container, anchor = "center")
        self.rest2 = ctk.CTkButton(self.master, text = "00:30", height = 80, width = 100, font = ("Roboto", 29), command=lambda: self.assignValue(2, "00:30"))
        self.rest2.place(x = 50, y = 550, in_= self.container, anchor = "center")
        self.rest3 = ctk.CTkButton(self.master, text = "1:00", height = 80, width = 100, font = ("Roboto", 29), command=lambda: self.assignValue(2, "1:00"))
        self.rest3.place(x = 200, y = 550, in_= self.container, anchor = "center")
        self.rest4 = ctk.CTkButton(self.master, text = "Custom", height = 80, width = 100, font = ("Roboto", 29), command=lambda: self.enterCustom("rest"))
        self.rest4.place(x = 350, y = 550, in_= self.container, anchor = "center")

        self.startButton = ctk.CTkButton(self.master, text = "Start", height = 80, width = 120, font = ("Roboto", 29), command=lambda: self.startTimer())
        self.startButton.place(x = 125, y = 700, in_= self.container, anchor = "center")

    def startTimer(self):
        self.updateCycle = False
        self.taskbar.destroy()
        self.container.destroy()
        print(str(self.intervalList[0]) + " " + str(self.intervalList[1]) + " " + str(self.intervalList[2]))
        self.startLabel = ctk.CTkLabel(self.master, text = "TIMER STARTING IN", font = ("Roboto", 40))
        self.startLabel.pack(side='top', pady=50)
        self.startTimeLabel = ctk.CTkLabel(self.master, text = "3", font = ("Roboto", 40))
        self.startTimeLabel.pack(side='top', pady=40)

        self.master.update_idletasks()  # The labels do not normally update until the below timer has passed, so this forces the GUI to undergo an immediate update.

        self.master.after(1000, lambda: self.startTimeLabel.configure(text= "2"))
        self.master.after(2000, lambda: self.startTimeLabel.configure(text= "1"))
        self.master.after(3000, lambda: self.startTimeLabel.configure(text= "STARTING"))
        self.master.after(4000, self.timerStarted)

    def timerStarted(self):
        self.startLabel.destroy()
        self.startTimeLabel.destroy()
        self.packItems()
        self.homeButton.destroy()
        self.update()

        self.countdownNum = self.calculateTime(self.intervalList[0])

        self.currentTime = ctk.CTkLabel(self.master, text = self.intervalList[0], font = ("Roboto", 60))
        self.currentTime.pack(side='top', pady=120)

        self.endTimer = ctk.CTkButton(self.master, text = "Finish", height = 35, width = 160, font = ("Roboto", 40), command=lambda: self.endEarly())
        self.endTimer.pack(side='top')
        
        self.countdown(self.countdownNum)
        self.resting = False

    def calculateTime(self, time):
        formattedTime = str(time).split(":", 1)
        realTime = (int(formattedTime[0]) * 60) + (int(formattedTime[1]))
        return realTime

    def countdown(self, time):
        if time >= 0:
            self.currentTime.configure(text=time)
            self.setTimerLabel(time)
            time -= 1
            self.master.after(1000, lambda: self.countdown(time))
        else:
            if self.resting == True:
                self.resting = False
                self.restLabel.destroy()
                self.countdown(self.countdownNum)
            else:
                if self.intervalList[1] > 1:
                    self.rest()
                    self.intervalList[1] -= 1
                else:
                    self.currentTime.configure(text = "FINISHED")
            

    def rest(self):
        self.resting = True
        self.restTime = self.calculateTime(self.intervalList[2])
        self.countdown(self.restTime)

        self.restLabel = ctk.CTkLabel(self.master, text = "REST PERIOD", font = ("Roboto", 60))
        self.restLabel.pack(side='top', pady=120)
        

    def setTimerLabel(self, time):
        mins = int(time / 60)
        secs = (time  - (mins * 60)) % 60

        self.currentTime.configure(text = "{:02d}".format(mins) + ":" + "{:02d}".format(secs))

    def endEarly(self):

        self.currentTime.destroy()
        self.endTimer.destroy()
        self.taskbar.destroy()
        self.updateCycle = False
        self.rebuild()

    def enterCustom(self, type):

        self.type = type
        self.pointer = 0
        self.updateCycle = False
        self.taskbar.destroy()
        self.container.destroy()

        self.customTimer = [0, 0, 0, 0]
        
        self.customContainer = ctk.CTkFrame(self.master)
        self.customContainer.pack(side='top')

        self.customTitle = ctk.CTkLabel(self.master, text = "ENTER A TIME", font = ("Roboto", 35))
        self.customTitle.pack(side='top', pady=15, in_= self.customContainer, anchor = "center")

        self.customNumDisplay = ctk.CTkLabel(self.master, text = "", font = ("Roboto", 56))
        self.customNumDisplay.pack(side='top', pady=20, in_= self.customContainer, anchor = "center")

        if type == "timer" or type == "rest":
            self.customNumDisplay.configure(text = "00:00")
        else:
            self.customNumDisplay.configure(text = "00")

        self.num1 = ctk.CTkButton(self.master, text = "1", height = 80, width = 100, font = ("Roboto", 35), command=lambda: self.addCustom(1))
        self.num1.place(x = -40, y = 250, in_= self.customContainer, anchor = "center")
        self.num2 = ctk.CTkButton(self.master, text = "2", height = 80, width = 100, font = ("Roboto", 35), command=lambda: self.addCustom(2))
        self.num2.place(x = 110, y = 250, in_= self.customContainer, anchor = "center")
        self.num3 = ctk.CTkButton(self.master, text = "3", height = 80, width = 100, font = ("Roboto", 35), command=lambda: self.addCustom(3))
        self.num3.place(x = 260, y = 250, in_= self.customContainer, anchor = "center")

        self.num4 = ctk.CTkButton(self.master, text = "4", height = 80, width = 100, font = ("Roboto", 35), command=lambda: self.addCustom(4))
        self.num4.place(x = -40, y = 400, in_= self.customContainer, anchor = "center")
        self.num5 = ctk.CTkButton(self.master, text = "5", height = 80, width = 100, font = ("Roboto", 35), command=lambda: self.addCustom(5))
        self.num5.place(x = 110, y = 400, in_= self.customContainer, anchor = "center")
        self.num6 = ctk.CTkButton(self.master, text = "6", height = 80, width = 100, font = ("Roboto", 35), command=lambda: self.addCustom(6))
        self.num6.place(x = 260, y = 400, in_= self.customContainer, anchor = "center")

        self.num7 = ctk.CTkButton(self.master, text = "7", height = 80, width = 100, font = ("Roboto", 35), command=lambda: self.addCustom(7))
        self.num7.place(x = -40, y = 550, in_= self.customContainer, anchor = "center")
        self.num8 = ctk.CTkButton(self.master, text = "8", height = 80, width = 100, font = ("Roboto", 35), command=lambda: self.addCustom(8))
        self.num8.place(x = 110, y = 550, in_= self.customContainer, anchor = "center")
        self.num9 = ctk.CTkButton(self.master, text = "9", height = 80, width = 100, font = ("Roboto", 35), command=lambda: self.addCustom(9))
        self.num9.place(x = 260, y = 550, in_= self.customContainer, anchor = "center")

        self.num0 = ctk.CTkButton(self.master, text = "0", height = 80, width = 100, font = ("Roboto", 35), command=lambda: self.addCustom(0))
        self.num0.place(x = -40, y = 700, in_= self.customContainer, anchor = "center")
        self.addNum = ctk.CTkButton(self.master, text = "Confirm", height = 80, width = 100, font = ("Roboto", 35), command=lambda: self.confirmCustom())
        self.addNum.place(x = 110, y = 700, in_= self.customContainer, anchor = "center")
        self.deleteNum = ctk.CTkButton(self.master, text = "Delete", height = 80, width = 100, font = ("Roboto", 35), command=lambda: self.removeCustom())
        self.deleteNum.place(x = 260, y = 700, in_= self.customContainer, anchor = "center")

    def addCustom(self, number):
        if self.type == "timer" or self.type == "rest":
            if self.pointer > 3:
                pass
            else:
                self.customTimer[self.pointer] = number
                self.pointer += 1
                self.customNumDisplay.configure(text = str(self.customTimer[0]) + str(self.customTimer[1]) + ":" + str(self.customTimer[2]) + str(self.customTimer[3]))
        else:
            if self.pointer > 1:
                pass
            else:
                self.customTimer[self.pointer] = number
                self.pointer += 1
                self.customNumDisplay.configure(text = str(self.customTimer[0]) + str(self.customTimer[1]))
    
    def removeCustom(self):
        if self.type == "timer" or self.type == "rest":
            if self.pointer - 1 < 0:
                self.pointer = 0
            else:
                self.pointer -= 1
                self.customTimer[self.pointer] = 0
                self.customNumDisplay.configure(text = str(self.customTimer[0]) + str(self.customTimer[1]) + ":" + str(self.customTimer[2]) + str(self.customTimer[3]))
        else:
            if self.pointer - 1 < 0:
                self.pointer = 0
            else:
                self.pointer -= 1
                self.customTimer[self.pointer] = 0
                self.customNumDisplay.configure(text = str(self.customTimer[0]) + str(self.customTimer[1]))
            
    
    def confirmCustom(self):
        if self.type == "timer":
            customTimerLocal = str(str(self.customTimer[0]) + str(self.customTimer[1]) + ":" + str(self.customTimer[2]) + str(self.customTimer[3]))
            self.assignValue(0, customTimerLocal)
        elif self.type == "rounds":
            customRoundsLocal = int(str(self.customTimer[0]) + str(self.customTimer[1]))
            self.assignValue(1, customRoundsLocal)
        else:
            customTimerLocal = str(str(self.customTimer[0]) + str(self.customTimer[1]) + ":" + str(self.customTimer[2]) + str(self.customTimer[3]))
            self.assignValue(2, customTimerLocal)
        self.customContainer.destroy()
        self.rebuild()

    def rebuild(self):
        self.packItems()
        self.update()
        self.packButtons()

    def back_to_home(self):
        # Execute the callback function to go back to the home menu
        self.taskbar.pack_forget()
        self.container.pack_forget()
        self.back_callback()
