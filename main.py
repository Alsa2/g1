import curses
import curses.textpad
import time
from library import *

# Defining Variables
# Create menu list
menu = ['Transaction Managment', 'View Wallet Records', 'Data Managment', 'Setting', 'Exit']

def main(stdsrc):
    # Remove cursor
    curses.curs_set(0)

    # Set up colors
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.color_pair(1)
    stdsrc.attron(curses.color_pair(1))

    # Get the window size
    h, w = stdsrc.getmaxyx()
    
    # Entry message
    text = ("Welcome to your Crypto Wallet Records. Press q to quit and any other key to continue.")


    # Centering calculations
    stdsrc.addstr(h//2, w//2 - len(text)//2, text)
    
    #Changing color
    stdsrc.attron(curses.color_pair(2))
    #Add a box
    win = curses.newwin(h-2, w-2, 1, 1)
    stdsrc.box()


    # Refresh the screen
    win.box()
    stdsrc.refresh()

    # Wait for any key to be pressed
    k = stdsrc.getch()
    if k == ord('q'):
        print("Successfully exited")
        quit(10)
    
    # Remove the entry message
    stdsrc.clear()

    print("step 1 ok")

    # Ask for login information
    login(stdsrc)

    print("step 2 ok")

    print("step 1 ok")
    # Set up current row
    current_row_idx = 0
    # Print the main menu
    main_menu(stdsrc, current_row_idx)

    while 1:
        key = stdsrc.getch()
        stdsrc.clear()
        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdsrc.addstr(0, 0, "You pressed {}".format(menu[current_row_idx]))
            stdsrc.refresh()
            stdsrc.getch()
        main_menu(stdsrc, current_row_idx)
        
def login(stdsrc):
    stdsrc.clear()
    while True:
        # Setup a box
        h, w = stdsrc.getmaxyx()
        boxtextmessage = ("Please enter you login credentials")
        box1 = curses.newwin(10, len(boxtextmessage), h//2 - 5, w//2 - len(boxtextmessage)//2)
        box1.box()    
        box1.addstr(boxtextmessage)
        stdsrc.refresh()
        box1.refresh()
    
        #Getting Username
        username = str("")
        stdsrc.addstr(h//2 - 3, w//2 - len(boxtextmessage)//2+2, "Username: ")
        stdsrc.refresh()
        chInput= stdsrc.getch()
        while True:
            if chInput == 127:
                username = username[:-1]
                stdsrc.addstr(h//2 - 3, w//2 - len(boxtextmessage)//2+2, ("Username: " +username + "  "))
            elif chInput == curses.KEY_ENTER or chInput in [10, 13]:
                break
            else:
                strInput = chr(int(chInput))
                username = str(username) + str(strInput)
                curentusernameoutput = ("Username: " + username)
                stdsrc.addstr(h//2 - 3, w//2 - len(boxtextmessage)//2+2, curentusernameoutput)
            stdsrc.refresh()
            chInput= stdsrc.getch()
        
        #Getting Password
        password = str("")
        stdsrc.addstr(h//2 - 2, w//2 - len(boxtextmessage)//2+2, "Password: ")
        stdsrc.refresh()
        chInput= stdsrc.getch()
        while True:
            if chInput == 127:
                password = password[:-1]
                stdsrc.addstr(h//2 - 2, w//2 - len(boxtextmessage)//2+2, ("Password: " +len(password) * "*"+ "  "))
            elif chInput == curses.KEY_ENTER or chInput in [10, 13]:
                break
            else:
                strInput = chr(int(chInput))
                password = str(password) + str(strInput)
                curentpasswordoutput = ("Password: " + len(password) * "*")
                stdsrc.addstr(h//2 - 2, w//2 - len(boxtextmessage)//2+2, curentpasswordoutput)
            stdsrc.refresh()
            chInput= stdsrc.getch()
        stdsrc.clear()
        if simple_login(username, password):
            exit_condition = True
            result = """
  _|_|    _|    _|  _|_|_|_|_|  _|    _|    _|_|    _|_|_|    _|_|_|    _|_|_|  _|_|_|_|  _|_|_|          _|_|      _|_|_|    _|_|_|  _|_|_|_|    _|_|_|  
_|    _|  _|    _|      _|      _|    _|  _|    _|  _|    _|    _|    _|        _|        _|    _|      _|    _|  _|        _|        _|        _|        
_|_|_|_|  _|    _|      _|      _|_|_|_|  _|    _|  _|_|_|      _|      _|_|    _|_|_|    _|    _|      _|_|_|_|  _|        _|        _|_|_|      _|_|    
_|    _|  _|    _|      _|      _|    _|  _|    _|  _|    _|    _|          _|  _|        _|    _|      _|    _|  _|        _|        _|              _|  
_|    _|    _|_|        _|      _|    _|    _|_|    _|    _|  _|_|_|  _|_|_|    _|_|_|_|  _|_|_|        _|    _|    _|_|_|    _|_|_|  _|_|_|_|  _|_|_|"""
        else:
            time.sleep(1)
            exit_condition = False
            result = """  _|_|      _|_|_|    _|_|_|  _|_|_|_|    _|_|_|      _|_|_|    _|_|_|_|  _|      _|  _|_|_|  _|_|_|_|  _|_|_|    
_|    _|  _|        _|        _|        _|            _|    _|  _|        _|_|    _|    _|    _|        _|    _|  
_|_|_|_|  _|        _|        _|_|_|      _|_|        _|    _|  _|_|_|    _|  _|  _|    _|    _|_|_|    _|    _|  
_|    _|  _|        _|        _|              _|      _|    _|  _|        _|    _|_|    _|    _|        _|    _|  
_|    _|    _|_|_|    _|_|_|  _|_|_|_|  _|_|_|        _|_|_|    _|_|_|_|  _|      _|  _|_|_|  _|_|_|_|  _|_|_|"""
        #split the result into lines
        result = result.splitlines()
        #get the number of lines
        num_lines = len(result)
        #get the width of the widest line
        max_width = max([len(line) for line in result])
        #get the starting position of the box
        start_x = w//2 - max_width//2
        start_y = h//2 - num_lines//2
        #create the box
        box2 = curses.newwin(num_lines+2, max_width+2, start_y-1, start_x-1)
        box2.box()
        box2.attron(curses.color_pair(4))
        #print the result
        for i, line in enumerate(result):
            stdsrc.attron(curses.color_pair(2))
            box2.addstr(i+1, 1, line)
        box2.refresh()
        time.sleep(2)
        stdsrc.refresh()
        if exit_condition:
            break
        

        




def main_menu(stdsrc, selected_row_idx):

    # Set up screen size
    h, w = stdsrc.getmaxyx()

    # Setup status bar
    """
    cursor_x = max(0, cursor_x)
    cursor_x = min(w-1, cursor_x)
    cursor_y = max(0, cursor_y)
    cursor_y = min(h-1, cursor_y)
    statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
    """

    # Set up menu
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + menu.index(row)
        if idx == selected_row_idx:
            stdsrc.attron(curses.color_pair(3))
            stdsrc.addstr(y, x, row)
            stdsrc.attron(curses.color_pair(1))
        else:
            stdsrc.addstr(y, x, row)
    
    # Refresh the screen
    stdsrc.refresh()

def screen_exit(stdsrc):
    stdsrc.clear()
    exit()

curses.wrapper(main)

curses.initscr()

