# from tkinter import *
from tkinter import filedialog

all_authors = []


class Author():
    """
    Author class contains all the loaded bullets.
    This class also contains a temporary list that bullets are removed
    from after they are displayed.  Turning on rating mode resets this list.
    """
    global bulletCount
    bulletCount = 0  # "How many of these bullet instances are created"

    def __init__(self, name, fileName, keybinding):
        Author.bulletCount += 1
        self.name = name
        self.all_bullets = []  # loads all bullets for this author
        self.temp_bullets = []  # will remove bullets we have seen
        self.sorted_bullets = []
        self.keybinding = ""
        self.fileName = ""

    def __str__(self):
        print("Author {0} #{1}.  Keybinding: {2}.  File Name {3}".format(
                                                            self.name,
                                                            bulletCount,
                                                            self.keybinding,
                                                            self.fileName
                                                            ))


def get_filename():
    """Opens a tkinter window and returns a file name."""

    root = Tk()
    fileName = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"),
                                                     ("All files", "*.*")))
    root.destroy()
    return fileName


def save_selection():
    """Saves the user configuration for the next session use.
    For examples saves what authors have been loaded into memory.
    """
    pass


def load_author():
    """
    Create a new author object from Author class.
    Append this new author object to all_authors = [].
    """
    try:
        fileName = get_filename()
        print("Loading file... " + fileName)
        authorName = input("What would you like to name this author?: ")
        keyBinding = input("What key would you like to bind to this author?: ")
        newAuthor = Author(authorName, fileName, keyBinding)
        all_authors.append(newAuthor)
    except Exception as e:
        print("Error loading file")
        print(e)


def load_configuration():
    """
    Loads the user configuration.  If a JSON file exists with configuration
    Automatically loads that into memory.
    """


def help():
    """Displays a list of all commands"""
    print("Help:")
    print("Press L to load an author.")
    print("Press Q to quit.")
    try:
        if all_authors:
            #  If this list is not empty. If there is at least 1 author object
            #  in the list.
            print("Current Authors:")
            for author in all_authors:  # Iterate through author objects
                print(str(author))
    except Error as e:
        print(e)


def read_input(user_input):
    """
    Read the users input then calls the appropriate function
    """
    if user_input.lower() == 'l':
        print("Loading author")
        load_author()
    elif user_input.lower() == 'q':
        print("Goodbye and good luck.")
        quit()
    elif user_input.lower() == 'h':
        help()


# Main
if __name__ == "__main__":
    print("Welcome to finished bullet rater")

    while True:
        try:
            read_input(input("Enter Selection: "))
        except ValueError as e:
            print(e)
            read_input(input("Enter selection: "))
