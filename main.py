#importing pkgs
import time
import os
import random

#from imports
from time import sleep

#colors - put all of them in cause i didnt know which ones i would use

Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"
cyan_back = "\033[0;46m"
purple_back = "\033[0;45m"
white_back = "\033[0;47m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
green_back = "\033[0;42m"
pink_back = "\033[0;41m"
grey_back = "\033[0;40m"
grey = '\033[38;4;236m'
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
invisible='\033[08m'
reverse='\033[07m'
reset='\033[0m'
grey = "\x1b[90m"

def clear():
  os.system('clear')

color_list=[red,green,yellow,magenta,cyan,bright_blue,bright_cyan,bright_green,bright_magenta,bright_red,bright_yellow]


clear()

for x in range(7):
	for i in range(9):
		f_color = random.choice(color_list)
		clear()
		for line in range(len(open("frames/frame" + str(i + 1) ).readlines())):
			print(f_color+open("frames/frame" + str(i + 1) ).readlines()[line],end="")
		time.sleep(0.1)
	time.sleep(0.5)
	clear()
