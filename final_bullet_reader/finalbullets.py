from tkinter import *
from tkinter import filedialog
import logging
import pickle
import os
import random

#  @TODO add globals to a user profile object.
all_authors = []
RATING_MODE_TOGGLE = False
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
        self.temp_bullets = []  # will remove bullets we have seen.  Copies over from all_bullets when this mode is activated.
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
    #  @TODO pickle the author # and make it work.
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
        # @TODO make bullets a 2d array not just a list of strings
        with open(fileName) as f:
            bullets = f.readlines()
            bullets = [bullet.strip() for bullet in bullets]
            #  Makes bullets a 2d array, string of bullet and
            for i in bullets:
                new_bullets = []
                new_bullets.append(i)
                new_bullets.append(0)
                bulletList.append(new_bullets)
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
    global RATING_MODE_TOGGLE
    global SORT_BY_RATING_TOGGLE

    for author in all_authors:
        if author.keybinding == user_input.lower():
            logging.info("User selected {0} by pressing {1}".format(author, user_input))
            process_bullet(author)

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
    elif user_input.lower() == 'r':
        RATING_MODE_TOGGLE = True
        print("Rating mode on")
        logging.info("RATING_MODE_TOGGLE now set to: ".format(RATING_MODE_TOGGLE))
    elif user_input.lower() == 'sort'
        print("Sort by rating toggle now on")
        SORT_BY_RATING_TOGGLE = True
        logging.info("Sort bullets by rating now on.")
        logging.info("Now call return_bullets_by_rating bullets by rating()".format()
    elif user_input.lower() == 'del':
        delete_author()
    else:
        return


def delete_author():
    global all_authors
    user_input=input("Enter key for author you would like to delete:")
    for author in all_authors:
        if author.keybinding == user_input.lower():
            all_authors.remove(author)


def rate_me(bullet, bullet_num):
    """  Adds a rating to the selected bullet. """

    logging.info("Rate me called.")
    print("Current rating is: " + str(bullet[1]))  # @TODO Change this to all.authors with bullet_num
    user_input=input("enter a rating between 1 - 5: ")

    try:
        if 1 <= int(user_input) <= 5:
            logging.info("user_input is a rating of:" + str(user_input))
            rating=int(user_input)
        else:
            print("Not a valid rating (Not a integer)")
        return rating
    except NameError:
        logging.info("rate_me() threw NameError")
        print("Input was not a digit - please try again.")
    except ValueError:
        logging.info("rate_me() threw ValueError")
        print("Not a valid rating")


def process_bullet(author):
    """ pass in whichever author the user chose

    First evaluates if rating mode is activated.  If so
    then calls the rate_me function with the correct bullet list
    """

    #  @TODO change author.all_bullets to a temporary variabe.
    #  Check which mode is turned on.  If temp_bullets i.e.
    #  Delete your bullet after rating.  Make variabe =
    #  author.temp_bullets NOT author.all_bullets

    bullet_num=int(random.randrange(len(author.all_bullets)))
    bullet=author.all_bullets[int(bullet_num)]
    #  Check if rating mode is activated if so pass the bullet
    #  along to rate_me()

    if RATING_MODE_TOGGLE == True:

        print(bullet[0])
        # set the bullet rating in the 2D array - to returned value from rate_me()
        author.all_bullets[bullet_num][1]=rate_me(bullet, bullet_num)
        #  are we not going to need to pass author also?
        print("You rated: \n" + str(author.all_bullets[bullet_num][0]) + "\n" + str(author.all_bullets[bullet_num][1]))

    else:
        print(bullet[0])


def return_bullets_by_rating(bullets, rating):
    """
    Takes the authors bullets and rating integer
    the user requests.  Iterates through all bullets
    and returns only those equal to and above a
    certain rating.
    """
    rated_bullets=[bullet for bullet in bullets if int(bullet[1]) >= int(rating)]
    return rated_bullets


def sort_bullets():
    """
    Call this function once the user decides to turn on sort by
    rating mode.  A sub-routine not a function.

    Asks the user what author he wants to sort and by what rating he would like to sort.  Passes author and rating selection to return_bullets_by_rating.  Updates the author object with the sorted bullets.  author.sorted_bullets = return_bullets_by_rating(author, rating)
    """


if __name__ == "__main__":
    main()


def main():
    print("Welcome to finished bullet rater")
    if os.path.exists(configFileName):
        load_configuration()
    while True:
        try:
            read_input(input("Enter Selection: "))
        except ValueError as e:
            print(e)
            read_input(input("Enter selection: "))


# @TODO turn on temp mode
