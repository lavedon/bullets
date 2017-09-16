#Bullet rater
#Take a bunch of different bullets from text files
#Bind them to keys
#Then rate them -- Later add a way to add a multi-dimensional array to store
# - bullet's written about

import os
from tkinter import *
from tkinter import filedialog
import random
import csv
##
#### .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.
####| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
####| |    ______    | || |   _____      | || |     ____     | || |   ______     | || |      __      | || |   _____      | || |    _______   | |
####| |  .' ___  |   | || |  |_   _|     | || |   .'    `.   | || |  |_   _ \    | || |     /  \     | || |  |_   _|     | || |   /  ___  |  | |
####| | / .'   \_|   | || |    | |       | || |  /  .--.  \  | || |    | |_) |   | || |    / /\ \    | || |    | |       | || |  |  (__ \_|  | |
####| | | |    ____  | || |    | |   _   | || |  | |    | |  | || |    |  __'.   | || |   / ____ \   | || |    | |   _   | || |   '.___`-.   | |
####| | \ `.___]  _| | || |   _| |__/ |  | || |  \  `--'  /  | || |   _| |__) |  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  |`\____) |  | |
####| |  `._____.'   | || |  |________|  | || |   `.____.'   | || |  |_______/   | || ||____|  |____|| || |  |________|  | || |  |_______.'  | |
####| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
####| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
#### '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
##

#Use _ORIGINAL for the all, unrated

BOB_BLY_FILENAME = ""
BOB_BLY_BULLETS = []
BOB_BLY_SORTED_BULLETS = []
BOB_BLY_KEY = ""


GARY_B_FILENAME = ""
GARY_B_BULLETS = []
GARY_B_SORTED_BULLETS = []
GARY_B_KEY = ""

JOHN_CARLTON_FILENAME = ""
JOHN_CARTLON_BULLETS = []
JOHN_CARLTON_SORTED_BULLETS = []
JOHN_CARLTON_KEY = ""

ZERGNET_FILENAME = ""
ZERGNET_BULLETS = []
ZERGNET_SORTED_BULLETS = []
ZERGNET_KEY = ""

HALBERT_FILENAME = ""
HALBERT_BULLETS = []
HALBERT_SORTED_BULLETS = []
HALBERT_KEY = ""

SETTLE_FILENAME = ""
SETTLE_BULLETS = []
SETTLE_SORTED_BULLETS = []
SETTLE_KEY = ""

#Knowledge Bombs importer that you write ideas from
CURRENT_CAMPAIGN_FILENAME = ""
CURRENT_CAMPAIGN_BOMBS = []
CURRENT_CAMPAIGN_BOMBS_SORTED = []
#This dictionary contains the bullets you write.
#The key is the original knowledge bomb.
#The value is a list, containing strings.  Each value in the list is a bullet / bullet idea.
CURRENT_CAMPAIGN_BULLETS = {}

RATING_KEY = ""
RATING_MODE_TOGGLE = False
SORT_KEY = ""
SORT_BY_RATING = False

##
##·▄▄▄▄• ▄▌ ▐ ▄  ▄▄· ▄▄▄▄▄▪         ▐ ▄ .▄▄ ·
##▐▄▄·█▪██▌•█▌▐█▐█ ▌▪•██  ██ ▪     •█▌▐█▐█ ▀.
##██▪ █▌▐█▌▐█▐▐▌██ ▄▄ ▐█.▪▐█· ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄
##██▌.▐█▄█▌██▐█▌▐███▌ ▐█▌·▐█▌▐█▌.▐▌██▐█▌▐█▄▪▐█
##▀▀▀  ▀▀▀ ▀▀ █▪·▀▀▀  ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪ ▀▀▀▀

def load_filenames():
    '''
    This function reads each line of the main 5 text files and returns lists
    '''
    #get the filenames
    #os.chdir('E:\\Writing\\Copywork\\Bullet Swipe File\\')
    #print("Changed the working directory to:")
    #print(os.getcwd());
    return ("E:\Writing\Copywork\Bullet Swipe File\\bob_bly.txt",
            "E:\Writing\Copywork\Bullet Swipe File\gary_bencievenga.txt",
            "E:\Writing\Copywork\Bullet Swipe File\john_carlton.txt",
            "E:\Writing\Copywork\Bullet Swipe File\zergnet_bullets.txt",
            "E:\Writing\Copywork\Bullet Swipe File\halbert_bullets.txt",
            "E:\Writing\Copywork\Bullet Swipe File\settle_bullets.txt",
            "E:\Writing\Agency\Dan Ray\\final_rated_bombs.csv")
    print("Bly is " + BOB_BLY)

