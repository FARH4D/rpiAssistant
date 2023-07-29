import customtkinter as ctk
from tkinter import Tk
from home import home

if __name__ == "__main__":
    root = ctk.CTk()
    main_menu = home(root)
    root.mainloop()