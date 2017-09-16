import random
import pandas as pd
from tkinter import *
from tkinter import filedialog
import os

### CONSTANTS #####
##                  .-'''-.                                         
##          .---.   '   _    \                      .---.            
##          |   | /   /` '.   \ /|                  |   |            
##  .--./)  |   |.   |     \  ' ||                  |   |            
## /.''\\   |   ||   '      |  '||                  |   |            
##| |  | |  |   |\    \     / / ||  __        __    |   |            
## \`-' /   |   | `.   ` ..' /  ||/'__ '.  .:--.'.  |   |       _    
## /("'`    |   |    '-...-'`   |:/`  '. '/ |   \ | |   |     .' |   
## \ '---.  |   |               ||     | |`" __ | | |   |    .   | / 
##  /'""'.\ |   |               ||\    / ' .'.''| | |   |  .'.'| |// 
## ||     ||'---'               |/\'..' / / /   | |_'---'.'.'.-'  /  
## \'. __//                     '  `'-'`  \ \._,\ '/     .'   \_.'   
##  `'---'                                 `--'  `"                  




##
##·▄▄▄▄• ▄▌ ▐ ▄  ▄▄· ▄▄▄▄▄▪         ▐ ▄ .▄▄ · 
##▐▄▄·█▪██▌•█▌▐█▐█ ▌▪•██  ██ ▪     •█▌▐█▐█ ▀. 
##██▪ █▌▐█▌▐█▐▐▌██ ▄▄ ▐█.▪▐█· ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄
##██▌.▐█▄█▌██▐█▌▐███▌ ▐█▌·▐█▌▐█▌.▐▌██▐█▌▐█▄▪▐█
##▀▀▀  ▀▀▀ ▀▀ █▪·▀▀▀  ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪ ▀▀▀▀ 
        
    
def load_bullets():
    '''
    This function reads the bullets from text files and adds them to a Pandas dataframe.
    
    '''
    os.chdir('E:\\Writing\\Copywork\\Bullet Swipe File\\')
    print("Changed the working directory:")
    print(os.getcwd()); 
    bly_bly = pd.read_fwf("E:\Writing\Copywork\Bullet Swipe File\bob_bly.txt")
    gary_b = pd.read_fwf("E:\Writing\Copywork\Bullet Swipe File\gary_bencievenga.txt")
    john_carlton = pd.read_fwf("E:\Writing\Copywork\Bullet Swipe File\john_carlton.txt")
    zergnet_bullets = pd.read_fwf("E:\Writing\Copywork\Bullet Swipe File\zergnet_bullets.txt")
    halbert_bullets = pd.read_fwf("E:\Writing\Copywork\Bullet Swipe File\halbert_bullets.txt")
    settle_bullets = pd.read_fwf("E:\Writing\Copywork\Bullet Swipe File\settle_bullets.txt")
  
    
        
          



def rando_bullet(keybinding):
    '''
    This function reads the user selection
    and prints the appropriate bullet
    '''

def read_input(userInput):
    '''
    we will do the keyboard reading in this section
    '''
    print("called read_input")
    if userInput.lower() == 'q':
        print("Quit")
        quit()
    elif userInput.lower() == 'h':
        print("Here are your possible commands:\n Quit: q, Open: o")
    elif userInput.lower() == 'o':
        print("Opening a file...")
        get_filename()
        
        

## _____ ______   ________  ___  ________      
##|\   _ \  _   \|\   __  \|\  \|\   ___  \    
##\ \  \\\__\ \  \ \  \|\  \ \  \ \  \\ \  \   
## \ \  \\|__| \  \ \   __  \ \  \ \  \\ \  \  
##  \ \  \    \ \  \ \  \ \  \ \  \ \  \\ \  \ 
##   \ \__\    \ \__\ \__\ \__\ \__\ \__\\ \__\
##    \|__|     \|__|\|__|\|__|\|__|\|__| \|__|
    
while True:
    '''
    This is the main loop of the program.
    '''
    load_bullets()
    userInput = input("Enter selection: ")
    read_input(userInput)
    
