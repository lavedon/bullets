from tkinter import *
from tkinter import filedialog
import logging
import pickle
import os
import random
import csv

#  @TODO add globals to a user profile object.
all_authors = []
RATING_MODE_TOGGLE = False
SORT_BY_RATING_TOGGLE = False
ONLY_SHOW_ONCE_TOGGLE = False
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
        #  self.temp_bullets = []  # will remove bullets we have seen.  Copies over from all_bullets when this mode is activated.
        self.sorted_bullets = []
        # self.sorted_temp_bullets = []
        self.keybinding = keybinding
        self.fileName = fileName
        self.rating_cutoff = 0
        #  When SORT_BY_RATING_TOGGLE = True
        #  self.rating_cutoff = # to not return
        #  bullets below
        #  self.temp_rating_mode = False
        #  @TODO Add self.temp to save unique bullets with an #  author object rating on and off.
        self.bullets_returned_so_far = []
        #  turn on temp_rating_mode when you want
        #  author to delete bullets after displaying them.
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
        #  newAuthor.temp_bullets = newAuthor.all_bullets
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
    print("L to load an author.")
    print("Q to quit.")
    print("'sort' to sort by rating.")
    print("R to turn on rating mode.")
    print("S to save")
    print("'Only' Only show bullets once mode.")
    print("'lc' to load a pickle file")
    print("'export' to export a CSV file")
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
    global ONLY_SHOW_ONCE_TOGGLE

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
        # Pickle all author objects
        save_configuration()
    elif user_input.lower() == 'lc':
        load_configuration()
    elif user_input.lower() == 'r':
        #  Turn on rating mode
        if RATING_MODE_TOGGLE:
            RATING_MODE_TOGGLE = False
            print("Rating mode off")
        else:
            RATING_MODE_TOGGLE = True
            print("Rating mode on")
        logging.info("RATING_MODE_TOGGLE now set to: ".format(RATING_MODE_TOGGLE))
    elif user_input.lower() == 'sort':
        #  Turn on sort by rating
        print("Sort bullets by rating")
        if SORT_BY_RATING_TOGGLE:
            SORT_BY_RATING_TOGGLE = False
            print("Turning off sorted bullets")
        else:
            SORT_BY_RATING_TOGGLE = True
            print("Now displaying sorted bullets")
            sort_bullets()
        logging.info("Sort bullets by rating togge is {}".format(SORT_BY_RATING_TOGGLE))

    elif user_input.lower() == 'del':
        delete_author()

    elif user_input.lower() == 'only':
        if ONLY_SHOW_ONCE_TOGGLE:
            print("Will show  bullets multiple times")
            ONLY_SHOW_ONCE_TOGGLE = False
        else:
            ONLY_SHOW_ONCE_TOGGLE = True
            logging.info("ONLY_SHOW_ONCE_TOGGLE now = {}".format(ONLY_SHOW_ONCE_TOGGLE))
            print("Will now only show new, unique bullets.")

    elif user_input.lower() == 'export':
        print("Exporting a CSV file")
        save_file()
    else:
        return


def delete_author():
    global all_authors
    user_input = input("Enter key for author you would like to delete:")
    for author in all_authors:
        if author.keybinding == user_input.lower():
            all_authors.remove(author)


def rate_me(bullet, bullet_num):
    """  Adds a rating to the selected bullet. """

    logging.info("Rate me called.")
    print("Current rating is: " + str(bullet[1]))  # @TODO Change this to all.authors with bullet_num
    user_input = input("enter a rating between 1 - 5: ")

    try:
        if 1 <= int(user_input) <= 5:
            logging.info("user_input is a rating of:" + str(user_input))
            rating = int(user_input)
        else:
            print("Not a valid rating (Not a integer)")
        return rating
    except NameError:
        logging.info("rate_me() threw NameError")
        print("Input was not a digit - please try again.")
    except ValueError:
        logging.info("rate_me() threw ValueError")
        print("Not a valid rating")


def get_bullets(author):
    """Returns correct bullets to use"""
    if SORT_BY_RATING_TOGGLE and author.sorted_bullets:
        bullets = author.sorted_bullets
    else:
        bullets = author.all_bullets

    return bullets


