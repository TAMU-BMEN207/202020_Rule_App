# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 20:31:33 2021

@author: annice

Description: According to the Vision Council, 75% of adults use glasses 
or contact lenses. Staring at computer, smartphone and other digital screens 
is known to play an important factor in permanently damaging you eyes and 
increasing the need to use corrective glasses or contact lenses. It is 
suggested that after looking at digital screens for 20 minutes you take a 20 
second break to look 20 meters away. 
In the following program we make an application that warns you every 20 mins
to look 20 meters away for 20 secs. The application lets you know when 20 mins
or 20 secs has passed by showing a message using the messagebox module. 

Instruction: 
    I) First create the UI. Look at the file provided for the 
UI and head over to the UI section below and use tkinter to build a similar UI.
    II) write a function for starting the timer.
    III) write a function for counting down and a function to reset the timer

"""

# ---------------------------- Use the modules imported below to write your program ------------------------------- #

import math
import tkinter
from tkinter import messagebox

# ---------------------------- Use the constants below in your program ------------------------------- #
#The color scheme has been defined for you below. Feel free to play around 
#with it later. You can explore other color schemes on colorhunt.co

TEAL = "#79A3B1"
LIGHTTEAL = "#D0E8F2"
DARKTEAL = "#456268"
BEIGE = "#FCF8EC"
GREEN = "#7FC8A9"
FONT_NAME = "Atkinson"
WORK_MIN = 1
SHORT_BREAK_SEC = 20
# ---------------------------- Variables ------------------------------- #
reps=0
timer = None

# ---------------------------- write a function for resetting timer below ------------------------------- # 
def reset_timer():
    '''
    Returns nothing. Changes the text shown on the top to "Timer" and sets the 
    timer equal to 00:00.
    
    '''
    return 0
    
# ---------------------------- write a function to start the timer below------------------------------- # 
def start_btn_clicked():
    '''
    Returns nothing. Changes the text shown on the top to either "Work" or 
    "Break! Look Away" and calls the count_down function.
    
    '''
    return 0

# ---------------------------- write a function for counting down ------------------------------- # 
def count_down(count):
    '''
    Returns nothing. Changes the text showing the time remaining. 

    Parameters:
        count (int):The string which is to be reversed.

    '''
    return 0

# ---------------------------- UI ------------------------------- #
window = tkinter.Tk()

window.mainloop()

    