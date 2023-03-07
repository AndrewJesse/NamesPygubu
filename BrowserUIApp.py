#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "browser.ui"


class BrowserApp:
    def __init__(self, parent):
        self.start_ui(parent)


    def start_ui(self, parent):
        builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("top_level", parent)
        builder.connect_callbacks(self)

        # retrieves the radio button widget object using the get_object() method of the Builder() object and assigns it to an instance variable for later use in callbacks.
        self.builder = builder
        self.male_button = builder.get_object('male_radio', parent)
        self.female_button = builder.get_object('female_radio', parent)
        self.name_entry = builder.get_object('name_entry', parent)

    def _search_names(self):
        pass










        # Create a new instance of a tkinter string variable to hold the selected gender
        self.gender_var = tk.StringVar()

        # Configure the female radio button to use the gender variable and set its value to "F"
        self.builder.get_object("female_radio").config(variable=self.gender_var, value="F")

        # Configure the male radio button to use the gender variable and set its value to "M"
        self.builder.get_object("male_radio").config(variable=self.gender_var, value="M")


    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = BrowserApp(root)
    app.run()
