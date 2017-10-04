import os
import random
import csv
from tkinter import *
from tkinter import filedialog


class Author():
    """
    Author class contains all the loaded bullets.
    This class also contains a temporary list that bullets are removed
    from after they are displayed.  Turning on rating mode resets this list.
    """
    bulletCount = 0  # "How many of these bullet instances are created"

    def __init__(self, name, fileName):
        Author.bulletCount += 1
        self.name = name
        self.all_bullets = []  # loads all bullets for this author
        self.temp_bullets = []  # will remove bullets we have seen
        self.sorted_bullets = []
        self.keybinding = ""
        self.fileName = ""


def get_filename():
    """Opens a tkinter window and returns a file name."""

    root = Tk()
    fileName = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"),
                                                     ("All files", "*.*")))
    return fileName


# Main
if __name__ == "__main__":
    print("Welcome to finished bullet rater")
    while True:
        user_input = input("press key")
