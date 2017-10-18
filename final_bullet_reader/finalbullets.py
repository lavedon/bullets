from tkinter import *
from tkinter import filedialog
import logging
import pickle
import os

all_authors = []
configFileName = "config.p"
logging.basicConfig(filename='bullet_reader.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s:%(asctime)s')


class Author():
    """
    Author class contains all the loaded bullets.

    This class also contains a temporary list temp_bullets[].
    Bullets are removed from temp_bullets[] after they are displayed.
    Turning on rating mode resets this list.
    """
    _bulletCount = 1  # "How many of these bullet instances are created"

    def __init__(self, name, fileName, keybinding):
        self.my_number = Author._bulletCount
        self.name = name
        self.all_bullets = []  # loads all bullets for this author
        self.temp_bullets = []  # will remove bullets we have seen
        self.sorted_bullets = []
        self.keybinding = keybinding
        self.fileName = fileName
        self.rating_cutoff = 0
        Author._bulletCount += 1

    def __str__(self):
        """Display important object attributes."""

        display = "Author {0} #{1}.  Keybinding: {2}.  File Name {3}".format(
            self.name,
            self.my_number,
            self.keybinding,
            self.fileName)
        return display


def get_filename():
    """Open a tkinter window and return a file name."""
    root = Tk()
    fileName = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"),
                                                     ("All files", "*.*")))
    root.destroy()
    logging.info('Opened file: {}'.format(fileName))
    return fileName


def save_configuration():
    """
    Save the user configuration for the next session use.

    For examples saves what authors have been loaded into memory.
    Also save all_authors[].
    """
    print("Saving...")
    pickle.dump(all_authors, open(configFileName, "wb"))
    logging.info("Saved pickle file to '{}'".format(configFileName))


def load_configuration():
    """
    Load saved user configuration.

    If a JSON file exists with configuration
    Automatically loads that into memory.
    """
    #  @TODO use os.path to see if the file is in the directory
    global all_authors
    print("Loading config file....")
    all_authors = pickle.load(open(configFileName, "rb"))
    logging.info("Opened pickle config file from '{}'".format(configFileName))
    logging.info("all_authors now equals: {}".format(str(all_authors)))


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
        logging.info("Created an author object named {0}, from file: {1}, \
                        with keybinding{2}  ".format(newAuthor.name,
                                                     newAuthor.fileName,
                                                     newAuthor.keybinding))

        all_authors.append(newAuthor)
        logging.info("These many authors now exist: {} ".format(len(all_authors)))
    except Exception as e:
        print("Error loading file")
        print(e)
    #  Read the file and put bullets into a list
    try:
        newAuthor.all_bullets = file_to_lists(fileName)
        newAuthor.temp_bullets = newAuthor.all_bullets
        logging.info("Author {} has {} \
            .all_bullets and [] .temp_bullets".format(newAuthor.name,
                                                      newAuthor.fileName,
                                                      newAuthor.keybinding))
        # @TODO update author object with lists
    except Exception as e:
        print("Error assigning bullets to author object")
        print(e)


def file_to_lists(fileName):
    """
    Loads all bullets and returns a list.

    Accepts a string as filename.
    """
    try:
        logging.info("Called file_to_lists()")
        bulletList = []
        # Open the file. Strip out new line character.
        with open(fileName) as f:
            bullets = f.readlines()
            bullets = [x.strip() for x in bullets]

        for i in bullets:
            bulletList.append(i)
        logging.info("Added {} bullets to bulletlist".format(len(bulletList)))
        return bulletList
    except Exception as e:
        print("Error loading bullets")
        print(e)


def menu_help():
    """Display list of all commands."""
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
    """Read the users input then call the appropriate function."""
    if user_input.lower() == 'l':
        print("Loading author")
        load_author()
    elif user_input.lower() == 'q':
        save_configuration()
        print("Goodbye and good luck.")
        quit()
    elif user_input.lower() == 'h':
        menu_help()
    elif user_input.lower() == 's':
        save_configuration()
    elif user_input.lower() == 'lc':
        load_configuration()
    # else:
        #   Iterate through all authors see if a key was pressed


if __name__ == "__main__":
    print("Welcome to finished bullet rater")
    if os.path.exists(configFileName):
        load_configuration()
    while True:
        try:
            read_input(input("Enter Selection: "))
        except ValueError as e:
            print(e)
            read_input(input("Enter selection: "))
