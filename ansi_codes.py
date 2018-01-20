#https://mihaicorciu.ro
#adapted from
#http://ascii-table.com/ansi-escape-sequences.php
#http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

from __future__ import print_function
import sys, time

#start = chr(27) + chr(91)
#start = '\x1b\x5b'
#start = u'\u001b['
start = chr(27)+"["

#Cursor Position:
#Moves the cursor to the specified position (coordinates).
#If you do not specify a position, the cursor moves to the home position at the upper-left corner of the screen (line 0, column 0). This escape sequence works the same way as the following Cursor Position escape sequence. 
def XY(x,y):    return(start + "{:d};{:d}H".format(x,y))
#Cursor Up:
#Moves the cursor up by the specified number of lines without changing columns. If the cursor is already on the top line, ANSI.SYS ignores this sequence. 
def Up(n):      return(start + "{:d}A".format(n))
#Cursor Down:
#Moves the cursor down by the specified number of lines without changing columns. If the cursor is already on the bottom line, ANSI.SYS ignores this sequence.
def Down(n):    return(start + "{:d}B".format(n))
#Cursor Forward:
#Moves the cursor forward by the specified number of columns without changing lines. If the cursor is already in the rightmost column, ANSI.SYS ignores this sequence. 
def Right(n):   return(start + "{:d}C".format(n))
#Cursor Backward:
#Moves the cursor back by the specified number of columns without changing lines. If the cursor is already in the leftmost column, ANSI.SYS ignores this sequence.
def Left(n):    return(start + "{:d}D".format(n))
#Save Cursor Position:
#Saves the current cursor position. You can move the cursor to the saved cursor position by using the Restore Cursor Position sequence. 
Save		= start + "s"
#Restore Cursor Position:
#Returns the cursor to the position stored by the Save Cursor Position sequence. 
Restore		= start + "u"	 
#Erase Display:
#Clears the screen and moves the cursor to the home position (line 0, column 0).
EraseDisplay	= start + "2J"
#Erase Line:
#Clears all characters from the cursor position to the end of the line (including the character at the cursor position). 
EraseLine	= start + "K"
#Erase Line:
#Clears all characters from the cursor position to the end of the line (including the character at the cursor position). 

#Set Graphics Mode:
#Calls the graphics functions specified by the following values. These specified functions remain active until the next occurrence of this escape sequence. Graphics mode changes the colors and attributes of text (such as bold and underline) displayed on the screen.

#Text attributes
Reset		= start + "0m"
Bold		= start + "1m"
Underline	= start + "4m"
Blink		= start + "5m"
Reverse		= start + "7m"
Conceale	= start + "8m"

#8 Colors Foreground
black		= start + '30m'
red		= start + '31m'
green		= start + '32m'
yellow		= start + '33m'
blue		= start + '34m'
magenta		= start + '35m'
cyan		= start + '36m'
white		= start + '37m'

#8 Colors Background
bg_black        = start + '40m'
bg_red          = start + '41m'
bg_green        = start + '42m'
bg_yellow       = start + '43m'
bg_blue         = start + '44m'
bg_magenta      = start + '45m'
bg_cyan         = start + '46m'
bg_white        = start + '47m'

#Parameters 30 through 47 meet the ISO 6429 standard

#16 Colors Foregroud
Black    = start + '30;1m'
Red      = start + '31;1m'
Green    = start + '32;1m'
Yellow   = start + '33;1m'
Blue     = start + '34;1m'
Magenta  = start + '35;1m'
Cyan     = start + '36;1m'
White    = start + '37;1m'

#16 Corors Background
Bg_Black         = start + '40;1m'
Bg_Red           = start + '41;1m'
Bg_Green         = start + '42;1m'
Bg_Yellow        = start + '43;1m'
Bg_Blue          = start + '44;1m'
Bg_Magenta       = start + '45;1m'
Bg_Cyan          = start + '46;1m'
Bg_White         = start + '47;1m'

def color256(n): return (start + "38;5;{:d}m".format(n))
def bg256(n): return (start + "48;5;{:d}m".format(n))


if __name__ == "__main__":
    print(EraseDisplay,XY(0,0),Underline,"ANSI Escape sequences",sep='')
    print("")
    print(black, bg_white, "black", Reset, sep='')
    print(red, 		"red", sep='')
    print(green, 	"green", sep='')
    print(yellow, 	"yellow", sep='')
    print(blue, 	"blue", sep='')
    print(magenta, 	"magenta", sep='')
    print(cyan, 	"cyan", sep='')
    print(white, 	"white", sep='')
    print(Reset)
    time.sleep(1)
    print(bg_black, 	"bg_black", Reset, sep='')
    print(bg_red, 	"bg_red", sep='')
    print(bg_green, 	"bg_green", sep='')
    print(bg_yellow, 	"bg_yellow", sep='')
    print(bg_blue, 	"bg_blue", sep='')
    print(bg_magenta, 	"bg_magenta", sep='')
    print(bg_cyan, 	"bg_cyan", sep='')
    print(bg_white,Black,"bg_white", sep='')
    print(Reset)
    time.sleep(1)
    print(Black,     "Black", Reset, sep='')
    print(Red,       "Red", sep='')
    print(Green,     "Green", sep='')
    print(Yellow,    "Yellow", sep='')
    print(Blue,      "Blue", sep='')
    print(Magenta,   "Magenta", sep='')
    print(Cyan,      "Cyan", sep='')
    print(White,     "White", sep='')
    print(Reset)
    time.sleep(1)
    print(Bg_Black,     "Bg_Black", Reset, sep='')
    print(Bg_Red,       "Bg_Red", sep='')
    print(Bg_Green,     "Bg_Green", sep='')
    print(Bg_Yellow,    "Bg_Yellow", sep='')
    print(Bg_Blue,      "Bg_Blue", sep='')
    print(Bg_Magenta,   "Bg_Magenta", sep='')
    print(Bg_Cyan,      "Bg_Cyan", sep='')
    print(Bg_White,Black,"Bg_White", sep='')
    print(Reset)
    time.sleep(1)

    for id in range(256):
        print(color256(id) + " " + str(id).ljust(4), end = ' ')
    print(Reset)

    time.sleep(1)

    for id in range(256):
        print(bg256(id) + " " + str(id).ljust(4), end = ' ')
    print(Reset)


    print(Reset)
