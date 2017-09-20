# Count bullets written
# THIS DOES NOT YET WORK
from tkinter import *
from tkinter import filedialog
root = Tk()
fileName = filedialog.askopenfilename( filetypes = (("TEXT files", "*.txt"),
("All files", "*.*")))

with open(fileName, 'r') as f:
    lines = f.readlines()

# Print out what lines were read:
print("Printing out each line")
for i in lines:
    print(i)

# remove lines with ()
for i in lines:
    if '(' in i:
        print("found this: " + i)
        quit()
    if i == '':
        lines.pop(i)
print("Now I removed the knowledge bombs...\n")
print("Printing out what is left")
for i in lines:
    print(i)

print("You have: " + str(len(lines)) + "written so far")
