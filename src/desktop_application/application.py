import tkinter as tk

from tkinter import messagebox
from omegaconf import  OmegaConf

from src.utils import download_images_helper

class Application(tk.Frame):
    def __init__(self, srch_safari, srch_chrome, second_image, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.__srch_safari = srch_safari
        self.__srch_chrome = srch_chrome
        self.__second_image = second_image


    def create_widgets(self):
        self.path_label = tk.Label(self, text="Path")
        self.path_label.pack()
        self.path_entry = tk.Entry(self)
        self.path_entry.pack()

        self.keyword_label = tk.Label(self, text="Keyword")
        self.keyword_label.pack()
        self.keyword_entry = tk.Entry(self)
        self.keyword_entry.pack()

        self.num_images_label = tk.Label(self, text="Number of images")
        self.num_images_label.pack()
        self.num_images_entry = tk.Entry(self)
        self.num_images_entry.pack()

        self.run_button = tk.Button(self)
        self.run_button["text"] = "Download Images"
        self.run_button["command"] = self.download_images
        self.run_button.pack()

    def download_images(self):
        path = self.path_entry.get()
        keyword = self.keyword_entry.get()
        num_images = int(self.num_images_entry.get())

        config = {
            "save_path": path,
            "keyword": keyword,
            "num_images": num_images,
            "srch_chrome": self.__srch_chrome,
            "srch_safari": self.__srch_safari,
            "second_image": self.__second_image
        }
        config = OmegaConf.create(config)

        download_images_helper(config)
        messagebox.showinfo("Information", "Download completed successfully!")

