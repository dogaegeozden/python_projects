# Copyright © 2021 All rights reserved. Doga Ege Ozden

# PyAudio v0.2.11: Python Bindings for PortAudio.
# Copyright (c) 2006 Hubert Pham

# This is the part that you import required packages.
import os

# This is the part that you installed required packages
os.system("pip freeze > system-installations-check.txt")

rPackages = []

with open("requirements.txt", "r") as a:
    for line in a:
        pac = line
        rPackages.append(pac[:-1])

with open("system-installations-check.txt", "r") as b:
    b_contents = b.read()

for i in range(len(rPackages)):
    if b_contents.find(rPackages[i]) != -1: # This means if it contains
        print("Required package is installed.")

    elif b_contents.find(rPackages[i]) == -1:
        print("Required package is not installed. Installing...")
        os.system(f'python -m pip install {rPackages[i]}')

import webbrowser
import random
from subprocess import check_output
import pytz
import datetime
from num2words import num2words
import tkinter as tk
from tkinter import filedialog
import shutil
import ctypes, sys
import getpass
import pandas
import numpy as np
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg


# This is the part that includes Windows features.
if os.name == "nt":
    print("You are on a windows machine.")
    print()

    # This is the part you grap the user object
    user = getpass.getuser()

    # This is the part that you grap the calypso's location
    calypsoLocation = os.getcwd()

    # These are the workspace locations.
    desktopPath = "C:\\Users\\{}\\Desktop".format(user)
    if os.path.exists(desktopPath):
        desktop = os.listdir(desktopPath)

    documentsPath = "C:\\Users\\{}\\Documents".format(user)
    if os.path.exists(documentsPath):
        documents = os.listdir(documentsPath)

    workSpacePath = "C:\\Users\\{}\\Desktop\\Work-Space".format(user)
    if os.path.exists(workSpacePath):
        workSpace = os.listdir(workSpacePath)

    testAreaPath = "C:\\Users\\{}\\Desktop\\Test-Area".format(user)
    if os.path.exists(testAreaPath):
        testArea = os.listdir(testAreaPath)

    # This is the part that you added text to speech feauture on windows.
    eSpeakContainter = []
    eSpeakFN = "espeak -v+f2"
    eSpeakStp = "setup_espeak-1.48.04.exe"
    allFileNames = []

    # DEVELOPMENT OPTIONS
    # OPTION 1 YOU CAN SET THE SPEECH PACKAGE TO AN RELATIVE PATH TO MAKE IT START FASTER.
    eSpeakContainter.append(calypsoLocation + "\\" + "eSpeak(location)\\eSpeak\\command_line")

    # OPTION 2 THIS IS THE PART THAT CALYPSO FIND IT'S OWN SPEECH PACKAGE
    # # This is the path that Calypso installs it's own speeh package
    # for currentpath, dirnames, filenames in os.walk("C:\\"):
    #     for file in os.listdir(currentpath):
    #         allFileNames.append(file)
    #
    #     # This is the part that Calypso finds it's own speech package
    #     if eSpeakFN in os.listdir(currentpath):
    #         eSpeakFP = currentpath
    #         eSpeakContainter.append(eSpeakFP)
    #
    # if eSpeakFN in allFileNames:
    #     print("Speech package is installed on this device.")
    #
    # elif eSpeakFN not in allFileNames:
    #     for currentpath, dirnames, filenames in os.walk("C:\\"):
    #         if eSpeakStp in os.listdir(currentpath):
    #             eSpeakStpP = currentpath
    #             os.chdir(eSpeakStpP)
    #             print("You should install the speech package!")
    #             os.startfile(eSpeakStp)
    #             os.chdir(calypsoLocation)

    # In the feature get this path with os.walk method
    os.chdir(eSpeakContainter[0])
    os.system('espeak -v+f2 "Hi, Doga. How are you?, What do you want today ?"')
    os.chdir(calypsoLocation)

    # This is the part that you allow calypso to get system administrator privledge.
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    os.system("cls")
    os.system("prompt Calpso_Interpreter: ")

    # this infinity loop allows you to enter message infinite times if your message exit! program will close
    while True:

        # Here you you should write you message to talk with Calipso.
        message = input("Enter your message here: ")


        mymessage = message.lower().strip()

        # this is the part where you create condition for closing Calypso.
        if mymessage == "exit" or "have" in mymessage and "a" in mymessage and "nice" in mymessage and "day" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Have a nice day. I\'m goding to have a sleep."')
            os.chdir(calypsoLocation)
            break

        elif mymessage == "help":
            print("""
#######################################################################
                      CALYPSO'S COMMANDS

Exit Program:
exit!                                       : To close the Calypso.

Greeting Commands:
["hi","hello","hey"]                        : These commands will make
Calyspo greet you.

Feeling Commands:
["i'm good","i am good","i'm great",
"i am great","i'm wonderful",
"i am wonderful","i'm ok","i am ok",
"i'm bad","i am bad","i'm sad","i am sad",
"i'm terrible","i am terrible",]          : These commands will make
Calypso talk with you in order to make you feel better.

Calypso's ID message:
["introduce yourself","who are you"]       : These commands will make
Calypso introduce herself.

Create File Command:
create file                                : This will ask you three
questions, file location, file name and file extension. And it will
create file depending on your answers.

Clear The Discussion:
clear                                      : This will clear your
chat with Calypso.

Question and Search:
question where should I travel             : Using question keyword
will make Calypso search question on web and give you best answers.

search test.txt                            : Using search keyword will
make Calypso ask questions such as where do you want to the search so
you can make searches on internet and computer partitions.

Security Commands:
password                                   : Generates 12 digit
random password.
lock folder                                : Will lock your folder
with a folder tree.

System Monitor Commands:
task manager                               : Will open task manager
performance manager                        : Will open performance
manager.
system check                               : It will scan all the
protected system files and then fix the corrupt files.

Time Commands:
what time                                  : will give time in hours
and minutes
what day                                   : will give the day
what date                                  : will give the date

Word Counter Command:
word counter                               : will count your words after
you entered a text.

Machine Learning:
examine                                    : will examine the data
that you provide and then learn the parioty the variables that are
having effect on the change of interested variable's value to create
decision tree or make prediction.

#####################################################################

""")


        # This is the part that includes daily talks
        elif mymessage == "thank you" or mymessage == "ty" or mymessage == "thx" or "thank" in mymessage and "you" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Your welcome."')
            os.chdir(calypsoLocation)

        # This is the part that you add translator feature.
        elif mymessage == "speak french":
            os.chdir(eSpeakContainter[0])
            os.system('espeak -vfr+f2 "Mon nom est Calyspo."')
            os.chdir(calypsoLocation)

        elif mymessage == "hi" or mymessage == "hello" or mymessage == "hey":
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Hi"')
            os.chdir(calypsoLocation)

        elif mymessage == "hi calypso" or mymessage == "hey calypso":
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Yes, I\'m listening."')
            os.chdir(calypsoLocation)

        elif mymessage == "welldone" or mymessage == "well done" or mymessage == "good job":
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Thank you."')
            os.chdir(calypsoLocation)

        elif "i'm good" in mymessage or "i am good" in mymessage or "i'm great" in mymessage or "i am great" in mymessage or "i'm wonderful" in mymessage or "i am wonderful" in mymessage or "im good" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Happy to heard that."')
            os.chdir(calypsoLocation)

        elif "i'm ok" in mymessage or "i am ok" in mymessage or "im ok" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Is there problem sir?"')
            os.chdir(calypsoLocation)
            question = input("Enter your answer here(y/n): ")
            answer = question.lower().strip()
            if answer == "y" or answer == "yes" or answer == "yeah" or answer == "yea":
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "What can I do for you?"')
                os.chdir(calypsoLocation)

            elif answer == 'n' or answer == "no" or answer == "nah" or answer == "nahh":
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "Happy to heard that."')
                os.chdir(calypsoLocation)

        elif "i'm bad" in mymessage or "i am bad" in mymessage or "i'm sad" in mymessage or "i am sad" in mymessage or "i'm terrible" in mymessage or "i am terrible" in mymessage or "im bad" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Sorry to heard that. What can I do for you?"')
            os.chdir(calypsoLocation)

        # This is the part that Calypso. Introduces herself.
        elif mymessage == "introduce yourself" or mymessage == "who are you" or message == "who you are" or "introduce" in mymessage and "yourself" in mymessage or "who" in mymessage and "are" in mymessage and "you" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "I\'m Calypso. I born in 25 November, 2019 in a basement."')
            os.chdir(calypsoLocation)

        # This is the daily talks part
        elif mymessage == "how are you" or "how" in mymessage and "are" in mymessage and "you" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "I\'m good. Thank you for asking. How are you?"')
            os.chdir(calypsoLocation)

        # This is the part that Calipso create files and folders for you.
        elif "create" in mymessage and "file" in mymessage or mymessage == "create file" or mymessage == "create a new file":
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Which kind of file do you want?"')
            os.chdir(calypsoLocation)
            question1 = input("Enter which kind of file do you want here(ex:html): ")
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "How do you want me to name it?"')
            os.chdir(calypsoLocation)
            question2 = input("Enter file name here: ")
            os.chdir(eSpeakContainter[0])
            os.system("espeak -v+f2 'Where do you want me to create the file:'")
            print("""Locations:
Desktop
Documents
Work-Space
Test-Area'""")

            os.chdir(calypsoLocation)
            question3 = input("Enter file location here(ex:Desktop): ")
            questionx = question3.lower().strip()

            if questionx == "desktop":
                with open(desktopPath + "\\" + "{}".format(question2) + "." + "{}".format(question1), "w") as f:
                    f.write("Created by Calypso.")
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "You can find the file you want in your desktop."')
                os.chdir(calypsoLocation)

            elif questionx == "documents":
                with open(documentsPath + "\\" + "{}".format(question2) + "." + "{}".format(question1), "w") as f:
                    f.write("Created by Calypso.")
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "You can find the file you want in your documents."')
                os.chdir(calypsoLocation)

            elif questionx == "work-space" or questionx == "work space":
                with open(workSpacePath + "\\" + "{}".format(question2) + "." + "{}".format(question1), "w") as f:
                    f.write("Created by Calypso.")
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "You can find the file you want in your work space."')
                os.chdir(calypsoLocation)

            elif questionx == "test-area" or questionx == "test area":
                with open(testAreaPath + "\\" + "{}".format(question2) + "." + "{}".format(question1), "w") as f:
                    f.write("Created by Calypso.")
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "You can find the file you want in your test area."')
                os.chdir(calypsoLocation)

        # This is the part that clears dialog.
        elif mymessage == "clear":
            os.system("cls")
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "I\'m cleaning our chat"')
            os.chdir(calypsoLocation)

        elif "question" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Do you prefer private search or not?"')
            os.chdir(calypsoLocation)
            question1 = input("Enter your answer here(Private=Yes(y)/UnPrivate=No(n))? ")

            if question1 == "n" or question1 == "no" or question1 == "unp" or question1 == "unprivate" or question1 == "un private":
                lenQuestionWord = len("question")
                questionWordIndex = message.find('question')+lenQuestionWord+1 # Plus one is to get rid of from the white space.
                searchQ = message[questionWordIndex:]
                url = "https://www.google.com.tr/search?q={}".format(searchQ)
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "These are the results I found."')
                os.chdir(calypsoLocation)
                webbrowser.open_new_tab(url)

            elif question1 == "y" or question1 == "yes" or question1 == "p" or question1 == "private":
                lenQuestionWord = len("question")
                questionWordIndex = message.find('question')+lenQuestionWord+1 # Plus one is to get rid of from the white space.
                searchQ = message[questionWordIndex:]
                url = "https://duckduckgo.com/?t=ffab&q={}".format(searchQ)
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "These are the results I found."')
                os.chdir(calypsoLocation)
                os.system('start firefox --private "{}"'.format(url))

        # This is the part that you create search feature.
        elif "search" in mymessage:
            lenSearchWord = len("search")
            searchWordIndex = message.find('search')+lenSearchWord+1 # Plus one is to get rid of from the white space.
            searchedForF = message[searchWordIndex:].strip()
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Where do you want me to do the search?"')
            os.chdir(calypsoLocation)
            listofTargetPaths = []
            numsOfForF = 0

            print("""
Device Partitions:
C
D
E
F

World Wide Web:
Internet, web

""")

            question1 = input("Enter your choice of your partition here(ex:C): ")

            if question1 == "c" or question1 == "C":
                if os.path.exists("{}:\\".format(question1.upper())) == True:

                    for currentpath, dirnames, filenames in os.walk("{}:\\".format(question1.upper())):
                        if searchedForF in os.listdir(currentpath):
                            listofTargetPaths.append(currentpath)

                    if len(listofTargetPaths) == 0:
                        os.chdir(eSpeakContainter[0])
                        os.system('espeak -v+f2 "There is no such a file called {} in partition {}"'.format(searchedForF,question1.upper()))
                        os.chdir(calypsoLocation)
                        print(listofTargetPaths)

                    else:
                        os.chdir(eSpeakContainter[0])
                        os.system('espeak -v+f2 "These are the results that I found."')
                        os.chdir(calypsoLocation)
                        print("RESULTS: ")
                        print()

                        for i in range(len(listofTargetPaths)):
                            numsOfForF += 1

                            if os.path.isfile(listofTargetPaths[i]+"\\"+searchedForF) == True:
                                print("{})".format(numsOfForF)," File Name: ",searchedForF,"Path: ", "{}".format(listofTargetPaths[i]))
                                print()

                            elif os.path.isfile(listofTargetPaths[i]+"\\"+searchedForF) == False:
                                print("{})".format(numsOfForF)," Folder Name: ",searchedForF,"Path: ", "{}".format(listofTargetPaths[i]))
                                print()

                        question2 = input("Enter the number of the file or folder here('none to exit'): ")
                        print()
                        if question2 == "none" or question2 == 0 or question2 == "no" or question2 == "exit":
                            os.chdir(eSpeakContainter[0])
                            os.system('espeak -v+f2 "Ok."')
                            os.chdir(calypsoLocation)

                        else:
                            indexNumofForF = int(question2)-1
                            os.startfile("{}\\{}".format(listofTargetPaths[indexNumofForF],searchedForF))

                else:
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "Sorry partition is not exists."')
                    os.chdir(calypsoLocation)
                    print("Partition {} is not exist".format(question1.upper()))

            elif question1 == "d" or question1 == "D":
                if os.path.exists("{}:\\".format(question1.upper())) == True:

                    for currentpath, dirnames, filenames in os.walk("{}:\\".format(question1.upper())):
                        if searchedForF in os.listdir(currentpath):
                            listofTargetPaths.append(currentpath)

                    if len(listofTargetPaths) == 0:
                        os.chdir(eSpeakContainter[0])
                        os.system('espeak -v+f2 "There is no such a file called {} in partition {}"'.format(searchedForF,question1.upper()))
                        os.chdir(calypsoLocation)
                        print(listofTargetPaths)

                    else:
                        os.chdir(eSpeakContainter[0])
                        os.system('espeak -v+f2 "These are the results that I found."')
                        os.chdir(calypsoLocation)
                        print("RESULTS: ")
                        print()

                        for i in range(len(listofTargetPaths)):
                            numsOfForF += 1

                            if os.path.isfile(listofTargetPaths[i]+"\\"+searchedForF) == True:
                                print("{})".format(numsOfForF)," File Name: ",searchedForF,"Path: ", "{}".format(listofTargetPaths[i]))
                                print()

                            elif os.path.isfile(listofTargetPaths[i]+"\\"+searchedForF) == False:
                                print("{})".format(numsOfForF)," Folder Name: ",searchedForF,"Path: ", "{}".format(listofTargetPaths[i]))
                                print()

                        question2 = input("Enter the number of the file or folder here('none to exit'): ")
                        print()
                        if question2 == "none" or question2 == 0 or question2 == "no" or question2 == "exit":
                            os.chdir(eSpeakContainter[0])
                            os.system('espeak -v+f2 "Ok."')
                            os.chdir(calypsoLocation)

                        else:
                            indexNumofForF = int(question2)-1
                            os.startfile("{}\\{}".format(listofTargetPaths[indexNumofForF],searchedForF))

                else:
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "Sorry partition is not exists."')
                    os.chdir(calypsoLocation)
                    print("Partition {} is not exist".format(question1.upper()))

            elif question1 == "e" or question1 == "E":
                if os.path.exists("{}:\\".format(question1.upper())) == True:

                    for currentpath, dirnames, filenames in os.walk("{}:\\".format(question1.upper())):
                        if searchedForF in os.listdir(currentpath):
                            listofTargetPaths.append(currentpath)



                    if len(listofTargetPaths) == 0:
                        os.chdir(eSpeakContainter[0])
                        os.system('espeak -v+f2 "There is no such a file called {} in partition {}"'.format(searchedForF,question1.upper()))
                        os.chdir(calypsoLocation)
                        print(listofTargetPaths)

                    else:
                        os.chdir(eSpeakContainter[0])
                        os.system('espeak -v+f2 "These are the results that I found."')
                        os.chdir(calypsoLocation)
                        print("RESULTS: ")
                        print()

                        for i in range(len(listofTargetPaths)):
                            numsOfForF += 1

                            if os.path.isfile(listofTargetPaths[i]+"\\"+searchedForF) == True:
                                print("{})".format(numsOfForF)," File Name: ",searchedForF,"Path: ", "{}".format(listofTargetPaths[i]))
                                print()

                            elif os.path.isfile(listofTargetPaths[i]+"\\"+searchedForF) == False:
                                print("{})".format(numsOfForF)," Folder Name: ",searchedForF,"Path: ", "{}".format(listofTargetPaths[i]))
                                print()

                        question2 = input("Enter the number of the file or folder here('none to exit'): ")
                        print()
                        if question2 == "none" or question2 == 0 or question2 == "no" or question2 == "exit":
                            os.chdir(eSpeakContainter[0])
                            os.system('espeak -v+f2 "Ok."')
                            os.chdir(calypsoLocation)

                        else:
                            indexNumofForF = int(question2)-1
                            os.startfile("{}\\{}".format(listofTargetPaths[indexNumofForF],searchedForF))

                else:
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "Sorry partition is not exists."')
                    os.chdir(calypsoLocation)
                    print("Partition {} is not exist".format(question1.upper()))

            elif question1 == "f" or question1 == "F":
                if os.path.exists("{}:\\".format(question1.upper())) == True:

                    for currentpath, dirnames, filenames in os.walk("{}:\\".format(question1.upper())):
                        if searchedForF in os.listdir(currentpath):
                            listofTargetPaths.append(currentpath)

                    if len(listofTargetPaths) == 0:
                        os.chdir(eSpeakContainter[0])
                        os.system('espeak -v+f2 "There is no such a file called {} in partition {}"'.format(searchedForF,question1.upper()))
                        os.chdir(calypsoLocation)
                        print(listofTargetPaths)

                    else:
                        os.chdir(eSpeakContainter[0])
                        os.system('espeak -v+f2 "These are the results that I found."')
                        os.chdir(calypsoLocation)
                        print("RESULTS: ")
                        print()

                        for i in range(len(listofTargetPaths)):
                            numsOfForF += 1

                            if os.path.isfile(listofTargetPaths[i]+"\\"+searchedForF) == True:
                                print("{})".format(numsOfForF)," File Name: ",searchedForF,"Path: ", "{}".format(listofTargetPaths[i]))
                                print()

                            elif os.path.isfile(listofTargetPaths[i]+"\\"+searchedForF) == False:
                                print("{})".format(numsOfForF)," Folder Name: ",searchedForF,"Path: ", "{}".format(listofTargetPaths[i]))
                                print()

                        question2 = input("Enter the number of the file or folder here('none to exit'): ")
                        print()
                        if question2 == "none" or question2 == 0 or question2 == "no" or question2 == "exit":
                            os.chdir(eSpeakContainter[0])
                            os.system('espeak -v+f2 "Ok."')
                            os.chdir(calypsoLocation)

                        else:
                            indexNumofForF = int(question2)-1
                            os.startfile("{}\\{}".format(listofTargetPaths[indexNumofForF],searchedForF))

                else:
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "Sorry partition is not exists."')
                    os.chdir(calypsoLocation)
                    print("Partition {} is not exist".format(question1.upper()))

            elif "web" in question1 or "internet" in question1 or "Internet" in question1 or "Web" in question1:
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "Do you prefer private search or not?"')
                os.chdir(calypsoLocation)
                question1 = input("Enter your answer here(Private=Yes(y)/UnPrivate=No(n))? ")

                if question1 == "n" or question1 == "no" or question1 == "unp" or question1 == "unprivate" or question1 == "un private":
                    lenQuestionWord = len("search")
                    questionWordIndex = message.find('search')+lenQuestionWord+1 # Plus one is to get rid of from the white space.
                    searchQ = message[questionWordIndex:]
                    url = "https://www.google.com.tr/search?q={}".format(searchQ)
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "These are the results I found."')
                    os.chdir(calypsoLocation)
                    webbrowser.open_new_tab(url)

                elif question1 == "y" or question1 == "yes" or question1 == "p" or question1 == "private":
                    lenQuestionWord = len("search")
                    questionWordIndex = message.find('search')+lenQuestionWord+1 # Plus one is to get rid of from the white space.
                    searchQ = message[questionWordIndex:]
                    url = "https://duckduckgo.com/?t=ffab&q={}".format(searchQ)
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "These are the results I found."')
                    os.chdir(calypsoLocation)
                    os.system('start firefox --private "{}"'.format(url))

            else:
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "You entered an invalid value."')
                os.chdir(calypsoLocation)

        # This is the part that you add password generator feature.
        elif "password" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Here is your password"')
            os.chdir(calypsoLocation)
            lcletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            ucletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", ",", ".", "<", ">", "/", "?", ";", ":"]

            rndmlclttrs = random.choices(lcletters, k=3)
            rndmuclttrs = random.choices(ucletters, k=3)
            rndmnmbrs = random.choices(numbers, k=3)
            rndmsymbls = random.choices(symbols, k=3)

            newlist = rndmlclttrs + rndmuclttrs + rndmnmbrs + rndmsymbls

            password = random.choices(newlist, k=12)

            def convert(password):
                new = ""

                for x in password:
                    new += x
                return new

            print("Password : ",convert(password))

        # This is the part that you created folder locker feature.
        elif "lock" in mymessage and "files" in mymessage or "lock" in mymessage or "folder" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Select the folder that you want to encrypt."')
            os.chdir(calypsoLocation)
            root = tk.Tk()
            root.withdraw()

            file_path = filedialog.askdirectory()

            from_dir= file_path
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Enter a new name for new encrypted folder to be created."')
            os.chdir(calypsoLocation)
            fname=input('Enter folder name to be created: ')
            caracterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "!", "@", "#", "$", "%", "^", "&", "(", ")", "-", "_", "=", "+", ",", ";", "[", "]", "{", "}" ]
            caracterstring = ""
            for c in caracterlist:
                s = str(c)
                caracterstring += s + ", "

            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Create a password by fallowing the instructions below."')
            os.chdir(calypsoLocation)
            pasw=input("Enter the password(Note: You can't use all the caracters such as capital letters and some of the symbols here is list of the caracters that you can use {}.): ".format(caracterstring))

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

            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Encryption is done you can find your encrypted folder in your desktop."')
            os.chdir(calypsoLocation)

        # This part is the part that you add task manager feature.
        elif "task manager" in mymessage or "tasks" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "I\'m opening the task manager."')
            os.chdir(calypsoLocation)
            os.system("taskmgr")

        # This is the part that you create performance monitor feature.
        elif "performance" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "I\'m opening the performance monitor."')
            os.chdir(calypsoLocation)
            os.system("perfmon.exe")

        # This is the part that you create scan and fix feature. !!You need to learn how to run it as administrator.
        elif "system" in mymessage and "check" in mymessage or mymessage == "system file check":
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "I need administrator priviledges to execute this operation."')
            os.chdir(calypsoLocation)
            question = input("Can I get administrator priviledges?(y/n) ")
            questionModif = question.lower().strip()
            if questionModif == "y" or questionModif == "yes":
                if is_admin():
                    print("Getting administrator priviledges...")
                    print("Administrator privledges = True")
                    # Enter your code here
                    os.system("sfc /scannow")
                else:
                    # Re-run the program with admin rights
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)



        # This is the part that includes word counter feature.
        elif "word counter" in mymessage or "count" in mymessage and "words" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Enter your text here"')
            os.chdir(calypsoLocation)
            nw = 0
            while True:
                article = input("""Enter your article here: """)
                print()
                if article == "exit":
                    break
                wl = article.split(" ")

                for w in wl:
                    nw += 1

                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "This text includes {} words."'.format(nw))
                os.chdir(calypsoLocation)
                print("Number of words: ",nw)
                print()

        elif "do the thing" == mymessage or "do" in mymessage and "thing" in mymessage or "do" in mymessage and "the" in mymessage:
            dt_time_now = datetime.datetime.now()
            stringTimeP1 = dt_time_now.strftime("%H %M")
            stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "It\'s {} sir!"'.format(stringTimeP2))
            os.chdir(calypsoLocation)

        elif "what" in mymessage and "date" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Where are you?"')
            os.chdir(calypsoLocation)
            question1 = input("Enter where you are?(Canada(C)/Turkey(T)/ComputerTime(Com) ")
            answer1 = question1.lower()
            if answer1 == "c":
                today = datetime.datetime.now(tz=pytz.timezone("Canada/Atlantic"))
                stringTodayP1 = today.strftime("%B %d %Y")
                stringTodayP2 = stringTodayP1.split(" ")[0] + " " + num2words(stringTodayP1.split(" ")[1]) + " " + num2words(stringTodayP1.split(" ")[2])
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "{}"'.format(stringTodayP2))
                os.chdir(calypsoLocation)
                print("Date: ",today.strftime('%b %d %Y'))
            elif answer1 == "t":
                today = datetime.datetime.now(tz=pytz.timezone("Turkey"))
                stringTodayP1 = today.strftime("%B %d %Y")
                stringTodayP2 = stringTodayP1.split(" ")[0] + " " + num2words(stringTodayP1.split(" ")[1]) + " " + num2words(stringTodayP1.split(" ")[2])
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "{}"'.format(stringTodayP2))
                os.chdir(calypsoLocation)
                print("Date: ",today.strftime('%b %d %Y'))
            elif answer1 == "com":
                today = datetime.datetime.now()
                stringTodayP1 = today.strftime("%B %d %Y")
                stringTodayP2 = stringTodayP1.split(" ")[0] + " " + num2words(stringTodayP1.split(" ")[1]) + " " + num2words(stringTodayP1.split(" ")[2])
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "{}"'.format(stringTodayP2))
                os.chdir(calypsoLocation)
                print("Date: ",today.strftime('%b %d %Y'))

        elif "what" in mymessage and "day" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Where are you?"')
            os.chdir(calypsoLocation)
            question1 = input("Enter where you are?(Canada(C)/Turkey(T)/ComputerTime(Com) ")
            answer1 = question1.lower()
            if answer1 == "c":
                todayDay = datetime.datetime.now(tz=pytz.timezone("Canada/Atlantic"))
                formattedDay = todayDay.strftime("%A")
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(formattedDay))
                os.chdir(calypsoLocation)
                print("Day: ",formattedDay)
            elif answer1 == "t":
                todayDay = datetime.datetime.now(tz=pytz.timezone("Turkey"))
                formattedDay = todayDay.strftime("%A")
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(formattedDay))
                os.chdir(calypsoLocation)
                print("Day: ",formattedDay)
            elif answer1 == "com":
                todayDay = datetime.datetime.now()
                formattedDay = todayDay.strftime("%A")
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(formattedDay))
                os.chdir(calypsoLocation)
                print("Day: ",formattedDay)


        elif "what" in mymessage and "time" in mymessage:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Where are you? "')
            os.chdir(calypsoLocation)
            print("""
KNOWN LOCATIONS
Turkey: Tr
Canada: Ca
Brazil: Bra
Russia: Rus
India: Ind
China: Chi
South Africa: Sa
""")
            userselection = str(input("Enter your selection here: "))
            caseinsensetiveselection = userselection.lower()


            if caseinsensetiveselection == "tr" or caseinsensetiveselection == "turkey":
                # This is the part that includes turkey's timezone.
                def dt_time_turkey():
                    return datetime.datetime.now(tz=pytz.timezone("Turkey"))

                stringTimeP1 = dt_time_turkey().strftime("%H %M")
                stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                os.chdir(calypsoLocation)

                print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                print()

            elif caseinsensetiveselection == "ca" or caseinsensetiveselection == "canada":
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "What is your timezone? "')
                os.chdir(calypsoLocation)
                print("CANADA TIMEZONES")
                print("Atlantic(A)")
                print("Central(C)")
                print("Eastern(E)")
                print("Mountain(M)")
                print("New Foundland(NF)")
                print("Pacific(P)")
                print("Saskatchewan(S)")
                print("Yukon(Y)")
                print()

                question1 = input("Enter your timezone here: ")
                answer1 = question1.lower()
                if answer1 == "atlantic" or answer1 == "a":
                    dt_time_cad_atlantic = datetime.datetime.now(tz=pytz.timezone("Canada/Atlantic"))

                    stringTimeP1 = dt_time_cad_atlantic.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "central" or answer1 == "c":
                    dt_time_cad_central = datetime.datetime.now(tz=pytz.timezone("Canada/Central"))

                    stringTimeP1 = dt_time_cad_central.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "eastern" or answer1 == "e":
                    dt_time_cad_eastern = datetime.datetime.now(tz=pytz.timezone("Canada/Eastern"))

                    stringTimeP1 = dt_time_cad_eastern.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "mountain" or answer1 == "m":
                    dt_time_cad_mountain = datetime.datetime.now(tz=pytz.timezone("Canada/Mountain"))

                    stringTimeP1 = dt_time_cad_mountain.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "newfoundland" or answer1 == "nf" or answer1 == "new foundland" or answer1 =="nfl":
                    dt_time_cad_newfoundland = datetime.datetime.now(tz=pytz.timezone("Canada/Newfoundland"))

                    stringTimeP1 = dt_time_cad_newfoundland.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "pacific" or answer1 == "p":
                    dt_time_cad_pacific = datetime.datetime.now(tz=pytz.timezone("Canada/Pacific"))

                    stringTimeP1 = dt_time_cad_pacific.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "saskatchewan" or answer1 == "s":
                    dt_time_cad_saskatchewan = datetime.datetime.now(tz=pytz.timezone("Canada/Saskatchewan"))

                    stringTimeP1 = dt_time_cad_saskatchewan.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "yukon" or answer1 == "y":
                    dt_time_cad_yukon = datetime.datetime.now(tz=pytz.timezone("Canada/Yukon"))

                    stringTimeP1 = dt_time_cad_yukon.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                else:
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "Sorry I coudln\'t understand"')
                    os.chdir(calypsoLocation)


            elif caseinsensetiveselection == "bra" or caseinsensetiveselection == "brazil":
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "What is your timezone? "')
                os.chdir(calypsoLocation)
                print("BRAZIL'S TIMEZONES")
                print("Acre(A)")
                print("Denoronha(D)")
                print("East(E)")
                print("West(W)")
                print()

                question1 = input("Enter your timezone here: ")
                answer1 = question1.lower()
                if answer1 == "acre" or answer1 == "a":
                    dt_time_braz_acre = datetime.datetime.now(tz=pytz.timezone("Brazil/Acre"))

                    stringTimeP1 = dt_time_braz_acre.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "denoronha" or answer1 == "d":
                    dt_time_braz_denoronha = datetime.datetime.now(tz=pytz.timezone("Brazil/DeNoronha"))

                    stringTimeP1 = dt_time_braz_denoronha.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "east" or answer1 == "e":
                    dt_time_braz_east = datetime.datetime.now(tz=pytz.timezone("Brazil/East"))

                    stringTimeP1 = dt_time_braz_east.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "west" or answer1 == "w":
                    dt_time_braz_west = datetime.datetime.now(tz=pytz.timezone("Brazil/West"))

                    stringTimeP1 = dt_time_braz_west.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                else:
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "Sorry I coudln\'t understand"')
                    os.chdir(calypsoLocation)


            elif caseinsensetiveselection == "rus" or caseinsensetiveselection == "russia":
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "What is your timezone? "')
                os.chdir(calypsoLocation)
                print("RUSSIA'S TIMEZONES")
                print("Kamchatka Krai, Russia(KK)")
                print("Magadan(M)")
                print("Sakhalin(S)")
                print("Vladivostok(V)")
                print("Yakutsk(Y)")
                print("Irkutsk(I)")
                print("Novosibirsk(N)")
                print("Samara(SAM)")
                print("Kaliningrad(K)")
                print()

                question1 = input("Enter your timezone here: ")
                answer1 = question1.lower()
                if answer1 == "kamchatka krai, russia" or answer1 == "kk" or answer1 == "kamchatka":
                    dt_time_rsy_krai = datetime.datetime.now(tz=pytz.timezone("Asia/Kamchatka"))

                    stringTimeP1 = dt_time_rsy_krai.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "magadan" or answer1 == "m":
                    dt_time_rsy_magadan = datetime.datetime.now(tz=pytz.timezone("Asia/Magadan"))

                    stringTimeP1 = dt_time_rsy_magadan.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "sakhalin" or answer1 == "s":
                    dt_time_rsy_sakhalin = datetime.datetime.now(tz=pytz.timezone("Asia/Sakhalin"))

                    stringTimeP1 = dt_time_rsy_sakhalin.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "vladivostok" or answer1 == "v":
                    dt_time_rsy_vladivostok = datetime.datetime.now(tz=pytz.timezone("Asia/Vladivostok"))

                    stringTimeP1 = dt_time_rsy_vladivostok.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "yakutsk" or answer1 == "y":
                    dt_time_rsy_yakutsk = datetime.datetime.now(tz=pytz.timezone("Asia/Yakutsk"))

                    stringTimeP1 = dt_time_rsy_yakutsk.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "irkutsk" or answer1 == "i":
                    dt_time_rsy_irkutsk = datetime.datetime.now(tz=pytz.timezone("Asia/Irkutsk"))

                    stringTimeP1 = dt_time_rsy_irkutsk.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "novosibirsk" or answer1 == "n":
                    dt_time_rsy_novosibirsk = datetime.datetime.now(tz=pytz.timezone("Asia/Novosibirsk"))

                    stringTimeP1 = dt_time_rsy_novosibirsk.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "samara" or answer1 == "sam":
                    dt_time_rsy_samara = datetime.datetime.now(tz=pytz.timezone("Europe/Samara"))

                    stringTimeP1 = dt_time_rsy_samara.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "kaliningrad" or answer1 == "k":
                    dt_time_rsy_kaliningrad = datetime.datetime.now(tz=pytz.timezone("Europe/Kaliningrad"))

                    stringTimeP1 = dt_time_rsy_kaliningrad.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                else:
                    os.chdir(eSpeakContainter[0])
                    os.system('espeak -v+f2 "Sorry I coudln\'t understand"')
                    os.chdir(calypsoLocation)



            elif caseinsensetiveselection == "ind" or caseinsensetiveselection == "india":
                dt_time_indi_antananarivo = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

                stringTimeP1 = dt_time_indi_antananarivo.strftime("%H %M")
                stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                os.chdir(calypsoLocation)

                print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                print()

            elif caseinsensetiveselection == "chi" or caseinsensetiveselection == "china":
                dt_time_chi_gmt8 = datetime.datetime.now(tz=pytz.timezone("Asia/Shanghai"))

                stringTimeP1 = dt_time_chi_gmt8.strftime("%H %M")
                stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                os.chdir(calypsoLocation)

                print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                print()

            elif caseinsensetiveselection == "sa" or caseinsensetiveselection == "south africa":
                dt_time_sa_gmt2 = datetime.datetime.now(tz=pytz.timezone("Africa/Johannesburg"))

                stringTimeP1 = dt_time_sa_gmt2.strftime("%H %M")
                stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                os.chdir(calypsoLocation)

                print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                print()

            else:
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "Sorry I coudln\'t understand"')
                os.chdir(calypsoLocation)


        # This is the part that you create file manager feature.

        # Machine learning/Examine feature
        elif "examine" in mymessage:
            # Calypso's speach; it askes you to provide data base
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Can you select the data base. I only know, how to read csv files."')
            os.chdir(calypsoLocation)

            # file selection dialog box with tkinter
            file_path = filedialog.askopenfilename()

            # It reads the csv file
            df = pandas.read_csv(file_path)

            dictCols = []

            for c in df:
                for va in df[c]:
                    if type(va) == str:
                        dictCols.append(c)

            dictCols = sorted(set(dictCols))

            print(f'List of the columns needs to be used to create dictionaries: {dictCols}\n')

            print("Dictionaries")

            for co in dictCols:
                keys = sorted(set(df[co].tolist()))

                values = [int(n) for n in range(len(sorted(set(df[co]))))]

                d = {}
                for v in values:
                    d[v] = values[v]

                for k in keys:
                    d[k] = d[keys.index(k)]
                    del d[keys.index(k)]

                print(d)
                df[co] = df[co].map(d)

            print()

            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Enter the name of the column that you interest with."')
            os.chdir(calypsoLocation)
            interestCol = input("Enter the name of the interested column: ")
            print()

            features = [str(col) for col in df]
            print(f'List of the columns: {features}')
            print()
            features.remove(interestCol)

            X = df[features]
            y = df[interestCol]

            dtree = DecisionTreeClassifier()
            dtree = dtree.fit(X, y)

            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Do you want me to show my decision tree or make predictions?"')
            os.chdir(calypsoLocation)
            decisionQ = str(input("Enter your choice(d:'Decision Tree', p:'Prediction'): "))

            if decisionQ == "d":
                data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
                graph = pydotplus.graph_from_dot_data(data)
                graph.write_png('calypso_decisiontree.png')
                img=pltimg.imread('calypso_decisiontree.png')
                imgplot = plt.imshow(img)
                plt.show()

            elif decisionQ == "p":
                answers = []
                listOfCols = []

                for aCol in df:
                    listOfCols.append(aCol)

                for col in listOfCols:
                    if len(answers) == len(listOfCols)-1 :
                        os.chdir(eSpeakContainter[0])
                        os.system('espeak -v+f2 "Thank you for entering values."')
                        os.chdir(calypsoLocation)

                    elif len(answers) != len(listOfCols)-1:
                        os.chdir(eSpeakContainter[0])
                        os.system('espeak -v+f2 "Enter a value for column {}."'.format(col))
                        os.chdir(calypsoLocation)
                        question = input(f'Enter a value for column {col}: ')
                        answers.append(question)

                # List of the values that are required to make predictions
                vRFPL = [float(q) for q in answers]
                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "Here are the values that you entered."')
                os.chdir(calypsoLocation)
                print(f'List of the values that you entered: {vRFPL}')
                print()

                os.chdir(eSpeakContainter[0])
                os.system('espeak -v+f2 "Here is your answer. Please check the dictionaries if you get confused."')
                os.chdir(calypsoLocation)
                cAnswer = dtree.predict(([vRFPL]))
                print(f'Intersted column: {interestCol}\nAnswer: {cAnswer}\n')

        # This is the part that Calipso doesn't understand what you are saying.
        else:
            os.chdir(eSpeakContainter[0])
            os.system('espeak -v+f2 "Sory, I couldn\'t understand. Can you repeat?"')
            os.chdir(calypsoLocation)
