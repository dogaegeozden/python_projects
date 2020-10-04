# For general security you should avoid words such as personal files when
# you are hiding your files because they can be found by those key
# words.
# !! Note: If you wanna use this folderlocker on a mac or any linux based operating system
# you should change the todir='path' to your desktop path or your documents path.
# ex: '/home/<user>/Desktop'

import os
import shutil

print("This application designed for Windows Operating Systems")
from_dir=input('ENTER the absoulute path of folder to protect(Note: You should change the backward slashs to forward slashs. You can find the full path by right clicking on your folder inside security tab): ')
fname=input('Enter folder name of create: ')
caracterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "!", "@", "#", "$", "%", "^", "&", "(", ")", "-", "_", "=", "+", ",", ";", "[", "]" ]
caracterstring = ""
for c in caracterlist:
    s = str(c)
    caracterstring += s + ", "

pasw=input("Enter the password(Note: You can't use all the caracters such as capital letters and some of the symbols here is list of the caracters that you can use {}.): ".format(caracterstring))

print('This script will create a the folder you named in your desktop.')

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
