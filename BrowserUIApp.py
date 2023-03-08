#!/usr/bin/python3
import pathlib
import tkinter as tk
from tkinter import ttk
from Name import *

import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "browser.ui"


class BrowserApp:
    def __init__(self, parent):
        self.init_ui(parent)
        self.setup_tree()
        self.search_button = ttk.Button(parent, command=self.search_name)

    def init_ui(self, parent):
        builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("top_level", parent)
        builder.connect_callbacks(self)

        # retrieves the radio button widget object using the get_object() method of the Builder() object and assigns
        # it to an instance variable for later use in callbacks.
        self._builder = builder
        self._male_button = builder.get_object('male_radio', parent)
        self._female_button = builder.get_object('female_radio', parent)
        self._name_entry = builder.get_object('name_entry', parent)

        # Create a new instance of a tkinter string variable to hold the selected gender
        self.gender_var = tk.StringVar()

        # Configure the female radio button to use the gender variable and set its value to "F"
        self._builder.get_object("female_radio").config(variable=self.gender_var, value="F")

        # Configure the male radio button to use the gender variable and set its value to "M"
        self._builder.get_object("male_radio").config(variable=self.gender_var, value="M")
        self._tree = builder.get_object('name_tree', parent)

    def setup_tree(self):
        tree = self._tree
        tree.configure(columns=(0, 1, 2, 3, 4), displaycolumns=(0, 1, 2, 3, 4))
        tree.heading(0, text="Name", anchor=tk.W)
        tree.heading(1, text="Year")
        tree.heading(2, text="Gender")
        tree.heading(3, text="Count")
        tree.heading(4, text="Total")
        tree.column(0, width=100)
        tree.column(1, anchor=tk.CENTER, width=100)
        tree.column(2, anchor=tk.CENTER, width=100)
        tree.column(3, anchor=tk.CENTER, width=100)
        tree.column(4, anchor=tk.CENTER, width=100)

    def search_name(self):
        name = self._name_entry.get()
        gender = self.gender_var.get()

        # Delete all existing items from the tree
        self._tree.delete(*self._tree.get_children())

        names = Name.fetch_names(name, gender)
        self.insert_names_to_tree(names)

    def insert_names_to_tree(self, names):
        for name in names:
            self._tree.insert("", tk.END, values=(
                name.get_name(),
                name.get_year(),
                name.get_gender(),
                name.get_name_count(),
                name.get_total()))

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = BrowserApp(root)
    app.run()