def get_bullet_num(author):
    """ Takes an author and returns a bullet number"""
    bullets = get_bullets(author)
    bullet_num = bullet_num = int(random.randrange(len(bullets)))
    return bullet_num


def process_bullet(author):
    """ pass in whichever author the user chose

    First evaluates if rating mode is activated.  If so
    then calls the rate_me function with the correct bullet list
    """

    #  Clean up this code!

    #  Now process bullets
    bullet_num = get_bullet_num(author)
    if ONLY_SHOW_ONCE_TOGGLE and len(author.all_bullets) != len(author.bullets_returned_so_far):
        try:
            while bullet_num in author.bullets_returned_so_far:
                bullet_num = get_bullet_num(author)
        except Exception as e:
            logging.info("Problem with {0}'s not repeating bullets {1}".format(author.name, e))
    elif len(author.all_bullets) == len(author.bullets_returned_so_far):
        print("Shown all of {}'s bullets.  Reseting...".format(author.name))
        author.bullets_returned_so_far.clear()
        

    author.bullets_returned_so_far.append(bullet_num)

    logging.info("bullet number{} has been shown.".format(bullet_num))
    bullets = get_bullets(author)
    bullet = bullets[int(bullet_num)]

    if RATING_MODE_TOGGLE:
        print(bullet[0])
        # set the bullet rating in the 2D array - to returned value from rate_me()
        bullets[bullet_num][1] = rate_me(bullet, bullet_num)
        #  are we not going to need to pass author also?
        print("You rated: \n" + str(bullets[bullet_num][0]) + "\n" + str(bullets[bullet_num][1]))
    else:
        print(bullet[0])


def return_bullets_by_rating(bullets, rating):
    """
    Takes the authors bullets and rating integer
    the user requests.  Iterates through all bullets
    and returns only those equal to and above a
    certain rating.
    """
    #  Clean out Nones, make them equal to 0
    for i in range(len(bullets)):
        if bullets[i][1] == None:
            bullets[i][1] = 0
    try:
        rated_bullets = [bullet for bullet in bullets if int(bullet[1]) >= int(rating)]
        return rated_bullets
    except TypeError as e:
        logging.info("Type error when returning bullets by rating")


def sort_bullets():
    """
    Call this function once the user decides to turn on sort by
    rating mode.  Pass in the author to sort.

    Asks the user what author he wants to sort and by what rating he would like to sort.  Passes author and rating selection to return_bullets_by_rating.  Updates the author object with the sorted bullets.  author.sorted_bullets = return_bullets_by_rating(author, rating)
    """

    logging.info("Called sort_bullets")
    author_selection = input("Which author would you like to sort?")

    rating = input("Display bullets only rated WHAT and above.")
    print("sorting...{0}.  Removing bullets only rated {1} and below.".format(author_selection, rating))
    # now change return bullets by rating to only
    logging.info("User chose {0} author and to sort by rating {1}".format(author_selection.lower(), str(rating)))

    for author in all_authors:
        if author_selection.lower() == author.keybinding:
            #  Should this be return_bullets_by_rating?
            author.sorted_bullets = return_bullets_by_rating(author.all_bullets, rating)
            #  author.sorted_temp_bulles = return_bullets_by_rating(author.temp_bullets, rating)
            print("Sorted {}'s bullets.".format(author.name))
            logging.info("Returned sorted bullets for {}".format(author))
            logging.info("Sorted {0}'s {1} bullets.".format(author.name, len(author.sorted_bullets)))


def save_file():
    """
    Take the 2D list of bullets, and save it as a CSV file
    """
    # iterate through bullets save to SV

    bullets = []
    select_key = input("Select author to export")
    for author in all_authors:
        if select_key.lower() == author.keybinding:
            bullets.extend(author.all_bullets)
    csvFile = open('saved_bullets.csv', 'w')
    try:
        writer = csv.writer(csvFile, dialect='excel')
        writer.writerow(('Bullet', 'Rating'))
        for bullet in bullets:
            writer.writerow(bullet)

    finally:
        print("saving your file")
        csvFile.close()
    #  @TODO allow user to choose export filename


#  @TODO function to apply either sorted_bullets or all_bullets
#  to temp.  MAY JUST BE ABLE TO USE WITH REPLACEMENT ON #  RANDOM.CHOICE


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


if __name__ == "__main__":
    main()