def csv_to_lists(filename):
    '''
    Takes the filename as string. Processes the two column CSV file.
    returns a list.  list[0] = bullets list[1] = rating.
    '''
    bulletList = []
    #Open the CSV file.
    with open(filename, newline='') as csvfile:
        bullet_reader = csv.reader(csvfile, delimiter=',')
        next(csvfile, None)
        for row in bullet_reader:
            bulletList.append(row)
    return bulletList

def file_to_lists(filename):
    '''
    Takes the filename as string. Then returns a list
    '''
    bulletList = []
    #Open the file. Strip the new line character
    with open(filename) as f:
        bullets = f.readlines()
        bullets = [x.strip() for x in bullets]

    for i in bullets:
        new_bullets = []
        new_bullets.append(i)
        new_bullets.append(0)
        bulletList.append(new_bullets)

    return bulletList


##
##                                                                ___                ___
##                                                              ,' | `.            ,' | `.
##                                                             | --+-- |__,-""-.__| --+-- |
##                                                     _________\_.----'----------`----._/_________
##                                                     \==========================================/
##                                                      `----------------------------------------'
##                                                                    \\ `-.__.-' //
##                                                                     \\ _/--\_ //
##                                                                      \/ ,--. \/
##                                                                      | |    | |
##                                                                       \ `--' /
##                                                                        `----'
def read_input(user_input):
    '''
    This function takes the user input and calls the appropriate function
    '''
    #Display help menu
    if user_input.lower() == '?':
        print('Possible selections:')
        print('Bob Bly Bullets: ' + BOB_BLY_KEY)
        print('Gary Bencievenga: ' + GARY_B_KEY)
        print('John Carlton Bullets: ' + JOHN_CARLTON_KEY)
        print('Gary Halbert Bullets: ' + HALBERT_KEY)
        print('Ben Settle Bullets: ' + SETTLE_KEY)
        print('ZergNet Headlines: ' + ZERGNET_KEY)
        print("Turn 'rating mode' on or off" + RATING_KEY)
        print("\nType 'q' to quit")
        print("Type '?' for help")

    #Toggle rating mode
    elif user_input.lower() == RATING_KEY:
        global RATING_MODE_TOGGLE
        if RATING_MODE_TOGGLE == False:
            RATING_MODE_TOGGLE = True
            print("Rating mode on")
        elif RATING_MODE_TOGGLE == True:
            RATING_MODE_TOGGLE = False
            print("Rating mode off")
    #Quit Python
    elif user_input.lower() == 'q':
        print("Goodbye")
        quit()

    #Toggle sort by rating mode
    elif user_input.lower() == SORT_KEY:
        global SORT_BY_RATING
        if SORT_BY_RATING == False:
            SORT_BY_RATING = True
            rating = input("What rating would you like to sort by? ")
            which_author = input("Choose an author (by key) ")
            if which_author.lower() == BOB_BLY_KEY:
                global BOB_BLY_SORTED_BULLETS
                BOB_BLY_SORTED_BULLETS = return_bullets_by_rating(BOB_BLY_BULLETS, rating)
            elif which_author.lower() == GARY_B_KEY:
                global GARY_B_SORTED_BULLETS
                GARY_B_SORTED_BULLETS = return_bullets_by_rating(GARY_B_BULLETS, rating)
            elif which_author.lower() == JOHN_CARLTON_KEY:
                global JOHN_CARLTON_SORTED_BULLETS
                JOHN_CARLTON_SORTED_BULLETS = return_bullets_by_rating(JOHN_CARLTON_BULLETS, rating)
            elif which_author.lower() == HALBERT_KEY:
                global HALBERT_SORTED_BULLETS
                HALBERT_SORTED_BULLETS = return_bullets_by_rating(HALBERT_BULLETS, rating)
            elif which_author.lower() == SETTLE_KEY:
                global SETTLE_SORTED_BULLETS
                SETTLE_SORTED_BULLETS = return_bullets_by_rating(SETTLE_BULLETS, rating)
            elif which_author.lower() == ZERGNET_KEY:
                global ZERGNET_SORTED_BULLETS
                ZERGNET_SORTED_BULLETS = return_bullets_by_rating(ZERGNET_BULLETS, rating)
            elif which_author.lower() == CURRENT_CAMPAIGN_KEY:
                global CURRENT_CAMPAIGN_BOMBS_SORTED
                CURRENT_CAMPAIGN_BOMBS_SORTED = return_bullets_by_rating(CURRENT_CAMPAIGN_BOMBS, rating)
        elif SORT_BY_RATING == True:
            SORT_BY_RATING = False
            print("Sort by rating OFF")
    #Toggle author selection
    elif user_input.lower() == BOB_BLY_KEY:
        if SORT_BY_RATING == False:
            process_bullet(BOB_BLY_BULLETS)
        elif SORT_BY_RATING == True:
            process_bullet(BOB_BLY_SORTED_BULLETS)
    elif user_input.lower() == GARY_B_KEY:
        if SORT_BY_RATING == False:
            process_bullet(GARY_B_BULLETS)
        elif SORT_BY_RATING == True:
            process_bullet(GARY_B_SORTED_BULLETS)
    elif user_input.lower() == JOHN_CARLTON_KEY:
        if SORT_BY_RATING == False:
            process_bullet(JOHN_CARLTON_BULLETS)
        elif SORT_BY_RATING == True:
            process_bullet(JOHN_CARLTON_SORTED_BULLETS)
    elif user_input.lower() == HALBERT_KEY:
        if SORT_BY_RATING == False:
            process_bullet(HALBERT_BULLETS)
        elif SORT_BY_RATING == True:
            process_bullet(HALBERT_SORTED_BULLETS)
    elif user_input.lower() == SETTLE_KEY:
        if SORT_BY_RATING == False:
            process_bullet(SETTLE_BULLETS)
        elif SORT_BY_RATING == True:
            process_bullet(SETTLE_SORTED_BULLETS)
    elif user_input.lower() == ZERGNET_KEY:
        if SORT_BY_RATING == False:
            process_bullet(ZERGNET_BULLETS)
        elif SORT_BY_RATING == True:
            process_bullet(ZERGNET_SORTED_BULLETS)
    elif user_input.lower() == CURRENT_CAMPAIGN_KEY:
        if SORT_BY_RATING == False:
            process_bullet(CURRENT_CAMPAIGN_BOMBS)
        elif SORT_BY_RATING == True:
            process_bullet(CURRENT_CAMPAIGN_BOMBS_SORTED)
    #Save file
    elif user_input.lower() == 'save':
        save_file()

