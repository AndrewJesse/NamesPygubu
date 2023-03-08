# Author: Andrew Marchese
# Date: 3/8/2023
# Title: Lab 9 GUI Part II
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

    # Initiate controls and main UI
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
        # Visual arrangement for the Treeview
        tree = self._tree
        self.create_treeview_style()
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

    @staticmethod
    def create_treeview_style():
        # noinspection PyUnresolvedReferences
        style = tk.ttk.Style()

        # fix for bug in alternating colors in Treeview in later versions of tkinter
        # see https://bugs.python.org/issue36468 for details
        style.map('Treeview', foreground=BrowserApp.fixed_map('foreground', style),
                  background=BrowserApp.fixed_map('background', style))

        style.element_create("Custom.Treeheading.border", "from", "default")
        style.layout("Custom.Treeview.Heading", [
            ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
            ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
                ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
                    ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
                    ("Custom.Treeheading.text", {'sticky': 'we'})
                ]})
            ]}),
        ])
        style.configure("Custom.Treeview.Heading",
                        background="dark blue", foreground="white", relief="flat", font=('Arial Black', 10, 'bold'))
        style.map("Custom.Treeview.Heading",
                  relief=[('active', 'groove'), ('pressed', 'sunken')])
        # Set the background color of the treeview to light gray
        style.configure("Treeview", background="light gray")
        return style
    # Fix bug in alternating colors in Treeview for later versions of tkinter
    @staticmethod
    def fixed_map(option, style):
        # Fix for setting text colour for Tkinter 8.6.9
        # From: https://core.tcl.tk/tk/info/509cafafae
        #
        # Returns the style map for 'option' with any styles starting with
        # ('!disabled', '!selected', ...) filtered out.

        # style.map() returns an empty list for missing options, so this
        # should be future-safe.
        return [elm for elm in style.map('Treeview', query_opt=option) if
                elm[:2] != ('!disabled', '!selected')]
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
