import customtkinter
from tkinter import *
from datetime import datetime, time


class intervalTimer(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.master = master
        self.master.geometry("320x480")
        self.master.title("Home Assistant")
        #self.root.attributes('-fullscreen', True)

        self.intervalList = [None] * 3

        self.packItems()
        self.update()
        self.packButtons()
        self.master.mainloop()


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
        self.taskbar = customtkinter.CTkFrame(self.master, height = 60)
        self.taskbar.pack(side='top', fill='x')

        self.timeLabel = customtkinter.CTkLabel(self.taskbar, text = "", font = ("Roboto", 18))
        self.timeLabel.pack(side='left', padx=10)

        self.homeIcon = PhotoImage(file='rpiAssistant/images/homeIcon.png')

        self.homeButton = customtkinter.CTkButton(self.taskbar, image=self.homeIcon, text = "", command=lambda: self.goHome())
        self.homeButton.configure(height=20, width=20)
        self.homeButton.place(x= 140, y = 0)


        self.dateLabel = customtkinter.CTkLabel(self.taskbar, text = "", font = ("Roboto", 18))
        self.dateLabel.pack(side='right', padx=10)

        self.container = customtkinter.CTkFrame(self.master)
        self.container.pack(side='top')
        self.titleLabel = customtkinter.CTkLabel(self.master, text = "INTERVAL TIMER", font = ("Roboto", 23))
        self.titleLabel.pack(side='top', pady=15, in_= self.container, anchor = "center")

    def assignValue(self, index, value):
        self.intervalList[index] = value

    def packButtons(self):
        self.timer1 = customtkinter.CTkButton(self.master, text = "1:00", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.assignValue(0, "1:00"))
        self.timer1.place(x = -15, y = 90, in_= self.container, anchor = "center")
        self.timer2 = customtkinter.CTkButton(self.master, text = "3:00", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.assignValue(0, "3:00"))
        self.timer2.place(x = 85, y = 90, in_= self.container, anchor = "center")
        self.timer3 = customtkinter.CTkButton(self.master, text = "Custom", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.enterCustom("timer"))
        self.timer3.place(x = 190, y = 90, in_= self.container, anchor = "center")

        self.roundsLabel = customtkinter.CTkLabel(self.master, text = "ROUNDS", font = ("Roboto", 20))
        self.roundsLabel.place(x = 85 , y = 150, in_= self.container, anchor = "center")
        self.rounds1 = customtkinter.CTkButton(self.master, text = "1", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.assignValue(1, 1))
        self.rounds1.place(x = -15, y = 210, in_= self.container, anchor = "center")
        self.rounds2 = customtkinter.CTkButton(self.master, text = "3", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.assignValue(1, 3))
        self.rounds2.place(x = 85, y = 210, in_= self.container, anchor = "center")
        self.rounds3 = customtkinter.CTkButton(self.master, text = "Custom", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.enterCustom("rounds"))
        self.rounds3.place(x = 190, y = 210, in_= self.container, anchor = "center")

        self.restLabel = customtkinter.CTkLabel(self.master, text = "REST PERIODS", font = ("Roboto", 20))
        self.restLabel.place(x = 90 , y = 270, in_= self.container, anchor = "center")
        self.rest1 = customtkinter.CTkButton(self.master, text = "15", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.assignValue(2, "00:15"))
        self.rest1.place(x = -15, y = 325, in_= self.container, anchor = "center")
        self.rest2 = customtkinter.CTkButton(self.master, text = "30", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.assignValue(2, "00:30"))
        self.rest2.place(x = 85, y = 325, in_= self.container, anchor = "center")
        self.rest3 = customtkinter.CTkButton(self.master, text = "Custom", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.enterCustom("rest"))
        self.rest3.place(x = 190, y = 325, in_= self.container, anchor = "center")

        self.startButton = customtkinter.CTkButton(self.master, text = "Start", height = 60, width = 100, font = ("Roboto", 25), command=lambda: self.startTimer())
        self.startButton.place(x = 85, y = 405, in_= self.container, anchor = "center")

    def startTimer(self):
        self.updateCycle = False
        self.taskbar.destroy()
        self.container.destroy()
        print(str(self.intervalList[0]) + " " + str(self.intervalList[1]) + " " + str(self.intervalList[2]))
        self.startLabel = customtkinter.CTkLabel(self.master, text = "TIMER STARTING IN", font = ("Roboto", 23))
        self.startLabel.pack(side='top', pady=15)
        self.startTimeLabel = customtkinter.CTkLabel(self.master, text = "3", font = ("Roboto", 23))
        self.startTimeLabel.pack(side='top', pady=15)

        self.master.update_idletasks()  # The labels do not normally update until the below timer has passed, so this forces the GUI to undergo an immediate update.

        self.master.after(1000, lambda: self.startTimeLabel.configure(text= "2"))
        self.master.after(2000, lambda: self.startTimeLabel.configure(text= "1"))
        self.master.after(3000, lambda: self.startTimeLabel.configure(text= "STARTING"))
        self.master.after(4000, self.timerStarted)

    def timerStarted(self):
        self.startLabel.destroy()
        self.startTimeLabel.destroy()

        countdownNums = str(self.intervalList[0]).split(":", 1)

        self.countdownNum = (int(countdownNums[0]) * 60) + (int(countdownNums[1]))

        self.currentTime = customtkinter.CTkLabel(self.master, text = self.intervalList[0], font = ("Roboto", 23))
        self.currentTime.pack(side='top', pady=15)
        self.currentTime2 = customtkinter.CTkLabel(self.master, text = self.intervalList[0], font = ("Roboto", 23))
        self.currentTime2.pack(side='top', pady=15)
        
        self.countdown()

    def countdown(self):
        if self.countdownNum >= 0:
            self.currentTime.configure(text=self.countdownNum)
            self.setTimerLabel()
            self.countdownNum -= 1
            self.master.after(1000, self.countdown)
        else:
            self.currentTime.configure(text="FINISHED")

    def setTimerLabel(self):
        mins = int(self.countdownNum / 60)
        secs = (self.countdownNum  - (mins * 60)) % 60
        
        if secs == 0:
            self.currentTime2.configure(text = str(mins) + ":00")
        elif secs < 10:
            self.currentTime2.configure(text = str(mins) + ":0" + str(secs))
        else:
            self.currentTime2.configure(text = str(mins) + ":" + str(secs))


    def enterCustom(self, type):

        self.type = type
        self.pointer = 0
        self.updateCycle = False
        self.taskbar.destroy()
        self.container.destroy()

        self.customTimer = [0, 0, 0, 0]
        
        self.customContainer = customtkinter.CTkFrame(self.master)
        self.customContainer.pack(side='top')

        self.customTitle = customtkinter.CTkLabel(self.master, text = "ENTER A TIME", font = ("Roboto", 23))
        self.customTitle.pack(side='top', pady=15, in_= self.customContainer, anchor = "center")

        self.customNumDisplay = customtkinter.CTkLabel(self.master, text = "", font = ("Roboto", 40))
        self.customNumDisplay.place(x = 72, y = 100, in_= self.customContainer, anchor = "center")

        if type == "timer" or type == "rest":
            self.customNumDisplay.configure(text = "00:00")
        else:
            self.customNumDisplay.configure(text = "00")

        self.num1 = customtkinter.CTkButton(self.master, text = "1", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.addCustom(1))
        self.num1.place(x = -27, y = 180, in_= self.customContainer, anchor = "center")
        self.num2 = customtkinter.CTkButton(self.master, text = "2", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.addCustom(2))
        self.num2.place(x = 73, y = 180, in_= self.customContainer, anchor = "center")
        self.num3 = customtkinter.CTkButton(self.master, text = "3", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.addCustom(3))
        self.num3.place(x = 178, y = 180, in_= self.customContainer, anchor = "center")

        self.num4 = customtkinter.CTkButton(self.master, text = "4", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.addCustom(4))
        self.num4.place(x = -27, y = 265, in_= self.customContainer, anchor = "center")
        self.num5 = customtkinter.CTkButton(self.master, text = "5", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.addCustom(5))
        self.num5.place(x = 73, y = 265, in_= self.customContainer, anchor = "center")
        self.num6 = customtkinter.CTkButton(self.master, text = "6", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.addCustom(6))
        self.num6.place(x = 178, y = 265, in_= self.customContainer, anchor = "center")

        self.num7 = customtkinter.CTkButton(self.master, text = "7", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.addCustom(7))
        self.num7.place(x = -27, y = 350, in_= self.customContainer, anchor = "center")
        self.num8 = customtkinter.CTkButton(self.master, text = "8", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.addCustom(8))
        self.num8.place(x = 73, y = 350, in_= self.customContainer, anchor = "center")
        self.num9 = customtkinter.CTkButton(self.master, text = "9", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.addCustom(9))
        self.num9.place(x = 178, y = 350, in_= self.customContainer, anchor = "center")

        self.num0 = customtkinter.CTkButton(self.master, text = "0", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.addCustom(0))
        self.num0.place(x = -27, y = 435, in_= self.customContainer, anchor = "center")
        self.addNum = customtkinter.CTkButton(self.master, text = "Confirm", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.confirmCustom())
        self.addNum.place(x = 73, y = 435, in_= self.customContainer, anchor = "center")
        self.deleteNum = customtkinter.CTkButton(self.master, text = "Delete", height = 60, width = 80, font = ("Roboto", 23), command=lambda: self.removeCustom())
        self.deleteNum.place(x = 178, y = 435, in_= self.customContainer, anchor = "center")

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

    def goHome(self):
        self.master.destroy()

    def run(self):
        self.master.mainloop()

root = customtkinter.CTk()
interval = intervalTimer(root)
interval.run()