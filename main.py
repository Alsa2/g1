import curses
import curses.textpad
from email.message import Message
import time
from xml.dom.expatbuilder import parseString
from library import *
from cryptography.fernet import Fernet


# Defining Variables
# Create menu list
menu = ['Transaction Managment', 'View Wallet Records', 'Data Managment', 'Setting', 'Exit']
fernet_password = "2wFYfwlLpg4iy_k-wkGxNUH3pGLYdzjFbEyf4jQJfiY="

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
    if k == ord('d'):

        # add a status bar at the bottom with a text zone for moving across functions
        stdsrc.attron(curses.color_pair(1))
        stdsrc.addstr(h-1, 0, "Debug menu <")
        stdsrc.refresh()
        stdsrc.getch()
        debug = ""
        chInput= stdsrc.getch()
        while True:
            if chInput == 127:
                debug = debug[:-1]
                stdsrc.addstr(h-1, 0, ("Debug menu <" +debug + "  "))
            elif chInput == curses.KEY_ENTER or chInput in [10, 13]:
                break
            else:
                strInput = chr(int(chInput))
                debug = str(debug) + str(strInput)
                curentdebugoutput = ("Debug menu <" + debug)
                stdsrc.addstr(h-1, 0, curentdebugoutput)
            stdsrc.refresh()
            chInput= stdsrc.getch()
        stdsrc.attron(curses.color_pair(2))
        if debug == "decrypt":
            decrypt_file(stdsrc)
        elif debug == "encrypt":
            encrypt_file(stdsrc)
        elif debug == "exit":
            screen_exit(stdsrc)
        elif debug == "login":
            login(stdsrc)
        elif debug == "menu":
            main_menu(stdsrc, 0)
        exit()
        


    
    # Remove the entry message
    stdsrc.clear()

    print("step 1 ok")

    # Ask for login information
    login(stdsrc)

    # Decryption of transaction records

    decrypt_file(stdsrc)

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
            if current_row_idx == 4:
                screen_exit(stdsrc)
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
            result = """  _|_|    _|    _|  _|_|_|_|_|  _|    _|    _|_|    _|_|_|    _|_|_|    _|_|_|  _|_|_|_|  _|_|_|          _|_|      _|_|_|    _|_|_|  _|_|_|_|    _|_|_|  
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
        


def decrypt_file(stdsrc):
    """
    Decrypts a file using the key
    """
    h, w = stdsrc.getmaxyx()
    stdsrc.clear()
    textmessage = ("Enter Decryption Key: ")

    # ask for decryption key
    win = curses.newwin(1, 40, h//2, w//2 - 20)
    box = curses.textpad.Textbox(win)
    curses.textpad.rectangle(stdsrc, h//2-2, w//2-(len(textmessage)//2+10), h//2+2, w//2+len(textmessage)//2+10)
    stdsrc.addstr(h//2 - 1, w//2-len(textmessage)//2, textmessage)
    stdsrc.refresh()
    box.edit()
    key = box.gather().replace("/n", "")
    key = key.replace(" ", "")
    # remove the window
    win.clear()
    stdsrc.clear()
    time.sleep(1)

    defaultkey = False
    if str(key) == "default":
        with open('filekey.key', 'r') as filekey:
            key = filekey.read()
        defaultkey = True
        try:
            fernet = Fernet(key)
        except:
            stdsrc.clear()
            stdsrc.addstr(h//2, w//2, "Invalid Defaut Key")
            stdsrc.addstr(h//2+2, w//2, key)
            stdsrc.refresh()
            time.sleep(2)
            exit()
    else:
        try:
            fernet = Fernet(key)
        except:
            stdsrc.clear()
            stdsrc.addstr(h//2, w//2, "Invalid Key")
            stdsrc.refresh()
            time.sleep(2)
            exit()

        defaultkey = False
    if str(key) == "default":
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        defaultkey = True
        try:
            fernet = Fernet(key)
        except:
            stdsrc.clear()
            stdsrc.addstr(h//2, w//2, "Invalid Defaut Key")
            stdsrc.addstr(h//2+2, w//2, key)
            stdsrc.refresh()
            time.sleep(2)
            exit()
    else:
        try:
            fernet = Fernet(key)
        except:
            stdsrc.clear()
            stdsrc.addstr(h//2, w//2, "Invalid Key")
            stdsrc.refresh()
            time.sleep(2)
            exit()
        
    
    stdsrc.addstr(h//2+4, w//2 - 10, "Loading Key...")
    h, w = stdsrc.getmaxyx()
    win2 = curses.newwin(1, 80, h//2+3, w//2 - 35)
    for i in range(0, 30):
        time.sleep(0.01)
        win2.addstr(0, 0, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(i/2), i))
        win2.refresh()
    win2.clear()
    stdsrc.addstr(h//2+3, w//2 - 35, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(30/2), 30))
    if defaultkey:
        stdsrc.addstr(h//2+4, w//2 - 10, "Default Key Loaded  ")
    else:
        stdsrc.addstr(h//2+4, w//2-10, "Key loaded   ")
    stdsrc.refresh()

    # loading file
    stdsrc.addstr(h//2+5, w//2 - 10, "Loading File...")
    with open('transactions.csv', 'rb') as enc_file:
        encrypted = enc_file.read()
    """
    stdsrc.clear()
    stdsrc.addstr(h//2+4, w//2 - 35, encrypted)
    stdsrc.refresh()
    time.sleep(2)
    exit(encrypted)
    """
    h, w = stdsrc.getmaxyx()
    win2 = curses.newwin(1, 80, h//2+3, w//2 - 35)
    for i in range(30, 50):
        time.sleep(0.01)
        win2.addstr(0, 0, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(i/2), i))
        win2.refresh()
    win2.clear()
    stdsrc.addstr(h//2+3, w//2 - 35, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(50/2), 50))
    stdsrc.addstr(h//2+5, w//2-10, "Loaded Encrypted File   ")
    stdsrc.refresh()

    stdsrc.addstr(h//2+6, w//2 - 10, "Decrypting File...")
    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception as e:
        stdsrc.clear()
        stdsrc.addstr(h//2, w//2, "Invalid Key")
        stdsrc.refresh()
        stdsrc.addstr(h//2 + 2, w//2, (e))
        stdsrc.refresh()
        time.sleep(4)
        exit(e)
    
    
    
    win2 = curses.newwin(1, 80, h//2+3, w//2 - 35)
    for i in range(50, 75):
        time.sleep(0.01)
        win2.addstr(0, 0, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(i/2), i))
        win2.refresh()
    win2.clear()
    stdsrc.addstr(h//2+3, w//2 - 35, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(75/2), 75))
    stdsrc.addstr(h//2+6, w//2-10, "File Decrypted    ")
    stdsrc.refresh()

    stdsrc.addstr(h//2+7, w//2 - 10, "Remplacing File...")
    
    with open('transactions.csv', 'wb') as dec_file:
        dec_file.write(decrypted)
    
    win2 = curses.newwin(1, 80, h//2+3, w//2 - 35)
    for i in range(75, 101):
        time.sleep(0.01)
        win2.addstr(0, 0, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(i/2), i))
        win2.refresh()
    win2.clear()
    stdsrc.addstr(h//2+3, w//2 - 35, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(101/2), 100))
    stdsrc.addstr(h//2+7, w//2-10, "File Replaced     ")
    stdsrc.refresh()

    time.sleep(1)
    stdsrc.addstr(h//2+3, w//2 - 35, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(101/2), 100))
    stdsrc.addstr(h//2+8, w//2-10, "Decryption Succesfully Complete")
    stdsrc.refresh()
    time.sleep(2)
    stdsrc.clear()

    

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
    h, w = stdsrc.getmaxyx()
    stdsrc.clear()
    # add a litle cute rectangle
    boxtextmessage = ("Do you want to encrypt?")
    box1 = curses.newwin(5, len(boxtextmessage) + 6, h//2 - 1, w//2-3 - len(boxtextmessage)//2)
    box1.box()    
    stdsrc.refresh()
    box1.refresh()
    stdsrc.addstr(h//2, w//2 - len(boxtextmessage)//2, boxtextmessage)
    # ask if the user whats to encrypt
    idx = 0
    while True:
        if idx == 0:
            stdsrc.attron(curses.color_pair(1))
            stdsrc.addstr(h//2+2, w // 2 - 11, "Yes")
            stdsrc.attron(curses.color_pair(2))
            stdsrc.addstr(h//2+2, w // 2 + 10, "No")
        elif idx == 1:
            stdsrc.attron(curses.color_pair(2))
            stdsrc.addstr(h//2+2, w // 2 - 11, "Yes")
            stdsrc.attron(curses.color_pair(1))
            stdsrc.addstr(h//2+2, w // 2 + 10, "No")
        stdsrc.refresh()
        key = stdsrc.getkey()
        if key == "KEY_LEFT":
            idx = 0
        elif key == "KEY_RIGHT":
            idx = 1
        elif key == "KEY_ENTER" or key in ["\n", "\r"]:
            if idx == 0:
                encrypt_file(stdsrc)
                break
            elif idx == 1:
                break

    exit()

def encrypt_file(stdsrc):
    """
    Encrypts a file using the key
    """
    h, w = stdsrc.getmaxyx()
    stdsrc.clear()
    textmessage = ("Enter Encryption Key: ")

    # ask for encryption key
    win = curses.newwin(1, 40, h//2, w//2 - 20)
    box = curses.textpad.Textbox(win)
    curses.textpad.rectangle(stdsrc, h//2-2, w//2-(len(textmessage)//2+10), h//2+2, w//2+len(textmessage)//2+10)
    stdsrc.addstr(h//2 - 1, w//2-len(textmessage)//2, textmessage)
    stdsrc.refresh()
    box.edit()
    key = box.gather().replace("/n", "")
    key = key.replace(" ", "")
    # remove the window
    win.clear()
    stdsrc.clear()
    time.sleep(1)

    defaultkey = False
    if str(key) == "default":
        with open('filekey.key', 'r') as filekey:
            key = filekey.read()
        defaultkey = True
        stdsrc.refresh()
        try:
            fernet = Fernet(key)
        except:
            stdsrc.clear()
            stdsrc.addstr(h//2, w//2, "Invalid Defaut Key")
            stdsrc.addstr(h//2+2, w//2, key)
            stdsrc.refresh()
            time.sleep(2)
            exit()
    else:
        try:
            fernet = Fernet(key)
        except:
            stdsrc.clear()
            stdsrc.addstr(h//2, w//2, "Invalid Key")
            stdsrc.refresh()
            time.sleep(2)
            exit()

        defaultkey = False
    if str(key) == "default":
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        defaultkey = True
        try:
            fernet = Fernet(key)
        except:
            stdsrc.clear()
            stdsrc.addstr(h//2, w//2, "Invalid Defaut Key")
            stdsrc.addstr(h//2+2, w//2, key)
            stdsrc.refresh()
            time.sleep(2)
            exit()
    else:
        try:
            fernet = Fernet(key)
        except:
            stdsrc.clear()
            stdsrc.addstr(h//2, w//2, "Invalid Key")
            stdsrc.refresh()
            time.sleep(2)
            exit()
        
    
    stdsrc.addstr(h//2+4, w//2 - 10, "Loading Key...")
    h, w = stdsrc.getmaxyx()
    win2 = curses.newwin(1, 80, h//2+3, w//2 - 35)
    for i in range(0, 30):
        time.sleep(0.01)
        win2.addstr(0, 0, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(i/2), i))
        win2.refresh()
    win2.clear()
    stdsrc.addstr(h//2+3, w//2 - 35, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(30/2), 30))
    if defaultkey:
        stdsrc.addstr(h//2+4, w//2 - 10, "Default Key Loaded  ")
    else:
        stdsrc.addstr(h//2+4, w//2-10, "Key loaded   ")
    stdsrc.refresh()

    # loading file
    stdsrc.addstr(h//2+5, w//2 - 10, "Loading File...")
    with open('transactions.csv', 'rb') as enc_file:
        decrypted = enc_file.read()
    
    h, w = stdsrc.getmaxyx()
    win2 = curses.newwin(1, 80, h//2+3, w//2 - 35)
    for i in range(30, 50):
        time.sleep(0.01)
        win2.addstr(0, 0, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(i/2), i))
        win2.refresh()
    win2.clear()
    stdsrc.addstr(h//2+3, w//2 - 35, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(50/2), 50))
    stdsrc.addstr(h//2+5, w//2-10, "Loaded Decrypted File   ")
    stdsrc.refresh()

    stdsrc.addstr(h//2+6, w//2 - 10, "Encrypting File...")
    try:
        encrypted = fernet.encrypt(decrypted)
    except Exception as e:
        stdsrc.clear()
        stdsrc.addstr(h//2, w//2, "Invalid Key")
        stdsrc.refresh()
        stdsrc.addstr(h//2 + 2, w//2, (e))
        stdsrc.refresh()
        time.sleep(4)
        exit(e)
    
    
    
    win2 = curses.newwin(1, 80, h//2+3, w//2 - 35)
    for i in range(50, 75):
        time.sleep(0.01)
        win2.addstr(0, 0, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(i/2), i))
        win2.refresh()
    win2.clear()
    stdsrc.addstr(h//2+3, w//2 - 35, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(75/2), 75))
    stdsrc.addstr(h//2+6, w//2-10, "File Encrypted    ")
    stdsrc.refresh()

    stdsrc.addstr(h//2+7, w//2 - 10, "Remplacing File...")
    
    with open('transactions.csv', 'wb') as dec_file:
        dec_file.write(encrypted)
    
    win2 = curses.newwin(1, 80, h//2+3, w//2 - 35)
    for i in range(75, 101):
        time.sleep(0.01)
        win2.addstr(0, 0, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(i/2), i))
        win2.refresh()
    win2.clear()
    stdsrc.addstr(h//2+3, w//2 - 35, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(101/2), 100))
    stdsrc.addstr(h//2+7, w//2-10, "File Replaced     ")
    stdsrc.refresh()

    time.sleep(1)
    stdsrc.addstr(h//2+3, w//2 - 35, "Progress: [{0:50s}] {1:.1f}%".format('#' * int(101/2), 100))
    stdsrc.addstr(h//2+8, w//2-10, "Encryption Succesfully Complete")
    stdsrc.refresh()
    time.sleep(1)

def func1(stdsrc):
    pass
#curses.wrapper(decrypt_file)
curses.wrapper(main)

curses.initscr()

