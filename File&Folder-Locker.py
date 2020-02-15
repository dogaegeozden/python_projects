# NOTES
# If you want this to be work you should create environment variables
# to hide your password in it or else they can open the file in read
# mode an get the password
# getpass() is for hiding password input !!
# You can create environment variables : ** You can learn how to do it
# from python notes you have also
# Start > Control Panel > System and Security > System > Advanged system settings
# > Environment Variables > New or Edit.
# You should also need to change quick access options or else
# they can see where your files are hidden.

import os
from tkinter import *
import getpass

while True:
    password = getpass.getpass("What is your password ?")
    if password == os.environ.get("USER_PASS"):
        print("ACCESS GRANTED")
        root = Tk()
        # path = 'C:\Folder Name'
        path = os.environ.get("USER_FILES_PATH")

        def open():
            os.startfile(path, 'open')

        button = Button(root, text="Open The Folder", command=open)
        button.pack()

        root.mainloop()
        break
    else:
        print("ACCESS DENIED")
