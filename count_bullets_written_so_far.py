# Count bullets written
from tkinter import *
from tkinter import filedialog
root = Tk()
fileName = filedialog.askopenfilename( filetypes = (("TEXT files", "*.txt"),
("All files", "*.*")))

with open(fileName, 'r') as f:
    lines = f.readlines()


# remove lines with ()
for i in lines:
    if '(' in lines:
        del i
print("You have: " + len(lines) + "written so far")
