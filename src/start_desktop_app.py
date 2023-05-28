
import tkinter as tk
from src.desktop_application import Application


def start_desktop_app(config):
    root = tk.Tk()
    app = Application(config["srch_safari"], config["srch_chrome"], config["second_image"],  master=root)
    app.mainloop()
