import curses
print("imported curses")
import curses.textpad
print("imported curses.textpad")
import datetime
print("imported datetime")
import time
print("imported time")
from library import *
print("imported external libraries")
from cryptography.fernet import Fernet
print("imported cryptography.fernet")
import csv
print("imported csv")
import plotext as plt
print("imported plotext")
import yfinance as yf
print("imported yfinance")



# Defining Variables
# Create menu list
menu = ['Transaction Managment', 'Record Graph', 'Crypto Value', 'Setting', 'Exit']
tranmenu = ["Add Transaction", "View and edit Transactions", "Back"]
currencymenu = ["--USD--", "--EUR--", "--GBP--", "--JPY--", "--CNY--", "Return"]

def main(stdsrc):
    # Remove cursor
    curses.curs_set(0)

    # Set up colors
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_RED)    
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



    def graph(stdsrc):
        #inport the amount of transaction and they date for the graph
        # first value is the amount of the transaction and the second is the date
        with open("transactions.csv", "r") as f:
            reader = csv.reader(f)
            data = list(reader)
            # remove the third row
            data.pop(2)
            # take the amount in the first row
            amounts = [int(i[0]) for i in data]
            # take the date in the second row (format: dd/mm/yyyy)
            plt.date_form('Y/m/d')
            dates = [i[1] for i in data]
            # remove the hour fros dates
            dates = [i.split(" ")[0] for i in dates]
            # remplace the - by / for the graph
            dates = [i.replace("-", "/") for i in dates]
            prices = amounts
            # bgcolor = "black", fg = "white"
            plt.axes_color("black")
            plt.canvas_color("black")
            plt.ticks_color("green")

            plt.plot(dates, prices, color="green", label="Amount")

            plt.title("Wallet Records")
            plt.xlabel("Date")
            plt.ylabel("Amount of transaction (press any key to continue)")
            #stop curses screen
            stdsrc.clear()
            stdsrc.refresh()
            curses.endwin()
            plt.show()
            #wait for the user to press a key
            stdsrc.getch()
            #remove the graph
            plt.clear_figure()
            plt.clear_terminal()
            #restart curses screen
            curses.initscr()

    def currencyvalue(stdsrc):
        stdsrc.clear()
        current_row_idx = 0
        stdsrc.refresh()
        func2(stdsrc, current_row_idx)
        exitcondition = 0
        while exitcondition != 1:
            key = stdsrc.getch()
            if key == curses.KEY_UP and current_row_idx > 0:
                current_row_idx -= 1
            elif key == curses.KEY_DOWN and current_row_idx < len(currencymenu)-1:
                current_row_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row_idx == 0:
                    return "BTC-USD"
                elif current_row_idx == 1:
                    return "BTC-EUR"
                elif current_row_idx == 2:
                    return "BTC-GBP"
                elif current_row_idx == 3:
                    return "BTC-JPY"
                elif current_row_idx == 4:
                    return "BTC-CNY"
                elif current_row_idx == 5:
                    return "exit"

                stdsrc.refresh()

            stdsrc.clear()
            func2(stdsrc, current_row_idx)

    def func4(stdsrc, current_row_idx, menu, selectedbox):
        stdsrc.clear()
        stdsrc.refresh()
        selectedbox.refresh()
        selectedbox.attron(curses.color_pair(2))
        hbox, wbox = selectedbox.getmaxyx()
        for idx, row in enumerate(menu):
            x = wbox//2 - len(row)//2
            y = hbox//2 - len(menu)//2 + idx
            if idx == current_row_idx:
                selectedbox.attron(curses.color_pair(3))
                selectedbox.addstr(y, x, row)
                selectedbox.attroff(curses.color_pair(3))
            else:
                selectedbox.attron(curses.color_pair(2))
                selectedbox.addstr(y, x, row)
        selectedbox.refresh()
        

    def change_password(stdsrc):
        stdsrc.clear()
        stdsrc.refresh()
        # create a new box for the password
        h, w = stdsrc.getmaxyx()
        selectedbox = curses.newwin(3, 50, h//2-2, w//2-25)
        selectedbox.box()
        selectedbox.refresh()
        notes = str("")
        stdsrc.attron(curses.color_pair(2))
        stdsrc.addstr(h//2 -1 , w//2 - len(boxtextmessage)//2-12, "New Password: ")
        stdsrc.refresh()
        chInput= stdsrc.getch()
        while True:
            if chInput == 127:
                notes = notes[:-1]
                stdsrc.addstr(h//2 -1, w//2 - len(boxtextmessage)//2-12, ("New Password: " +notes + "  "))
            elif chInput == curses.KEY_ENTER or chInput in [10, 13]:
                break
            else:
                strInput = chr(int(chInput))
                notes = str(notes) + str(strInput)
                curentnotesoutput = ("New Password: " + notes)
                stdsrc.addstr(h//2 -1, w//2 - len(boxtextmessage)//2-12, curentnotesoutput)
            stdsrc.refresh()
            chInput= stdsrc.getch()
        stdsrc.clear()
        stdsrc.refresh()
        newpassword = notes
        localusername = username
        with open("user.csv", "r") as file:
            database = file.readlines()
        salty = "(╯°□°）╯︵ ┻━┻"
        to_hash = localusername + newpassword + salty
        hashed_password = hmac.new(''.encode(), to_hash.encode(),  'sha512').hexdigest()
        with open("user.csv", "w") as file:
            for line in database:
                if localusername in line:
                    file.write(localusername + "," + hashed_password + "\n")
                else:
                    file.write(line)
    
    def changetheme(stdsrc):
        stdsrc.clear()
        stdsrc.refresh()
        color = thememenu(stdsrc)
        if color == "RED":
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
            curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        if color == "GREEN":
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
            curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        if color == "YELLOW":
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
            curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        if color == "BLUE":
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
            curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        if color == "MAGENTA":
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
            curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        if color == "CYAN":
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
            curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
        if color == "WHITE":
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
            curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    def thememenu(stdsrc):
        availablecolors = ["RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE"]
        stdsrc.clear()
        h, w = stdsrc.getmaxyx()
        selectedbox = curses.newwin(h, 30, 0, w//2-15)
        selectedbox.box()
        selectedbox.refresh()
        stdsrc.refresh()
        current_row_idx = 0
        func4(stdsrc, current_row_idx, availablecolors, selectedbox)
        key = stdsrc.getch()
        while True:
            if key == curses.KEY_UP and current_row_idx > 0:
                current_row_idx -= 1
            elif key == curses.KEY_DOWN and current_row_idx < len(availablecolors)-1:
                current_row_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row_idx == 0:
                    return "RED"
                elif current_row_idx == 1:
                    return "GREEN"
                elif current_row_idx == 2:
                    return "YELLOW"
                elif current_row_idx == 3:
                    return "BLUE"
                elif current_row_idx == 4:
                    return "MAGENTA"
                elif current_row_idx == 5:
                    return "CYAN"
                elif current_row_idx == 6:
                    return "WHITE"
                stdsrc.refresh()

            stdsrc.clear()
            func4(stdsrc, current_row_idx, availablecolors, selectedbox)
            key = stdsrc.getch()



    def settings(stdsrc):
        settingsmenu = ["Change Password", "Change Color Theme", "AUTODESTRUCTION", "Back"]
        stdsrc.clear()
        stdsrc.refresh()
        #add a box with a menu for chosing the option
        # Setup a box
        h, w = stdsrc.getmaxyx()
        boxtextmessage = ("┌────────────Settings────────────┐")
        box6 = curses.newwin(10, len(boxtextmessage), h//2 - 5, w//2 - len(boxtextmessage)//2)
        box6.box()    
        box6.addstr(boxtextmessage)
        stdsrc.refresh()
        box6.refresh()
        #add a menu
        current_row_idx = 0
        func4(stdsrc, current_row_idx, settingsmenu, box6)
        key = stdsrc.getch()
        while True:
            if key == curses.KEY_UP and current_row_idx > 0:
                current_row_idx -= 1
            elif key == curses.KEY_DOWN and current_row_idx < len(settingsmenu)-1:
                current_row_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row_idx == 0:
                    change_password(stdsrc)
                elif current_row_idx == 1:
                    changetheme(stdsrc)
                elif current_row_idx == 2:
                    stdsrc.clear()
                    stdsrc.refresh()
                    #ask for confirmation
                    boxtextmessage = ("┌────────────Settings────────────┐")
                    box6 = curses.newwin(10, len(boxtextmessage), h//2 - 5, w//2 - len(boxtextmessage)//2)
                    box6.box()
                    box6.addstr(boxtextmessage)
                    stdsrc.refresh()
                    box6.refresh()
                    box6.addstr(2, 2, "Are you sure you want to delete all your data?")
                    box6.addstr(3, 2, "This action cannot be undone.")
                    box6.addstr(4, 2, "Press Y to confirm, N to cancel.")
                    box6.refresh()
                    key = stdsrc.getch()
                    while True:
                        if key == ord("y"):
                            #delete all data
                            #erase transactions.csv
                            with open("transactions.csv", "w") as file:
                                file.write("")
                            #erase user.csv
                            with open("user.csv", "w") as file:
                                file.write("")
                            #erase filekey.key
                            with open("filekey.key", "w") as file:
                                file.write("")
                            #erase library.py
                            with open("library.py", "w") as file:
                                file.write("")
                            #erase main.py
                            with open("main.py", "w") as file:
                                file.write("")
                            stdsrc.clear()
                            stdsrc.refresh()
                            boxtextmessage = ("┌────────────Settings────────────┐")
                            box6 = curses.newwin(10, len(boxtextmessage), h//2 - 5, w//2 - len(boxtextmessage)//2)
                            box6.box()
                            box6.addstr(boxtextmessage)
                            stdsrc.refresh()
                            box6.refresh()
                            box6.addstr(2, 2, "All data has been deleted.")
                            box6.addstr(3, 2, "Press any key to continue.")
                            box6.refresh()
                            stdsrc.getch()
                            break
                        elif key == ord("n"):
                            break
                    
                elif current_row_idx == 3:
                    stdsrc.clear()
                    break
            stdsrc.clear()
            func4(stdsrc, current_row_idx, settingsmenu, box6)
            box6.refresh()
            stdsrc.refresh()
            key = stdsrc.getch()
        





    def func2(stdsrc, current_row_idx):
        h, w = stdsrc.getmaxyx()
        # Set up menu
        for idx, row in enumerate(currencymenu):
            x = w//2 - len(row)//2
            y = h//2 - len(currencymenu)//2 + currencymenu.index(row)
            if idx == current_row_idx:
                stdsrc.attron(curses.color_pair(3))
                stdsrc.addstr(y, x, row)
                stdsrc.attron(curses.color_pair(1))
            else:
                stdsrc.addstr(y, x, row)
        # Refresh the screen
        stdsrc.refresh()

    def cryptovalue(stdsrc):
        h, w = stdsrc.getmaxyx()
        currency = currencyvalue(stdsrc)
        if currency == "exit":
            stdsrc.clear()
            return
        
        plt.date_form('d/m/Y')

        # ask the user to enter the start date
        editw = 7
        stdsrc.clear()
        stdsrc.refresh()
        notes = ""
        box5 = curses.newwin(h//5, w//2, h//5*2, w//4)
        box5.box()
        box5height, box5weight = box5.getmaxyx()
        box5height = box5height//2
        box5.addstr(box5height-1 , editw, "Enter the start date (format: yyyy-mm-dd): " + notes)
        box5.refresh()
        chInput= stdsrc.getch()
        while True:
            if chInput == 127:
                notes = notes[:-1]
                box5.addstr(box5height-1 , editw, ("Enter the start date (format: yyyy-mm-dd): " +notes + "  "))
            elif chInput == curses.KEY_ENTER or chInput in [10, 13]:
                if len(notes) == 10:
                    if notes[4] == "-" and notes[7] == "-":
                        startdate = notes
                        box5.addstr(box5height , editw, "                                                        ")
                        break
                    box5.attron(curses.color_pair(5))
                    box5.addstr(box5height , editw, "Check that the date is in the correct format (yyyy-mm-dd)")
                    box5.attroff(curses.color_pair(5))
                else:
                    box5.attron(curses.color_pair(5))
                    box5.addstr(box5height , editw, "Invalid date format, please try again")
                    box5.attroff(curses.color_pair(5))
            else:
                strInput = chr(int(chInput))
                notes = str(notes) + str(strInput)
                curentnotesoutput = ("Enter the start date (format: yyyy-mm-dd): " + notes)
                box5.addstr(box5height-1 , editw, curentnotesoutput)
            box5.refresh()
            chInput= stdsrc.getch()

        notes = ""
        # ask the user to enter the end date
        box5.addstr(box5height+1 , editw, "Enter the end date (format: yyyy-mm-dd, enter 'today' for today's date): " + notes)
        box5.refresh()
        chInput= stdsrc.getch()
        while True:
            if chInput == 127:
                notes = notes[:-1]
                box5.addstr(box5height+1 , editw, ("Enter the end date (format: yyyy-mm-dd, enter 'today' for today's date): " +notes + "  "))
            elif chInput == curses.KEY_ENTER or chInput in [10, 13]:
                #chech if if input valid date format
                if notes == "today":
                    enddate = datetime.datetime.today().strftime('%d/%m/%Y')
                    break
                elif len(notes) == 10:
                    if notes[4] == "-" and notes[7] == "-":
                        enddate = notes
                        break
                    box5.addstr(box5height , editw, "                                                        ")
                else:
                    box5.attron(curses.color_pair(5))
                    box5.addstr(box5height + 2, editw, "Invalid date format, please try again")
                    box5.attroff(curses.color_pair(5))
                
            else:
                strInput = chr(int(chInput))
                notes = str(notes) + str(strInput)
                curentnotesoutput = ("Enter the end date (format: yyyy-mm-dd, enter 'today' for today's date): " + notes)
                box5.addstr(box5height+1 , editw, curentnotesoutput)
            box5.refresh()
            chInput= stdsrc.getch()
        enddate = notes
        if enddate == "today":
            enddate = datetime.datetime.now().strftime("%Y-%m-%d")
        # get the data from the API
        del box5
        stdsrc.clear()
        stdsrc.refresh()
        stdsrc.addstr(h//2, w//2, "Downloading flochart data...")
        stdsrc.refresh()

        data = yf.download(currency, startdate, enddate)


        dates = plt.datetimes_to_string(data.index)

        plt.candlestick(dates, data)
        plt.axes_color("black")
        plt.canvas_color("black")
        plt.ticks_color("green")
        plt.title(f"{currency} Graph")
        plt.xlabel("Date")
        plt.ylabel("Stock Price (press any key to exit")
        stdsrc.clear()
        stdsrc.refresh()
        curses.endwin()
        plt.show()
        #wait for the user to press a key
        stdsrc.getch()
        #remove the graph
        plt.clear_figure()
        plt.clear_terminal()
        #restart curses screen
        curses.initscr()




    def addtransaction(stdsrc):
        # importing transaction csv file
        # the transaction file is separated into 3 columns
        # the first column is the updated balance
        # the second column is the date of the transaction in the utc time
        # the third column is notes about the transaction
        stdsrc.clear()
        while True:
            # Setup a box
            h, w = stdsrc.getmaxyx()
            boxtextmessage = ("Please Enter the Transaction Details")
            box1 = curses.newwin(10, len(boxtextmessage), h//2 - 5, w//2 - len(boxtextmessage)//2)
            box1.box()    
            box1.addstr(boxtextmessage)
            stdsrc.refresh()
            box1.refresh()

            # get if its a deposit or withdrawl
            idx = 0
            while True:
                if idx == 0:
                    box1.attron(curses.color_pair(1))
                    box1.addstr(2, 5, "Deposit")
                    box1.attron(curses.color_pair(2))
                    box1.addstr(2, 23, "Withdraw")
                elif idx == 1:
                    box1.attron(curses.color_pair(2))
                    box1.addstr(2, 5, "Deposit")
                    box1.attron(curses.color_pair(1))
                    box1.addstr(2, 23, "Withdraw")
                box1.refresh()
                key = stdsrc.getkey()
                if key == "KEY_LEFT":
                    idx = 0
                elif key == "KEY_RIGHT":
                    idx = 1
                elif key == "KEY_ENTER" or key in ["\n", "\r"]:
                    if idx == 0:
                        deposit = True
                        break
                    elif idx == 1:
                        deposit = False
                        break
            stdsrc.attron(curses.color_pair(2))
            #Getting the amount
            amount = str("")
            stdsrc.addstr(h//2 - 1, w//2 - len(boxtextmessage)//2+5, "Amount: ")
            stdsrc.refresh()
            chInput= stdsrc.getch()
            while True:
                stdsrc.attron(curses.color_pair(2))
                if chInput == 127:
                    amount = amount[:-1]
                    stdsrc.addstr(h//2 - 1, w//2 - len(boxtextmessage)//2+5, ("Amount: " +amount + "  "))
                elif chInput == curses.KEY_ENTER or chInput in [10, 13]:
                    if amount == "":
                        amount = "0"
                        break
                    if not amount.isdigit():
                        stdsrc.attron(curses.color_pair(4))
                        stdsrc.addstr(h//2, w//2 - len(boxtextmessage)//2+5, ("Only digits allowed"))
                        stdsrc.attroff(curses.color_pair(4))
                    elif amount[0] == "-":
                        stdsrc.attron(curses.color_pair(4))
                        stdsrc.addstr(h//2, w//2 - len(boxtextmessage)//2+5, ("Only positive numbers allowed"))
                        stdsrc.attroff(curses.color_pair(4))
                    elif int(amount) > 2147483647:
                        stdsrc.attron(curses.color_pair(4))
                        stdsrc.addstr(h//2, w//2 - len(boxtextmessage)//2+5, ("How is it even possible ???)"))
                        stdsrc.attroff(curses.color_pair(4))
                    else:
                        amount = int(amount)
                        break
                else:
                    stdsrc.attron(curses.color_pair(2))
                    strInput = chr(int(chInput))
                    amount = str(amount) + str(strInput)
                    curentamountoutput = ("Amount: " + amount)
                    stdsrc.addstr(h//2 - 1, w//2 - len(boxtextmessage)//2+5, curentamountoutput)
                stdsrc.refresh()
                chInput= stdsrc.getch()
            
            #Getting notes
            notes = str("")
            stdsrc.addstr(h//2 +1 , w//2 - len(boxtextmessage)//2+5, "Notes: ")
            stdsrc.refresh()
            chInput= stdsrc.getch()
            while True:
                if chInput == 127:
                    notes = notes[:-1]
                    stdsrc.addstr(h//2 + 1, w//2 - len(boxtextmessage)//2+5, ("Notes: " +notes + "  "))
                elif chInput == curses.KEY_ENTER or chInput in [10, 13]:
                    break
                else:
                    strInput = chr(int(chInput))
                    notes = str(notes) + str(strInput)
                    curentnotesoutput = ("Notes: " + notes)
                    stdsrc.addstr(h//2 + 1, w//2 - len(boxtextmessage)//2+5, curentnotesoutput)
                stdsrc.refresh()
                chInput= stdsrc.getch()
            stdsrc.clear()
    
            # Putting the transaction into the csv file
            # the transaction file is separated into 3 columns
            # the first column is the updated balance
            # the second column is the date of the transaction in the utc time
            # the third column is notes about the transaction

            # Calculating the new balance
            if deposit:
                amount = int(amount)
            else:
                amount = -int(amount)
            # Adding the transaction to the csv file
            with open('transactions.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([amount, datetime.datetime.now(), notes])
            stdsrc.clear()
            stdsrc.addstr(h//2, w//2, "Transaction Added")
            stdsrc.refresh()
            time.sleep(1)
            stdsrc.clear()
            stdsrc.refresh()
            break



            # Get the window size
            h, w = stdsrc.getmaxyx()
    def transedit(stdsrc, numberofrow):
        h, w = stdsrc.getmaxyx()
        box2 = curses.newwin(h, w//4, 0, w//4*3)
        box2.box()
        # add in the midle of the box
        boxtextmessage = "Editing Transaction Record"
        box2.addstr(0, w//8 - len(boxtextmessage)//2, boxtextmessage)
        box2.refresh()
        stdsrc.refresh()
        idx = 0
        boxh, boxw = box2.getmaxyx()
        editw = 7
        editd = boxw - len("Delete") - 7
        while True:
            if idx == 0:
                box2.attron(curses.color_pair(1))
                box2.addstr(2, editw, "Edit")
                box2.attron(curses.color_pair(2))
                box2.addstr(2, editd, "Delete")
            elif idx == 1:
                box2.attron(curses.color_pair(2))
                box2.addstr(2, editw, "Edit")
                box2.attron(curses.color_pair(1))
                box2.addstr(2, editd, "Delete")
            box2.refresh()
            key = stdsrc.getkey()
            if key == "KEY_LEFT":
                idx = 0
            elif key == "KEY_RIGHT":
                idx = 1
            elif key == "KEY_ENTER" or key in ["\n", "\r"]:
                if idx == 0:
                    delete = False
                    break
                elif idx == 1:
                    delete = True
                    break
        if delete:
            with open('transactions.csv', 'r') as f:
                reader = csv.reader(f)
                data = list(reader)
            with open('transactions.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                for row in data:
                    if row != data[numberofrow]:
                        writer.writerow(row)
            box2.attron(curses.color_pair(4))
            box2.addstr(boxh//2, boxw//2-len("Transaction Deleted") + 3, "Transaction Deleted")
            box2.attroff(curses.color_pair(4))
            stdsrc.refresh()
            box2.refresh()
            time.sleep(1)
            stdsrc.clear()
            stdsrc.refresh()
            box2.clear()
            del box2
        if not delete:

            # getting transaction data
            boxtextmessage = ("Please Enter the Transaction Details")
            boxh, boxw = box2.getmaxyx()
            editw = 7
            editd = boxw - len("Withdraw") - 7
            box2.addstr(6, w//8 - len(boxtextmessage)//2, boxtextmessage)
            box2.box()
            stdsrc.refresh()
            box2.refresh()
            #get the transaction data
            with open('transactions.csv', 'r') as f:
                reader = csv.reader(f)
                data = list(reader)
            transaction = data[numberofrow]
            date = transaction[1]
            amount = str(transaction[0])
            notes = transaction[2]
            if int(amount) > 0:
                idx = 0
            else:
                idx = 1
            # get if its a deposit or withdrawl
            while True:
                if idx == 0:
                    box2.attron(curses.color_pair(1))
                    box2.addstr(8, editw, "Deposit")
                    box2.attron(curses.color_pair(2))
                    box2.addstr(8, editd, "Withdraw")
                elif idx == 1:
                    box2.attron(curses.color_pair(2))
                    box2.addstr(8, editw, "Deposit")
                    box2.attron(curses.color_pair(1))
                    box2.addstr(8, editd, "Withdraw")
                box2.attron(curses.color_pair(2))
                box2.refresh()
                key = stdsrc.getkey()
                if key == "KEY_LEFT":
                    idx = 0
                elif key == "KEY_RIGHT":
                    idx = 1
                elif key == "KEY_ENTER" or key in ["\n", "\r"]:
                    if idx == 0:
                        deposit = True
                        break
                    elif idx == 1:
                        deposit = False
                        break
            stdsrc.attron(curses.color_pair(2))
            #Getting the amount
            #remove the minus for the manout
            if not deposit:
                amount = amount[1:]
            box2.addstr(10, editw, "Amount: " + amount)
            box2.refresh()
            chInput= stdsrc.getch()
            while True:
                stdsrc.attron(curses.color_pair(2))
                if chInput == 127:
                    amount = amount[:-1]
                    box2.addstr(10, editw, ("Amount: " +amount + "  "))
                elif chInput == curses.KEY_ENTER or chInput in [10, 13]:
                    if amount == "":
                        amount = "0"
                        break
                    if not amount.isdigit():
                        box2.attron(curses.color_pair(4))
                        box2.addstr(11, editw, ("Only digits allowed"))
                        box2.attroff(curses.color_pair(4))
                    elif amount[0] == "-":
                        box2.attron(curses.color_pair(4))
                        box2.addstr(11, editw, ("Only positive numbers allowed"))
                        box2.attroff(curses.color_pair(4))
                    elif int(amount) > 2147483647:
                        box2.attron(curses.color_pair(4))
                        box2.addstr(11, editw, ("How is it even possible ???)"))
                        box2.attroff(curses.color_pair(4))
                    else:
                        amount = int(amount)
                        break
                else:
                    box2.attron(curses.color_pair(2))
                    strInput = chr(int(chInput))
                    amount = str(amount) + str(strInput)
                    curentamountoutput = ("Amount: " + amount)
                    box2.addstr(10, editw, curentamountoutput)
                box2.refresh()
                chInput= stdsrc.getch()
            box2.addstr(11, 2, ((boxw-4)*" "))

            #Getting notes
            box2.addstr(12 , editw, "Notes: " + notes)
            box2.refresh()
            chInput= stdsrc.getch()
            while True:
                if chInput == 127:
                    notes = notes[:-1]
                    box2.addstr(12 , editw, ("Notes: " +notes + "  "))
                elif chInput == curses.KEY_ENTER or chInput in [10, 13]:
                    break
                else:
                    strInput = chr(int(chInput))
                    notes = str(notes) + str(strInput)
                    curentnotesoutput = ("Notes: " + notes)
                    box2.addstr(12 , editw, curentnotesoutput)
                box2.refresh()
                chInput= stdsrc.getch()

            if deposit:
                amount = int(amount)
            else:
                amount = -int(amount)

            # remplace the transaction with a new one
            with open('transactions.csv', 'r') as f:
                reader = csv.reader(f)
                data = list(reader)
            with open('transactions.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                for row in data:
                    if row != data[numberofrow]:
                        writer.writerow(row)
                    else:
                        writer.writerow([amount, date, notes])
            box2.attron(curses.color_pair(1))
            box2.addstr(boxh//2, boxw//2-len("Transaction Edited"), "Transaction Edited")
            box2.attroff(curses.color_pair(1))
            stdsrc.refresh()
            box2.refresh()
            time.sleep(1)
            stdsrc.clear()
            stdsrc.refresh()
            box2.clear()
            del box2
        
        

    def editviewtransactionrecord(stdsrc):
        h, w = stdsrc.getmaxyx()
        box3 = curses.newwin(h//3, w//4, h//3, 0)
        box3.box()
        box3.attron(curses.color_pair(2))
        # add in the midle of the box
        boxtextmessage = "Help"
        box3.addstr(0, (w//4)//2 - len(boxtextmessage)//2, boxtextmessage)
        box3.refresh()
        stdsrc.refresh()
        box3.addstr(2, 2, "Tips:")
        box3.refresh()
        time.sleep(0.3)
        box3.addstr(4, 2, "1. Use the arrows to navigate")
        box3.refresh()
        time.sleep(0.3)
        box3.addstr(6, 2, "2. Use enter to select")
        box3.refresh()
        time.sleep(0.3)
        box3.addstr(8, 2, "3. Use backspace to go back to the menu")
        box3.refresh()
        time.sleep(0.3)

        while True:
            h, w = stdsrc.getmaxyx()
            box1 = curses.newwin(h, w//2, 0, w//4)
            box1.box()
            # add in the midle of the box
            boxtextmessage = "Edit Transaction Record"
            box1.addstr(0, w//4 - len(boxtextmessage)//2, boxtextmessage)
            box1.refresh()
            stdsrc.refresh()
            # getting the amount of items in the transaction file
            with open('transactions.csv', 'r') as f:
                reader = csv.reader(f)
                data = list(reader)
                amountofitems = len(data)
            current_rox_idx = 0
            def printlist(current_rox_idx, amountofitems, notloaded):
                box1.box()
                box1.addstr(0, w//4 - len(boxtextmessage)//2, boxtextmessage)
                box1.refresh()
                # printing the list of transactions
                with open('transactions.csv', 'r') as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    amountofitems = len(data)
                    for i in range(0, amountofitems):
                        if i == current_rox_idx:
                            box1.attron(curses.color_pair(1))
                            box1.addstr(i+2, 2,(data[amountofitems-i-1][2]+ "  "))
                            box1.attroff(curses.color_pair(1))
                        else:
                            box1.addstr(i+2, 2, ("  "+data[amountofitems-i-1][2]))
                        if notloaded:
                            time.sleep(0.1)
                            box1.refresh()
                box1.refresh()
                
            current_row_idx = 0
            printlist(current_rox_idx, amountofitems, True)
            while True:
                box3.refresh()
                key = stdsrc.getch()
                if key == curses.KEY_UP and current_row_idx > 0:
                    current_row_idx -= 1
                elif key == curses.KEY_DOWN and current_row_idx < amountofitems-1:
                    current_row_idx += 1
                elif key == curses.KEY_ENTER or key in [10, 13]:
                    numberofrow = amountofitems - current_row_idx - 1
                    transedit(stdsrc, numberofrow)
                    box1.clear()
                elif key == 127:
                    box1.clear()
                    del box1
                    exit = True
                    break
                printlist(current_row_idx, amountofitems, False)
            if exit:
                break

                
            
            


        
    # Refresh the screen
    win.box()
    stdsrc.refresh()
    def firstoptionmenu(stdscr):
        stdsrc.clear()
        current_row_idx = 0
        stdsrc.refresh()
        func1(stdsrc, current_row_idx)
        exitcondition = 0
        while exitcondition != 1:
            key = stdsrc.getch()
            if key == curses.KEY_UP and current_row_idx > 0:
                current_row_idx -= 1
            elif key == curses.KEY_DOWN and current_row_idx < len(tranmenu)-1:
                current_row_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row_idx == 0:
                    addtransaction(stdsrc)
                elif current_row_idx == 1:
                    editviewtransactionrecord(stdsrc)
                if current_row_idx == 2:
                    stdscr.clear()
                    current_row_idx = 0
                    # Print the main menu
                    main_menu(stdsrc, current_row_idx)
                    break
                stdsrc.refresh()

            stdsrc.clear()
            func1(stdsrc, current_row_idx)

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


    # Ask for login information
    login(stdsrc)

    stdsrc.clear()
    # add a litle cute rectangle
    boxtextmessage = ("Do you want to decrypt?")
    box1 = curses.newwin(5, len(boxtextmessage) + 6, h//2 - 1, w//2-3 - len(boxtextmessage)//2)
    box1.box()    
    stdsrc.refresh()
    box1.refresh()
    stdsrc.addstr(h//2, w//2 - len(boxtextmessage)//2, boxtextmessage)
    # Ask for decryption of transaction records
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
                decrypt_file(stdsrc)
                break
            elif idx == 1:
                break
    stdsrc.clear()
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
            if current_row_idx == 0:
                firstoptionmenu(stdsrc)
            elif current_row_idx == 1:
                stdsrc.clear()
                graph(stdsrc)
            elif current_row_idx == 2:
                cryptovalue(stdsrc)
            elif current_row_idx == 3:
                settings(stdsrc)
            elif current_row_idx == 4:
                screen_exit(stdsrc)
            stdsrc.refresh()
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
        global username 
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

def func1(stdsrc, current_row_idx):
    
    #Transaction managment
    tranmenu = ["Add Transaction", "View and edit Transactions", "Back"]
    
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
    for idx, row in enumerate(tranmenu):
        x = w//2 - len(row)//2
        y = h//2 - len(tranmenu)//2 + tranmenu.index(row)
        if idx == current_row_idx:
            stdsrc.attron(curses.color_pair(3))
            stdsrc.addstr(y, x, row)
            stdsrc.attron(curses.color_pair(1))
        else:
            stdsrc.addstr(y, x, row)
    # Refresh the screen
    stdsrc.refresh()
    

#curses.wrapper(decrypt_file)
curses.wrapper(main)

curses.initscr()

