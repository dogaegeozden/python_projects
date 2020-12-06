import os
import shutil
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()
from_dir= file_path
fname=input('Enter folder name to be created: ')
caracterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "!", "@", "#", "$", "%", "^", "&", "(", ")", "-", "_", "=", "+", ",", ";", "[", "]", "{", "}" ]
caracterstring = ""
for c in caracterlist:
    s = str(c)
    caracterstring += s + ", "

pasw=input("Enter a password(Note: You can't use all the caracters such as capital letters and some of the symbols here is list of the caracters that you can use {}.): ".format(caracterstring))

user = os.getcwd().split("\\")[2]
todir='C:/Users/{}/Desktop'.format(user)
todir=os.path.join(todir,fname)
os.mkdir(todir)

for i in pasw:
    for j in caracterlist:
        path=os.path.join(todir,str())
        try:
            os.mkdir(path)
        except:
            print('error1')
        for k in caracterlist:
            path2=os.path.join(path,str(k))
            try:
                os.mkdir(path2)
            except:
                print('processing')

    todir=todir+'/'+i

try:
    todir += "/" + fname
    shutil.copytree(from_dir,todir)
except:
    print()

print("Encryption is done!")
print("You can find the encrypted folder in your desktop.")
