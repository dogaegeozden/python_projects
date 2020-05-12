# For general security you should avoid words such as personal files when
# you are hiding your files because they can be found by those key
# words.
# !! Note: If you wanna use this folderlocker on a mac or any linux based operating system
# you should change the todir='path' to your desktop path or your documents path.
# ex: '/home/<user>/Desktop'

import os
import shutil

from_dir=input('ENTER the absoulute path of folder to protect(Note: You should change the backward slashs to forward slashs.): ')
fname=input('Enter folder name of create: ')
pasw=input('Enter the password(Note: With numbers it can have any length.): ')
user=input('Enter you user name(Note: You enter the user name so many people can use): ')
print('This script will create a the folder you named in your desktop.')

todir='C:/Users/{}/Desktop'.format(user)
todir=os.path.join(todir,fname)
os.mkdir(todir)

for i in pasw:
    for j in range(1,11):
        path=os.path.join(todir,str())
        try:
            os.mkdir(path)
        except:
            print('error1')
        for k in range(1,11):
            path2=os.path.join(path,str(k))
            try:
                os.mkdir(path2)
            except:
                print('error2')

    todir=todir+'/'+i

try:
    shutil.move(from_dir,todir)
except:
    print()
