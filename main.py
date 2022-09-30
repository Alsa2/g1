import curses
import curses.textpad
import time

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

curses.wrapper(main)

