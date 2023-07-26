import customtkinter
from tkinter import *
from datetime import datetime, time


class deviceControl(customtkinter.CTkFrame):

    def __init__(self, master):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.master = master
        self.master.geometry("768x1024")
        self.master.title("Home Assistant")
        #self.master.attributes('-fullscreen', True)
