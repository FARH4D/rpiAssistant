import customtkinter
import tkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



root = customtkinter.CTk()
root.title("Home Assistant")
root.geometry("320x480")
# root.attributes('-fullscreen', True)

taskbar = customtkinter.CTkFrame(root, height = 60)
taskbar.pack(side='top', fill='x')

timeLabel = customtkinter.CTkLabel(taskbar, text = "13:09", font = ("Roboto", 18))
timeLabel.pack(side='left', padx=10)

dateLabel = customtkinter.CTkLabel(taskbar, text = "02/04/2023", font = ("Roboto", 18))
dateLabel.pack(side='right', padx=10)

greetingLabel = customtkinter.CTkLabel(root, text = "Good Morning!", font = ("Roboto", 23))
greetingLabel.pack(side='top', pady=15)

rectFrame = customtkinter.CTkFrame(root, width=250, height=75)
rectFrame.place(relx=0.5, rely=0.3, anchor='center')
rectFrame.grid_propagate(False)

tempLabel = customtkinter.CTkLabel(rectFrame, text = "Temperature: ", font = ("Roberto", 18))
humidLabel = customtkinter.CTkLabel(rectFrame, text = "Humidity: ", font = ("Roberto", 18))

tempLabel.grid(row=0, column = 0, padx = (10, 0))
humidLabel.grid(row=1, column = 0, pady = (10, 0))

root.mainloop()