def rate_me(bullet, bullet_num):
    '''
    Takes a bullet which was previously selected by random choice selects a bullet
    We then append a new rating to that bullet.
    The rating is stored in the 2d array bullets[1] = the rating
    An example of how ratings are stored in the 2d array is:
    SETTLE_BULLETS[34][1] = the rating
    #random bullet bullet[1] = the rating
    '''

    print("Current rating is: " + str(bullet[1]))
    user_input = input("enter your rating: ")
    user_input.lower()
    str(user_input)
    if '1' or '2' or '3' or '4' or '5' in user_input:
        print("User input is an integer")
        print("user_input is: " + str(user_input))
        rating = int(user_input)
    else:
        print("Not a valid rating (Not a integer)")
    return rating

def process_bullet(which_bullets):
	''' pass in whichever list of bullets (as a 2d Python list)
		The user chose.
		This function evaluates whether or not
		rating mode is turned on.
		if rating mode is activated: it calls the rate_me function with the correct
		bullet list.

		'''

	# the two local variables which store 1.) The random index 2.) the actual list of the bullet (which has two values a.) the actual bullet b.) the rating
	bullet_num = int(random.randrange(len(which_bullets)))
	bullet = which_bullets[int(bullet_num)]

	#Check if rating mode is activated if so pass the bullet along to rate_me()
	if RATING_MODE_TOGGLE == True:
		print(bullet[0])
		# set the original bullet rating in the 2d array - to the returned rating from rate_me()
		which_bullets[bullet_num][1] = rate_me(bullet, bullet_num)
		print("You rated: \n" + str(which_bullets[bullet_num][0]) + "\n" + str(which_bullets[bullet_num][1]))
	else:
		print(bullet[0])

