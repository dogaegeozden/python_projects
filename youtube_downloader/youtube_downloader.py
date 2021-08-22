import os
from pytube import YouTube

os.system("pip freeze > requirements_check.txt")

requiredPacs = []
with open(f'requirements.txt', 'r') as a:
    for ln in a:
        requiredPacs.append(ln)

with open(f'requirements_check.txt', "r") as b:
    b_contents = b.read()

for i in range(len(requiredPacs)):
    if b_contents.find(requiredPacs[i]) != -1: # This means if it contains
        print("Required package is installed.")
    elif b_contents.find(requiredPacs[i]) == -1:
        os.system(f'python -m pip install {requiredPacs[i]}')


while True:
    try:
        question1 = str(input("Would you like to download as video or audio? (v/a)"))
        question2 = input("Enter you the url here: ")
        if question1 == "v":
            yt = YouTube(f'{question2}')
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

        if question1 == "a":
            yt = YouTube(f'{question2}')
            yt.streams.filter(only_audio=True).first().download()
    except:
        print("You didn't entered a valid value. You should be entering a url as fallows: https://www.youtube.com/watch?v=htrxWYQayk0")
