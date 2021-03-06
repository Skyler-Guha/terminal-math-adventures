from os import system, name
import time
import sys

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux (here os.name is 'posix')
    else:
        _ = system('clear')

#enabling ASNI for windows if os is windows
def enable_win_asni():
    if name == 'nt':
        system("REG ADD HKCU\CONSOLE /f /v VirtualTerminalLevel /t REG_DWORD /d 1")
        clear()

def slow_print(text,speed):
    for i in text:
        if(i!= " " or i != ">"):
            time.sleep(speed)

        print (i,end = "")
        sys.stdout.flush() #this one's for colour

def fg (color):
	return "\33[38;5;" + str(color) + "m"

def bg (color):
	return "\33[48;5;" + str(color) + "m"

def fgbg(fg_color,bg_color):
	return "\33[38;5;" + str(fg_color) + "m" + "\33[48;5;" + str(bg_color) + "m"

NC= "\033[1;37;40m"

ES= chr(96)
#we add NC & ES to end of fg colored text to -
#prevent color bleading on windows 10 terminal-
#which is glitchy and buggy. Try not to use fg color -
#at the bourders of that trerminal either.
#for more info visit: https://github.com/microsoft/terminal/issues/75 