def save_file():
    '''
    Take the 2D list of bullets, and save it as a CSV file
    '''
    # iterate through bullets save to SV
    print("saving your file")
    csvFile = open('saved_bullets.csv', 'w')

    bullets = []
    bullets.extend(BOB_BLY_SORTED_BULLETS)
    bullets.extend(GARY_B_SORTED_BULLETS)
    bullets.extend(JOHN_CARLTON_SORTED_BULLETS)
    bullets.extend(HALBERT_SORTED_BULLETS)
    bullets.extend(SETTLE_SORTED_BULLETS)
    bullets.extend(ZERGNET_SORTED_BULLETS)

    try:
        writer = csv.writer(csvFile, dialect='excel')
        writer.writerow(('Bullet', 'Rating'))
        for bullet in bullets:
            writer.writerow(bullet)

    finally:
        csvFile.close()

def return_bullets_by_rating(bullets, rating):
    '''
    bullets = 2D list, rating = integer
    Iterates through all the bullets and returns only those equal to and above a certain rating
    '''
    rated_bullets = [bullet for bullet in bullets if int(bullet[1]) >= int(rating)]
    return rated_bullets



##
##          ____                                 ,--.
##        ,'  , `.   ,---,         ,---,       ,--.'|
##     ,-+-,.' _ |  '  .' \     ,`--.' |   ,--,:  : |
##  ,-+-. ;   , || /  ;    '.   |   :  :,`--.'`|  ' :
## ,--.'|'   |  ;|:  :       \  :   |  '|   :  :  | |
##|   |  ,', |  '::  |   /\   \ |   :  |:   |   \ | :
##|   | /  | |  |||  :  ' ;.   :'   '  ;|   : '  '; |
##'   | :  | :  |,|  |  ;/  \   \   |  |'   ' ;.    ;
##;   . |  ; |--' '  :  | \  \ ,'   :  ;|   | | \   |
##|   : |  | ,    |  |  '  '--' |   |  ''   : |  ; .'
##|   : '  |/     |  :  :       '   :  ||   | '`--'
##;   | |`-'      |  | ,'       ;   |.' '   : |
##|   ;/          `--''         '---'   ;   |.'
##'---'                                 '---'
##

print("Calling load_filenames()")
BOB_BLY_FILENAME, GARY_B_FILENAME, JOHN_CARLTON_FILENAME, ZERGNET_FILENAME, HALBERT_FILENAME, SETTLE_FILENAME, CURRENT_CAMPAIGN_FILENAME = load_filenames()
print("Fetching Bly bullets")
BOB_BLY_BULLETS = file_to_lists(BOB_BLY_FILENAME)
print("Fetching Gary B bullets")
GARY_B_BULLETS = file_to_lists(GARY_B_FILENAME)
print("Fetching John Carlton bullets")
JOHN_CARLTON_BULLETS = file_to_lists(JOHN_CARLTON_FILENAME)
print("Fetching Zergnet bullets")
ZERGNET_BULLETS = file_to_lists(ZERGNET_FILENAME)
print("Fetching Halbert bullets")
HALBERT_BULLETS = file_to_lists(HALBERT_FILENAME)
print("Fetching Settle bullets")
SETTLE_BULLETS = file_to_lists(SETTLE_FILENAME)
print("Fetching Current Campain Knowledge Bombs...")
CURRENT_CAMPAIGN_BOMBS = csv_to_lists(CURRENT_CAMPAIGN_FILENAME)

#Bind Keys
BOB_BLY_KEY = 'b'
GARY_B_KEY = 'g'
JOHN_CARLTON_KEY = 'j'
ZERGNET_KEY = 'z'
HALBERT_KEY = 'h'
SETTLE_KEY = 's'
RATING_KEY = 'r'
SORT_KEY = 'x'
CURRENT_CAMPAIGN_KEY = 'c'

#Main loop
while True:
    #Ask for input
    try:
        read_input(input("Enter Selection: "))
    except ValueError as e:
        print(e)
        read_input(input("Enter Selection: "))
