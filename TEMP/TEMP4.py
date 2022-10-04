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
        time.sleep(2)
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