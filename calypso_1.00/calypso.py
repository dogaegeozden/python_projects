#!/usr/bin/python3
# Copyright © 2021 All rights reserved. Doga Ege Ozden

# First You should import the os module
import os

# This is the part that includes Windows features.
if os.name == "nt":
    print("You are on a windows machine.")

    # OPTION 1: You can use bin folder and settings files to control calypso
    # This is start up settings. So, if you want calypso to start on boot you should see bootsettings file.
    startUpSetting = None
    calypsoLocation = "E:\\work_space\\calypso_1.00"
    sString = "Start Calypso at every computer start up = "
    lStrring = "Location to start Calypso on every start up = "
    sStatuCheck = False
    allFileNames = []

    # These are the variables required for espeak package control
    eSpeakContainer = []
    eSpeakFN = "espeak.exe"

    for path, dirname, filename in os.walk(calypsoLocation):
        for file in os.listdir(path):
            allFileNames.append(file)

        # This is the part that Calypso finds it's own speech package
        if eSpeakFN in os.listdir(path):
            eSpeakFP = path
            eSpeakContainer.append(eSpeakFP)

    # These are imported libraries.
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
    import math
    from decimal import Decimal
    from pytube import YouTube

    # This is the part you grap the user object
    user = getpass.getuser()

    # These are the workspace locations.
    desktopPath = "E:\\desktop"
    if os.path.exists(desktopPath):
        desktop = os.listdir(desktopPath)
    else:
        try:
            os.mkdir("E:\\desktop")
        except:
            print("Partition E: doesn't exist.")

    documentsPath = "E:\\documents"
    if os.path.exists(documentsPath):
        documents = os.listdir(documentsPath)
    else:
        try:
            os.mkdir("E:\\documents")
        except:
            print("Partition E: doesn't exist.")

    workSpacePath = "E:\\work_space"
    if os.path.exists(workSpacePath):
        workSpace = os.listdir(workSpacePath)
    else:
        try:
            os.mkdir("E:\\work_space")
        except:
            print("Partition E: doesn't exist.")

    testAreaPath = "E:\\test_area"
    if os.path.exists(testAreaPath):
        testArea = os.listdir(testAreaPath)
    else:
        try:
            os.mkdir("E:\\test_area")
        except:
            print("Partition E: doesn't exist.")

    # In the feature get this path with os.walk method
    os.chdir(eSpeakContainer[0])
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
            os.chdir(eSpeakContainer[0])
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
password                                   : Generates 20 digit
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

Calcultor feature:
["open the calculator", "calculator", "open calculator"]  : will
open the calculator it includes 3 features 1 is under development.

Translator Feature:
"french translator"                        : will activate the
french translator feature

Youtube Feature:
download video                             : to download videos from
YouTube
download audio                             : to download audios from
YouTube

#####################################################################

""")
        # This is the part that includes daily talks
        elif mymessage == "thank you" or mymessage == "ty" or mymessage == "thx" or "thank" in mymessage and "you" in mymessage:
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Your welcome."')
            os.chdir(calypsoLocation)

        elif mymessage == "hi" or mymessage == "hello" or mymessage == "hey":
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Hi"')
            os.chdir(calypsoLocation)

        elif mymessage == "hi calypso" or mymessage == "hey calypso":
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Yes, I\'m listening."')
            os.chdir(calypsoLocation)

        elif mymessage == "welldone" or mymessage == "well done" or mymessage == "good job":
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Thank you."')
            os.chdir(calypsoLocation)

        elif "i'm good" in mymessage or "i am good" in mymessage or "i'm great" in mymessage or "i am great" in mymessage or "i'm wonderful" in mymessage or "i am wonderful" in mymessage or "im good" in mymessage:
            if "hbu" in mymessage:
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "I\'m good too. Happy to heard that."')
                os.chdir(calypsoLocation)
            else:
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "Happy to heard that."')
                os.chdir(calypsoLocation)

        elif "i'm ok" in mymessage or "i am ok" in mymessage or "im ok" in mymessage:
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Is there problem sir?"')
            os.chdir(calypsoLocation)
            question = input("Enter your answer here(y/n): ")
            answer = question.lower().strip()
            if answer == "y" or answer == "yes" or answer == "yeah" or answer == "yea":
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "What can I do for you?"')
                os.chdir(calypsoLocation)

            elif answer == 'n' or answer == "no" or answer == "nah" or answer == "nahh":
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "Happy to heard that."')
                os.chdir(calypsoLocation)

        elif "i'm bad" in mymessage or "i am bad" in mymessage or "i'm sad" in mymessage or "i am sad" in mymessage or "i'm terrible" in mymessage or "i am terrible" in mymessage or "im bad" in mymessage or "i'm not good" in mymessage or "im not good" in mymessage:
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Sorry to heard that. What can I do for you?"')
            os.chdir(calypsoLocation)

        # This is the part that Calypso. Introduces herself.
        elif mymessage == "introduce yourself" or mymessage == "who are you" or message == "who you are" or "introduce" in mymessage and "yourself" in mymessage or "who" in mymessage and "are" in mymessage and "you" in mymessage:
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "I\'m Calypso. I born in 25 November, 2019 in a basement."')
            os.chdir(calypsoLocation)

        # This is the daily talks part
        elif mymessage == "how are you" or "how" in mymessage and "are" in mymessage and "you" in mymessage:
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "I\'m good. Thank you for asking. How are you?"')
            os.chdir(calypsoLocation)

        # This is the part that Calipso create files and folders for you.
        elif "create" in mymessage and "file" in mymessage or mymessage == "create file" or mymessage == "create a new file":
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Which kind of file do you want?"')
            os.chdir(calypsoLocation)
            question1 = input("Enter which kind of file do you want here(ex:html): ")
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "How do you want me to name it?"')
            os.chdir(calypsoLocation)
            question2 = input("Enter file name here: ")
            os.chdir(eSpeakContainer[0])
            os.system("espeak -v+f2 'Where do you want me to create the file:'")
            print("""Locations:
desktop
documents
work_space
test_area'""")

            os.chdir(calypsoLocation)
            question3 = input("Enter file location here(ex:Desktop): ")
            questionx = question3.lower().strip()

            if questionx == "desktop":
                with open(desktopPath + "\\" + "{}".format(question2) + "." + "{}".format(question1), "w") as f:
                    f.write("Created by Calypso.")
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "You can find the file you want in your desktop."')
                os.chdir(calypsoLocation)

            elif questionx == "documents":
                with open(documentsPath + "\\" + "{}".format(question2) + "." + "{}".format(question1), "w") as f:
                    f.write("Created by Calypso.")
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "You can find the file you want in your documents."')
                os.chdir(calypsoLocation)

            elif questionx == "work_space" or questionx == "work space":
                with open(workSpacePath + "\\" + "{}".format(question2) + "." + "{}".format(question1), "w") as f:
                    f.write("Created by Calypso.")
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "You can find the file you want in your work space."')
                os.chdir(calypsoLocation)

            elif questionx == "test_area" or questionx == "test area":
                with open(testAreaPath + "\\" + "{}".format(question2) + "." + "{}".format(question1), "w") as f:
                    f.write("Created by Calypso.")
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "You can find the file you want in your test area."')
                os.chdir(calypsoLocation)

        # This is the part that clears dialog.
        elif mymessage == "clear":
            os.system("cls")
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "I\'m cleaning our chat"')
            os.chdir(calypsoLocation)

        elif "question" in mymessage:
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Do you prefer private search or not?"')
            os.chdir(calypsoLocation)
            question1 = input("Enter your answer here(Private=Yes(y)/UnPrivate=No(n))? ")

            if question1 == "n" or question1 == "no" or question1 == "unp" or question1 == "unprivate" or question1 == "un private":
                lenQuestionWord = len("question")
                questionWordIndex = message.find('question')+lenQuestionWord+1 # Plus one is to get rid of from the white space.
                searchQ = message[questionWordIndex:]
                url = "https://www.google.com.tr/search?q={}".format(searchQ)
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "These are the results I found."')
                os.chdir(calypsoLocation)
                webbrowser.open_new_tab(url)

            elif question1 == "y" or question1 == "yes" or question1 == "p" or question1 == "private":
                lenQuestionWord = len("question")
                questionWordIndex = message.find('question')+lenQuestionWord+1 # Plus one is to get rid of from the white space.
                searchQ = message[questionWordIndex:]
                url = "https://duckduckgo.com/?t=ffab&q={}".format(searchQ)
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "These are the results I found."')
                os.chdir(calypsoLocation)
                os.system('start firefox --private "{}"'.format(url))

        # This is the part that you create search feature.
        elif "search" in mymessage:
            lenSearchWord = len("search")
            searchWordIndex = message.find('search')+lenSearchWord+1 # Plus one is to get rid of from the white space.
            searchedForF = message[searchWordIndex:].strip()
            os.chdir(eSpeakContainer[0])
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
                        os.chdir(eSpeakContainer[0])
                        os.system('espeak -v+f2 "There is no such a file called {} in partition {}"'.format(searchedForF,question1.upper()))
                        os.chdir(calypsoLocation)
                        print(listofTargetPaths)

                    else:
                        os.chdir(eSpeakContainer[0])
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
                            os.chdir(eSpeakContainer[0])
                            os.system('espeak -v+f2 "Ok."')
                            os.chdir(calypsoLocation)

                        else:
                            indexNumofForF = int(question2)-1
                            os.startfile("{}\\{}".format(listofTargetPaths[indexNumofForF],searchedForF))

                else:
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "Sorry partition is not exists."')
                    os.chdir(calypsoLocation)
                    print("Partition {} is not exist".format(question1.upper()))

            elif question1 == "d" or question1 == "D":
                if os.path.exists("{}:\\".format(question1.upper())) == True:

                    for currentpath, dirnames, filenames in os.walk("{}:\\".format(question1.upper())):
                        if searchedForF in os.listdir(currentpath):
                            listofTargetPaths.append(currentpath)

                    if len(listofTargetPaths) == 0:
                        os.chdir(eSpeakContainer[0])
                        os.system('espeak -v+f2 "There is no such a file called {} in partition {}"'.format(searchedForF,question1.upper()))
                        os.chdir(calypsoLocation)
                        print(listofTargetPaths)

                    else:
                        os.chdir(eSpeakContainer[0])
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
                            os.chdir(eSpeakContainer[0])
                            os.system('espeak -v+f2 "Ok."')
                            os.chdir(calypsoLocation)

                        else:
                            indexNumofForF = int(question2)-1
                            os.startfile("{}\\{}".format(listofTargetPaths[indexNumofForF],searchedForF))

                else:
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "Sorry partition is not exists."')
                    os.chdir(calypsoLocation)
                    print("Partition {} is not exist".format(question1.upper()))

            elif question1 == "e" or question1 == "E":
                if os.path.exists("{}:\\".format(question1.upper())) == True:

                    for currentpath, dirnames, filenames in os.walk("{}:\\".format(question1.upper())):
                        if searchedForF in os.listdir(currentpath):
                            listofTargetPaths.append(currentpath)

                    if len(listofTargetPaths) == 0:
                        os.chdir(eSpeakContainer[0])
                        os.system('espeak -v+f2 "There is no such a file called {} in partition {}"'.format(searchedForF,question1.upper()))
                        os.chdir(calypsoLocation)
                        print(listofTargetPaths)

                    else:
                        os.chdir(eSpeakContainer[0])
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
                            os.chdir(eSpeakContainer[0])
                            os.system('espeak -v+f2 "Ok."')
                            os.chdir(calypsoLocation)

                        else:
                            indexNumofForF = int(question2)-1
                            os.startfile("{}\\{}".format(listofTargetPaths[indexNumofForF],searchedForF))

                else:
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "Sorry partition is not exists."')
                    os.chdir(calypsoLocation)
                    print("Partition {} is not exist".format(question1.upper()))

            elif question1 == "f" or question1 == "F":
                if os.path.exists("{}:\\".format(question1.upper())) == True:

                    for currentpath, dirnames, filenames in os.walk("{}:\\".format(question1.upper())):
                        if searchedForF in os.listdir(currentpath):
                            listofTargetPaths.append(currentpath)

                    if len(listofTargetPaths) == 0:
                        os.chdir(eSpeakContainer[0])
                        os.system('espeak -v+f2 "There is no such a file called {} in partition {}"'.format(searchedForF,question1.upper()))
                        os.chdir(calypsoLocation)
                        print(listofTargetPaths)

                    else:
                        os.chdir(eSpeakContainer[0])
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
                            os.chdir(eSpeakContainer[0])
                            os.system('espeak -v+f2 "Ok."')
                            os.chdir(calypsoLocation)

                        else:
                            indexNumofForF = int(question2)-1
                            os.startfile("{}\\{}".format(listofTargetPaths[indexNumofForF],searchedForF))

                else:
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "Sorry partition is not exists."')
                    os.chdir(calypsoLocation)
                    print("Partition {} is not exist".format(question1.upper()))

            elif "web" in question1 or "internet" in question1 or "Internet" in question1 or "Web" in question1:
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "Do you prefer private search or not?"')
                os.chdir(calypsoLocation)
                question1 = input("Enter your answer here(Private=Yes(y)/UnPrivate=No(n))? ")

                if question1 == "n" or question1 == "no" or question1 == "unp" or question1 == "unprivate" or question1 == "un private":
                    lenQuestionWord = len("search")
                    questionWordIndex = message.find('search')+lenQuestionWord+1 # Plus one is to get rid of from the white space.
                    searchQ = message[questionWordIndex:]
                    url = "https://www.google.com.tr/search?q={}".format(searchQ)
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "These are the results I found."')
                    os.chdir(calypsoLocation)
                    webbrowser.open_new_tab(url)

                elif question1 == "y" or question1 == "yes" or question1 == "p" or question1 == "private":
                    lenQuestionWord = len("search")
                    questionWordIndex = message.find('search')+lenQuestionWord+1 # Plus one is to get rid of from the white space.
                    searchQ = message[questionWordIndex:]
                    url = "https://duckduckgo.com/?t=ffab&q={}".format(searchQ)
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "These are the results I found."')
                    os.chdir(calypsoLocation)
                    os.system('start firefox --private "{}"'.format(url))

            else:
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "You entered an invalid value."')
                os.chdir(calypsoLocation)

        # This is the part that you add password generator feature.
        elif "password" in mymessage:
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Here is your password"')
            os.chdir(calypsoLocation)
            lcletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            ucletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", ",", ".", "<", ">", "/", "?", ";", ":"]

            rndmlclttrs = random.choices(lcletters, k=5)
            rndmuclttrs = random.choices(ucletters, k=5)
            rndmnmbrs = random.choices(numbers, k=5)
            rndmsymbls = random.choices(symbols, k=5)

            newlist = rndmlclttrs + rndmuclttrs + rndmnmbrs + rndmsymbls

            password = random.choices(newlist, k=20)

            def convert(password):
                new = ""

                for x in password:
                    new += x
                return new

            print("Password : ",convert(password))

        # This is the part that you created folder locker feature.
        elif "lock" in mymessage and "files" in mymessage or "lock" in mymessage or "folder" in mymessage:
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Select the folder that you want to encrypt."')
            os.chdir(calypsoLocation)
            root = tk.Tk()
            root.withdraw()

            file_path = filedialog.askdirectory()

            from_dir= file_path
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Enter a new name for new encrypted folder to be created."')
            os.chdir(calypsoLocation)
            fname=input('Enter folder name to be created: ')
            caracterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "!", "@", "#", "$", "%", "^", "&", "(", ")", "-", "_", "=", "+", ",", ";", "[", "]", "{", "}" ]
            caracterstring = ""
            for c in caracterlist:
                s = str(c)
                caracterstring += s + ", "

            os.chdir(eSpeakContainer[0])
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

            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Encryption is done you can find your encrypted folder in your desktop."')
            os.chdir(calypsoLocation)

        # This part is the part that you add task manager feature.
        elif "task manager" in mymessage or "tasks" in mymessage:
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "I\'m opening the task manager."')
            os.chdir(calypsoLocation)
            os.system("taskmgr")

        # This is the part that you create performance monitor feature.
        elif "performance" in mymessage:
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "I\'m opening the performance monitor."')
            os.chdir(calypsoLocation)
            os.system("perfmon.exe")

        # This is the part that you create scan and fix feature. !!You need to learn how to run it as administrator.
        elif "system" in mymessage and "check" in mymessage or mymessage == "system file check":
            os.chdir(eSpeakContainer[0])
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
            os.chdir(eSpeakContainer[0])
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

                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "This text includes {} words."'.format(nw))
                os.chdir(calypsoLocation)
                print("Number of words: ",nw)
                print()

        elif "do the thing" == mymessage or "do" in mymessage and "thing" in mymessage or "do" in mymessage and "the" in mymessage:
            dt_time_now = datetime.datetime.now()
            stringTimeP1 = dt_time_now.strftime("%H %M")
            stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "It\'s {} sir!"'.format(stringTimeP2))
            os.chdir(calypsoLocation)

        elif "what" in mymessage and "date" in mymessage:
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Where are you?"')
            os.chdir(calypsoLocation)
            question1 = input("Enter where you are?(Canada(C)/Turkey(T)/ComputerTime(Com) ")
            answer1 = question1.lower()
            if answer1 == "c":
                today = datetime.datetime.now(tz=pytz.timezone("Canada/Atlantic"))
                stringTodayP1 = today.strftime("%B %d %Y")
                stringTodayP2 = stringTodayP1.split(" ")[0] + " " + num2words(stringTodayP1.split(" ")[1]) + " " + num2words(stringTodayP1.split(" ")[2])
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "{}"'.format(stringTodayP2))
                os.chdir(calypsoLocation)
                print("Date: ",today.strftime('%b %d %Y'))
            elif answer1 == "t":
                today = datetime.datetime.now(tz=pytz.timezone("Turkey"))
                stringTodayP1 = today.strftime("%B %d %Y")
                stringTodayP2 = stringTodayP1.split(" ")[0] + " " + num2words(stringTodayP1.split(" ")[1]) + " " + num2words(stringTodayP1.split(" ")[2])
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "{}"'.format(stringTodayP2))
                os.chdir(calypsoLocation)
                print("Date: ",today.strftime('%b %d %Y'))
            elif answer1 == "com":
                today = datetime.datetime.now()
                stringTodayP1 = today.strftime("%B %d %Y")
                stringTodayP2 = stringTodayP1.split(" ")[0] + " " + num2words(stringTodayP1.split(" ")[1]) + " " + num2words(stringTodayP1.split(" ")[2])
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "{}"'.format(stringTodayP2))
                os.chdir(calypsoLocation)
                print("Date: ",today.strftime('%b %d %Y'))

        elif "what" in mymessage and "day" in mymessage:
            os.chdir(eSpeakContainer[0])
            os.system('espeak -v+f2 "Where are you?"')
            os.chdir(calypsoLocation)
            question1 = input("Enter where you are?(Canada(C)/Turkey(T)/ComputerTime(Com) ")
            answer1 = question1.lower()
            if answer1 == "c":
                todayDay = datetime.datetime.now(tz=pytz.timezone("Canada/Atlantic"))
                formattedDay = todayDay.strftime("%A")
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(formattedDay))
                os.chdir(calypsoLocation)
                print("Day: ",formattedDay)
            elif answer1 == "t":
                todayDay = datetime.datetime.now(tz=pytz.timezone("Turkey"))
                formattedDay = todayDay.strftime("%A")
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(formattedDay))
                os.chdir(calypsoLocation)
                print("Day: ",formattedDay)
            elif answer1 == "com":
                todayDay = datetime.datetime.now()
                formattedDay = todayDay.strftime("%A")
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(formattedDay))
                os.chdir(calypsoLocation)
                print("Day: ",formattedDay)


        elif "what" in mymessage and "time" in mymessage:
            os.chdir(eSpeakContainer[0])
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
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                os.chdir(calypsoLocation)

                print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                print()

            elif caseinsensetiveselection == "ca" or caseinsensetiveselection == "canada":
                os.chdir(eSpeakContainer[0])
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
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "central" or answer1 == "c":
                    dt_time_cad_central = datetime.datetime.now(tz=pytz.timezone("Canada/Central"))

                    stringTimeP1 = dt_time_cad_central.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "eastern" or answer1 == "e":
                    dt_time_cad_eastern = datetime.datetime.now(tz=pytz.timezone("Canada/Eastern"))

                    stringTimeP1 = dt_time_cad_eastern.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "mountain" or answer1 == "m":
                    dt_time_cad_mountain = datetime.datetime.now(tz=pytz.timezone("Canada/Mountain"))

                    stringTimeP1 = dt_time_cad_mountain.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "newfoundland" or answer1 == "nf" or answer1 == "new foundland" or answer1 =="nfl":
                    dt_time_cad_newfoundland = datetime.datetime.now(tz=pytz.timezone("Canada/Newfoundland"))

                    stringTimeP1 = dt_time_cad_newfoundland.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "pacific" or answer1 == "p":
                    dt_time_cad_pacific = datetime.datetime.now(tz=pytz.timezone("Canada/Pacific"))

                    stringTimeP1 = dt_time_cad_pacific.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "saskatchewan" or answer1 == "s":
                    dt_time_cad_saskatchewan = datetime.datetime.now(tz=pytz.timezone("Canada/Saskatchewan"))

                    stringTimeP1 = dt_time_cad_saskatchewan.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "yukon" or answer1 == "y":
                    dt_time_cad_yukon = datetime.datetime.now(tz=pytz.timezone("Canada/Yukon"))

                    stringTimeP1 = dt_time_cad_yukon.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                else:
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "Sorry I coudln\'t understand"')
                    os.chdir(calypsoLocation)


            elif caseinsensetiveselection == "bra" or caseinsensetiveselection == "brazil":
                os.chdir(eSpeakContainer[0])
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
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "denoronha" or answer1 == "d":
                    dt_time_braz_denoronha = datetime.datetime.now(tz=pytz.timezone("Brazil/DeNoronha"))

                    stringTimeP1 = dt_time_braz_denoronha.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "east" or answer1 == "e":
                    dt_time_braz_east = datetime.datetime.now(tz=pytz.timezone("Brazil/East"))

                    stringTimeP1 = dt_time_braz_east.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "west" or answer1 == "w":
                    dt_time_braz_west = datetime.datetime.now(tz=pytz.timezone("Brazil/West"))

                    stringTimeP1 = dt_time_braz_west.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                else:
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "Sorry I coudln\'t understand"')
                    os.chdir(calypsoLocation)


            elif caseinsensetiveselection == "rus" or caseinsensetiveselection == "russia":
                os.chdir(eSpeakContainer[0])
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
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "magadan" or answer1 == "m":
                    dt_time_rsy_magadan = datetime.datetime.now(tz=pytz.timezone("Asia/Magadan"))

                    stringTimeP1 = dt_time_rsy_magadan.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "sakhalin" or answer1 == "s":
                    dt_time_rsy_sakhalin = datetime.datetime.now(tz=pytz.timezone("Asia/Sakhalin"))

                    stringTimeP1 = dt_time_rsy_sakhalin.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "vladivostok" or answer1 == "v":
                    dt_time_rsy_vladivostok = datetime.datetime.now(tz=pytz.timezone("Asia/Vladivostok"))

                    stringTimeP1 = dt_time_rsy_vladivostok.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "yakutsk" or answer1 == "y":
                    dt_time_rsy_yakutsk = datetime.datetime.now(tz=pytz.timezone("Asia/Yakutsk"))

                    stringTimeP1 = dt_time_rsy_yakutsk.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "irkutsk" or answer1 == "i":
                    dt_time_rsy_irkutsk = datetime.datetime.now(tz=pytz.timezone("Asia/Irkutsk"))

                    stringTimeP1 = dt_time_rsy_irkutsk.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "novosibirsk" or answer1 == "n":
                    dt_time_rsy_novosibirsk = datetime.datetime.now(tz=pytz.timezone("Asia/Novosibirsk"))

                    stringTimeP1 = dt_time_rsy_novosibirsk.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "samara" or answer1 == "sam":
                    dt_time_rsy_samara = datetime.datetime.now(tz=pytz.timezone("Europe/Samara"))

                    stringTimeP1 = dt_time_rsy_samara.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                elif answer1 == "kaliningrad" or answer1 == "k":
                    dt_time_rsy_kaliningrad = datetime.datetime.now(tz=pytz.timezone("Europe/Kaliningrad"))

                    stringTimeP1 = dt_time_rsy_kaliningrad.strftime("%H %M")
                    stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                    os.chdir(calypsoLocation)

                    print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                    print()

                else:
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "Sorry I coudln\'t understand"')
                    os.chdir(calypsoLocation)



            elif caseinsensetiveselection == "ind" or caseinsensetiveselection == "india":
                dt_time_indi_antananarivo = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

                stringTimeP1 = dt_time_indi_antananarivo.strftime("%H %M")
                stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                os.chdir(calypsoLocation)

                print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                print()

            elif caseinsensetiveselection == "chi" or caseinsensetiveselection == "china":
                dt_time_chi_gmt8 = datetime.datetime.now(tz=pytz.timezone("Asia/Shanghai"))

                stringTimeP1 = dt_time_chi_gmt8.strftime("%H %M")
                stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                os.chdir(calypsoLocation)

                print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                print()

            elif caseinsensetiveselection == "sa" or caseinsensetiveselection == "south africa":
                dt_time_sa_gmt2 = datetime.datetime.now(tz=pytz.timezone("Africa/Johannesburg"))

                stringTimeP1 = dt_time_sa_gmt2.strftime("%H %M")
                stringTimeP2 = num2words(stringTimeP1.split(" ")[0]) + " " + num2words(stringTimeP1.split(" ")[1])
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "It\'s {}"'.format(stringTimeP2))
                os.chdir(calypsoLocation)

                print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                print()

            else:
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "Sorry I coudln\'t understand"')
                os.chdir(calypsoLocation)


        # Machine learning/Examine feature
        elif "examine" in mymessage:
            # Calypso's speach; it askes you to provide data base
            os.chdir(eSpeakContainer[0])
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

            os.chdir(eSpeakContainer[0])
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

            os.chdir(eSpeakContainer[0])
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
                        os.chdir(eSpeakContainer[0])
                        os.system('espeak -v+f2 "Thank you for entering values."')
                        os.chdir(calypsoLocation)

                    elif len(answers) != len(listOfCols)-1:
                        os.chdir(eSpeakContainer[0])
                        os.system('espeak -v+f2 "Enter a value for column {}."'.format(col))
                        os.chdir(calypsoLocation)
                        question = input(f'Enter a value for column {col}: ')
                        answers.append(question)

                # List of the values that are required to make predictions
                vRFPL = [float(q) for q in answers]
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "Here are the values that you entered."')
                os.chdir(calypsoLocation)
                print(f'List of the values that you entered: {vRFPL}')
                print()

                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "Here is your answer. Please check the dictionaries if you get confused."')
                os.chdir(calypsoLocation)
                cAnswer = dtree.predict(([vRFPL]))
                print(f'Intersted column: {interestCol}\nAnswer: {cAnswer}\n')

        elif "calculator" in mymessage or mymessage == "open calculator" or "open" in mymessage and "calculator" in mymessage:
            print("FEATURES")
            features = {
            "Simple Calculator": 1,
            "Mathematics of Business & Finance Calculator": 2,
            "Business Statistics Calculator": 3,
            }

            while True:
                print("FEATURES")
                for f in features:
                    print(f'{f}: {features[f]}')

                print()
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "Select a feature please."')
                os.chdir(calypsoLocation)
                feature = input("Enter your selection of feature: ")
                print()
                if feature == "exit":
                    break

                # This is the part for feature 1.
                elif feature == "1":
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "You select the simple calculator."')
                    os.chdir(calypsoLocation)
                    aritmetical_operators = {
                    "Multiply": "*",
                    "Division": "/",
                    "Addition": "+",
                    "Subtract": "-",
                    "Remainer": "%",
                    "Power": "^",
                    }

                    print("Aritmetical Operators")
                    for o in aritmetical_operators:
                        print(f'{o}: {aritmetical_operators[o]}')

                    print()

                    try:
                        n1 = Decimal(input("Enter your first number: "))
                        while True:
                            # Think about creating another try block here using name error and try to exit the loop exit string.
                            symbol = input("Enter your operator of choice: ")
                            try:
                                n2 = Decimal(input("Enter your number: "))
                                if symbol == aritmetical_operators["Multiply"]:
                                    n1 *= n2
                                    print("Result = ", n1)

                                elif symbol == aritmetical_operators["Division"]:
                                    n1 /= n2
                                    print("Result = ", n1)

                                elif symbol == aritmetical_operators["Addition"]:
                                    n1 += n2
                                    print("Result = ", n1)

                                elif symbol == aritmetical_operators["Subtract"]:
                                    n1 -= n2
                                    print("Result = ", n1)

                                elif symbol == aritmetical_operators["Remainer"]:
                                    n1 %= n2
                                    print("Result = ", n1)

                                elif symbol == aritmetical_operators["Power"]:
                                    n1 **= n2
                                    print("Result = ",n1)

                                else:
                                    print("""You didn't enter a valid symbol.
            Result = {}""".format(n1))

                            except:
                                print("""You didn't enter a valid number.
            Result = {}""".format(n1))

                    except:
                        print("You haven't entered a valid number.")

                # This is the part for feature 2.
                elif feature == "2":
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "You select the mathematics business and finance calculator. Here are the known topics."')
                    os.chdir(calypsoLocation)
                    topics = {
                    "Aritmetic Average": "AA",
                    "Weighted Average": "WA",
                    "Geometic Mean": "G",
                    "Portion": "P",
                    "Percentage Change": "PC",
                    "Pay for pay period": "PP",
                    "Hourly rate of pay": "HRP",
                    "Property tax": "PT",
                    "Property tax expressed as mill rate": "PTM",
                    "Index Number on Selected Date": "INSD",
                    "Inflation Rate": "IR",
                    "Real Income": "RI",
                    "Purchasing Power of a Dollar": "PPD",
                    "S&P/TSX Composite Index": "S&P/TSX-CI",
                    "Amount of trade discount": "ATD",
                    "Net price": "NP",
                    "Net price after a seris of discounts": "NPASD",
                    "Single equivalent discount rate": "SEDR",
                    "Amount Credited": "AC",
                    "Selling Price": "SP",
                    "Amount of Markup": "M",
                    "Selling Price2(using overhead expenses and operating profit)": "SP2",
                    "Rate of Markup on Cost": "RMC",
                    "Rate of Markup on Selling Price": "RMSP",
                    "Break Even Price": "BPRC",
                    "Reduced Selling Price": "RSP",
                    "Amount of Markdown": "AMD",
                    "Rate of Markdown": "RMD",
                    "Reduced Profit(using cost and overhead expenses)": "RP",
                    "Reduced Profit(using markdown)": "RP2",
                    "Net Amount of Markup": "NAM",
                    "Net Rate of Markup Based on Total Cost": "NRMBTC",
                    "Net Rate of Markup Based on Total Sales": "NRMBTS",
                    "Total Variable Costs": "TVC",
                    "Total Costs": "TC",
                    "Total Revenue": "TR",
                    "Net Income": "NI",
                    "At the break even point": "ABE",
                    "Contribution Margin per Unit": "CMPU",
                    "Contribution Ratio": "CR",
                    "Cost-Volume-Profit Analysis": "CVPA",
                    "Number of Units(Produced and sold)": "NU",
                    "Number of Units at the Break-Even Point": "NUBE",
                    "Contribution Margin Percent": "CMP",
                    "Net Income2": "NI2",
                    "Total Contribution Margin": "TMC",
                    "Interest": "I",
                    "Maturity Value": "MV",
                    "Principal": "Pir",
                    "Future Value": "FV",
                    "Amount of Compound Interest": "ACI",
                    "Periodic Interest Rate": "PIR",
                    "Number of Compounding Periods": "NCP",
                    "Nominal Interest Rate": "NIR",
                    "Periodic interest rate using future value and present value": "PIR2",
                    "Equivalent Periodic Interest Rate": "EPIR",
                    "Equivalent Nominal Interest Rate": "ENIR",
                    "Number of Compounding Periods": "NCP2",
                    "Time Period in Years": "TPY",
                    "Effective Interest Rate": "EIR",
                    "Future Value of an Ordinary Simple Annuity": "FVOSA",
                    "Present Value of an Ordinary Simple Annuity": "PVOSA",
                    "Number of Compounding Periods per Payment Period": "NCPPPP",
                    "Equivalent Periodic Interest Rate per Payment Period": "EPIRPP",
                    "Future Value of a Simple Annuity Due": "FVSAD",
                    "Present Value of a Simple Annuity Due": "PVSAD",
                    "Number of Payments, Given 'FV'": "NPGFV",
                    "Number of Payments, Given 'PV'": "NPGPV",
                    "Time Period (in years)": "TPY2",
                    "Number of Payments, Given 'FV­Due'": "NPGFVD",
                    "Number of Payments, Given 'PV­Due'": "NPGPVD",
                    }

                    print("TOPICS :")
                    for t in topics:
                        print(f'{t}: {topics[t]}')

                    print()

                    topic = input("Enter your topic here: ")
                    # This is the part that calculates aritetic average.

                    if topic == topics["Aritmetic Average"] or topic == topics["Aritmetic Average"].lower():
                        try:
                            print("""Formula:
        Aritmetic Average = Sum of all values of terms / Number of terms = (x1 + x2 + x3 + ... + xn)/n""")
                            nums = str(input("""
        Hint: Enter your numbers by putting ',' between them and no spacing.
        Enter your numbers here: """))
                            numl = nums.split(",")

                            def aritmetic_average_cal(nums,numl):
                                startpoint = Decimal(0)

                                def Adder(numl,startpoint):

                                    for n in numl:
                                        startpoint += Decimal(n)

                                    return startpoint

                                Aresult = Adder(numl,startpoint) / len(numl)
                                return Aresult

                            print(f'Result = {aritmetic_average_cal(nums,numl)}')


                        except:
                            print("You didn't entered a valid input. You should enter in the fallowing syntax: 5,6,7")


                    # This is the part that calculates weighted average.
                    elif topic == topics["Weighted Average"] or topic == topics["Weighted Average"].lower():
                        try:
                            print("""Formula:
        Weighted Average = Sum of all weighted values / Sum of the weighting values = (w1x1 + w2x2 + w3x3 + ... wnxn) / (w1 + w2 + w3) """)
                            nums = str(input("""
        Hint: Enter your numbers in right order by putting ',' between them and no spacing. Ex: 1,2,3
        Enter your numbers here: """))
                            wvals = str(input("""
        Hint: Enter your weight values in right order by putting ',' between them and no spacing. Ex: 1,2,3
        Enter your weight values: """))
                            def weighted_average_cal(nums,wvals):
                                numl = nums.split(",")
                                wvall = wvals.split(",")
                                numl1 = [ Decimal(n) for n in numl ]
                                wvall1 = [ Decimal(wv) for wv in wvall ]

                                for c in range(len(numl1)):
                                    numl1[c] = numl1[c] * wvall1[c] / sum(wvall1)

                                numl1 = sum(numl1)

                                return numl1

                            print(f'Result = {weighted_average_cal(nums,wvals)}')

                        except:
                            print(f'You didn\'entered a valid input. Ex: 1,2,3')


                    # This is the part that calculates geometric mean.
                    elif topic == topics["Geometic Mean"] or topic == topics["Geometic Mean"].lower():
                        try:
                            print("""Formula:
        Geometric Mean = (x1 * x2 * x3 * x4 * x5 * ... * xn)^(1/n)""")
                            nums = str(input("""
        Hint: Enter the numbers that you want to calculate their geometric mean by putting ',' between them no spacing. Ex: 1,2,3
        Enter your numbers: """))
                            def geometric_mean_cal(nums):
                                numl = nums.split(',')
                                numl1 = [ Decimal(item) for item in numl ]

                                def Multiplier(numl1):
                                    startpoint = 1

                                    for n in numl1:
                                        startpoint *= Decimal(n)

                                    return startpoint
                                Multiplier(numl1)

                                Gresult = Multiplier(numl1) ** (1/len(numl1))

                                return Gresult

                            print("Result = ", geometric_mean_cal(nums))


                        except:
                            print("You didn't entered valid value. Ex: 1,2,3")

                    # This is the part that calculates portion.
                    elif topic == topics["Portion"] or topic == topics["Portion"].lower():
                        try:
                            print("""Formula:
        Portion = Rate * Base""")
                            rate = Decimal(input("""Ex: 500
        Enter your rate(part) value here: """))
                            base = Decimal(input("""Ex: 1000
        Enter your base(whole) value here: """))

                            def portion_cal(rate,base):
                                portion = rate / base
                                return portion

                        except:
                            print("You didn't entered a valid value. Ex: 60")

                        print(f'Result = {portion_cal(rate,base)*100}%')

                    # This is the part that calculates percnetage change.
                    elif topic == topics["Percentage Change"] or topic == topics["Percentage Change"].lower():
                        try:
                            print("""Formula:
        Percentge change(%) = (Final Value - Initial Value) / Initial Value""")
                            finval = Decimal(input("""Ex: 170000
        Enter you final value here: """))
                            initval = Decimal(input("""Ex: 160000
        Enter you initial value here: """))
                            def percentage_change_cal(finval,initval):
                                percchange = (( finval - initval ) / initval ) * 100
                                return percchange

                            print(f'Result = {percentage_change_cal(finval,initval)}%')

                        except:
                            print("You didn't entered a valid value. Ex: 70")

                    # This is the part that calculates pay for pay period.
                    elif topic == topics["Pay for pay period"] or topic == topics["Pay for pay period"].lower():
                        try:
                            print("""Formula:
        Pay for pay period = Annual Salary / Number of pay periods per year""")
                            Annusall = Decimal(input("""Ex: 5000
        Enter your annual salary here: """))
                            Npp = Decimal(input("""Ex(Monthly Pay - Once a month): 12, Ex1(Semi-monthly Pay - Twice in a month): 24, Ex2(Bi-weekly Pay - Once in a 2 week): 26 Ex3(Weekly - Once a week): 52
        Enter your number of pay for pay period here: """))
                            def pay_for_pay_period_cal(Annusall, Npp):
                                Ppp = Annusall / Npp
                                return Ppp

                            print(f'Result = ${pay_for_pay_period_cal(Annusall,Npp)}')

                        except:
                            print("You didn't entered a valid value. Ex(Annual Sallary): 5000, Ex2(Pay Periods - Monthly): 12")

                    # This is the part that calculates Hourly rate.
                    elif topic == topics["Hourly rate of pay"] or topic == topics["Hourly rate of pay"].lower():
                        try:
                            print("""Formula:
        Hourly Rate of Pay = Weekly Pay / Number of working hours per week""")
                            wp = Decimal(input("""Ex: 800
        Enter your weekly pay here: """))
                            numberOfWorkingHour = Decimal(input("""Ex: 20
        Enter your number of work hours per week here: """))
                            def hourly_rate_of_pay_cal(wp,numberOfWorkingHour):
                                hourlyRateOfPay = wp / numberOfWorkingHour
                                return hourlyRateOfPay

                            print(f'Result = ${hourly_rate_of_pay_cal(wp,numberOfWorkingHour)}')

                        except:
                            print("You didn't entered valid value. Ex(Weekly Pay): 800, Ex1(Number of Working Hour): 20")

                    # This is the part that calculates property tax.
                    elif topic == topics["Property tax"] or topic == topics["Property tax"].lower():
                        try:
                            print("""Formula:
        Property Tax = Assessed value of property * Tax rate""")
                            avp = Decimal(input("""Ex: 500000
        Enter your assessed value of property: """))
                            tr = Decimal(input("""Hint: If your tax rate defined as percentage don't forget to enter it as decimal number.
        Ex: 90% = 0.9
        Enter your tax rate here: """))
                            def property_tax_cal(avp,tr):
                                pt = avp * tr
                                return pt

                            print(f'Result = ${property_tax_cal(avp,tr)}')

                        except:
                            print("You didn't entered valid value. Ex(Assessed Value of Property): 130000, Ex1(Tax Rate): 0.2")

                    # This is the part that calculates property tax expressed as mill rate.
                    elif topic == topics["Property tax expressed as mill rate"] or topic == topics["Property tax expressed as mill rate"].lower():
                        try:
                            print("""Formula:
        Property Tax = (Assessed value of property / 1000) * Mill Rate""")
                            avp = Decimal(input("""Ex: 120000
        Enter your assessed value of property here: """))
                            mr = Decimal(input("""Ex: 40
        Enter your mill rate here: """))
                            def property_tax_expressed_as_mill_cal(avp,mr):
                                ptm = ( avp / 1000 ) * mr
                                return ptm

                            print(f'Result = ${property_tax_expressed_as_mill_cal(avp,mr)}')

                        except:
                            print("You didn't entered valid value. Ex(Assesssed Value of Property): 100000, Ex1(Mill Rate): 40")

                    # This is the part that calculates index number on a selected date
                    elif topic == topics["Index Number on Selected Date"] or topic == topics["Index Number on Selected Date"].lower():
                        try:
                            visd = Decimal(input("""Ex: 350
        Enter the value of item on selected date here: """))
                            vibd = Decimal(input("""Ex: 500
        Enter the value of item on base date here: """))
                            insd = (visd / vibd)*100

                            print(f'Result = {insd}%')

                        except:
                            print("You didn't entered valid value. Ex(Value of item on seleted date) = 150, Ex1(Value of item on base date) = 130.5")

                    # This is the part that calculates Inflation Rate
                    elif topic == topics["Index Number on Selected Date"] or topic == topics["Index Number on Selected Date"].lower():
                        try:
                            cpiya = Decimal(input("""Ex: 126.5
        Enter your consumer price index year A(initial year/first year) here: """))
                            cpiyb = Decimal(input("""Ex: 130.8
        Enter your consumer price index year B(final year/second year) here: """))
                            ir = ( ( cpiyb - cpiya ) / cpiya ) * 100

                            print(f'Result = {ir}%')

                        except:
                            print("You didn't entered valid value. Ex(Consumer price index year A) = 125.5 , Ex1(Consumer price index year B) = 130.2")

                    # This is the part that calculates real income
                    elif topic == topics["Real Income"] or topic == topics["Real Income"].lower():
                        try:
                            mi = Decimal(input("""Ex: 600
            Enter your money income here: """))
                            cpi = Decimal(input("""Ex: 130
            Enter your consumer price index here: """))
                            ri = (mi / cpi) / 100

                            print(f'Result = ${ri}')

                        except:
                            print("You didn't entered valid value. Ex(Money income) = 150 , Ex1(Consumer price index) = 130.5")

                    # This is the part that calculates purchasing power of a dollar
                    elif topic == topics["Purchasing Power of a Dollar"] or topic == topics["Purchasing Power of a Dollar"].lower():
                        try:
                            cpi = Decimal(input("""Ex: 120
        Enter your consumer price index here: """))
                            ppd = ((1/cpi) * 100)*100

                            print(f'Result = {ppd}%')

                        except:
                            print("You didn't entered valid value. Ex(Consumer price index = 120.8)")

                    # This is the part that calculates S&P/TSX Composite Index
                    elif topic == topics["S&P/TSX Composite Index"] or topic == topics["S&P/TSX Composite Index"].lower():
                        try:
                            vpsd = Decimal(input("""Ex: 2829000.00
        Enter your value of portfolio on selected date here: """))
                            vpbd = Decimal(input("""Ex: 200000.00
        Enter your value of portfolio on base date here: """))
                            sandportsxci = (vpsd / vpbd) * 1000

                            print(f'Result = {sandportsxci}')

                        except:
                            print("You didn't entered valid value. Ex(Value of portfolio on selected date) = 2829000 , Ex1(Value of portfolio on base date) = 200000")

                    # This is the part that calculates amount of trade discount
                    elif topic == topics["Amount of trade discount"] or topic == topics["Amount of trade discount"].lower():
                        try:
                            print("""Formula:
        Amount of trade discount = Single discount rate * List pirce""")
                            lp = Decimal(input("""Ex: 1200
        Enter your list price here: """))
                            sdr = Decimal(input("""Ex: 0.02, 0.02 = 2%
        Enter your single discount rate expressed as decimal number here: """))
                            def amount_of_trade_discount_cal(sdr, lp):
                                atd = sdr * lp
                                return atd

                            print(f'Result = ${amount_of_trade_discount_cal(sdr, lp)}')

                        except:
                            print("You didn't entered valid value. Ex(List Price): 1200, Ex1(Single Discount Rate): 0.02")

                    # This is the part that calculates Net price.
                    elif topic == topics["Net price"] or topic == topics["Net price"].lower():
                        try:
                            print("""Formula:
        Net price = List price * (1 - Single Discount rate)""")
                            lp = Decimal(input("""Ex: 500
        Enter your list price here: """))
                            sdr = Decimal(input("""Ex: 0.03, 0.03 = 3%
        Enter your single discount rate here: """))
                            def net_price_cal(lp,sdr):
                                np = lp * ( 1 - sdr )
                                return np

                            print(f'Result = ${net_price_cal(lp,sdr)}')

                        except:
                            print("You didn't entered valid value. Ex(List Price): 500, Ex1(Single Discount Rate): 0.03")

                    #This is the part that calculates Net price after series of discounts.
                    elif topic == topics["Net price after a seris of discounts"] or topic == topics["Net price after a seris of discounts"].lower():
                        try:
                            print("""Notation:
        L = List Price
        d = Single Discount Rate

        Formula:
        Net price after a series of discounts = L * (1 - d1) * (1 - d2) * (1 - d3) * ... * (1 - dn)""")
                            lp = Decimal(input("Enter your list price here: "))
                            dsc = str(input("""
        Hint: Enter your discounts here by putting ',' between each other no spacing. If your discounts are described as percentage don't forget to enter it as decimal number (60% = 0.6)
        Ex: 0.02,0.1,0.0.05
        Enter your discounts here: """))
                            def net_price_after_series_of_discounts_cal(lp, dsc):
                                discl = dsc.split(',')
                                discl1 = [ Decimal(n) for n in discl ]


                                for c in range(len(discl1)):
                                    discl1[c] = ( 1 - discl1[c] )

                                startpoint = lp

                                for n in discl1:
                                    startpoint *= Decimal(n)

                                return startpoint

                            print(f'Result = ${net_price_after_series_of_discounts_cal(lp,dsc)}')

                        except:
                            print("You didn't entered valied value. Ex(List Price): 50, Ex1(Series of discount): 0.02,0.03,0.1")

                    # This ts the part that calculates single equivalent discount rate to a seres of dicounts.
                    elif topic == topics["Single equivalent discount rate"] or topic == topics["Single equivalent discount rate"].lower():
                        try:
                            print("""Notation:
        sd = Single Equivalent Discount Rate
        d = Discount Rate

        Formula:
        sd = 1 - [(1-d1) * (1-d2) * (1-d3) * ... * (1-dn)]""")
                            discs = str(input("""
        Hint: Enter your discounts here by putting ',' between each other, no spacing. If your discounts are described as percentage don't forget to enter it as decimal number(30% = 0.3)
        Ex: 0.6, 0.05, 0.1
        Enter your discounts here: """))
                            def single_equivalent_discount_rate_cal(discs):
                                discsl = discs.split(',')
                                discsl1 = [ Decimal(n) for n in discsl ]

                                for c in range(len(discsl1)):
                                    discsl1[c] = ( 1 - discsl1[c] )

                                startpoint = 1

                                def multiplier(startpoint, discsl1):

                                    for n in discsl1:
                                        startpoint *= Decimal(n)

                                    return startpoint

                                sedrR = 1 - multiplier(startpoint,discsl1)

                                return sedrR

                            print(f'Result = {single_equivalent_discount_rate_cal(discs)*100}%')


                        except:
                            print("You didn't entered valid value. Ex(Discount list): 0.05, 0.1, 0.2")

                    # This is the part that calculates Amount Credited
                    elif topic == topics["Amount Credited"] or topic == topics["Amount Credited"].lower():
                        try:
                            print("""Formula:
        Amount Credited = Amount Paid / ( 1 - Single discount rate )""")
                            ap = Decimal(input("""Ex: 1000
        Enter your ammound paid here: """))
                            sd = Decimal(input("""Hint: You should enter your single discount rate as decimal number(0.2 = 20%)
        Ex: 0.05
        Enter your single discount rate here: """))

                            Ac = ap / ( 1 - sd )
                            print(f'Result = ${Ac}')

                        except:
                            print("You didn't entered valid value. Ex(Amount Paid): 1000, Ex1(Single discount rate): 0.2")

                    # This is the part that calculates Selling price.
                    elif topic == topics["Selling Price"] or topic == topics["Selling Price"].lower():
                        try:
                            print("""Formula options:
        1) Selling Price1 = Cost + Markup
        2) Selling Price2 = Overhead expenses + Operating Profit""")
                            choice = input("""Ex: 1
        Enter your choice here( 1 = Selling price1 = Cost + Markup): """)
                            if choice == 1:
                                cst = Decimal(input("""Ex: 50
        Enter your cost here: """))
                                mrkup = Decimal(input("""Ex: 20
        Enter your markup here: """))
                                sp = cst + mrkup
                                print(f'Result = ${sp}')
                            elif choice == 2:
                                cst = Decimal(input("""Ex: 20
        Enter your cost here: """))
                                ohe = Decimal(input("""Ex: 50
        Enter your overhead expenses here: """))
                                op = Decimal(input("""Ex: 60
        Enter your operating profit here: """))
                                sp = cst + ohe + op
                                print(f'Result = ${sp}')

                        except:
                            print("You didn't entered valid value. Ex(Cost): 50, Ex2(Markup): 20")

                    # This is the part that calculates Amount of markup.
                    elif topic == topics["Amount of Markup"] or topic == topics["Amount of Markup"].lower():
                        try:
                            print("""Formula:
        Markup = Overhead Expenses + Operating Profit""")
                            ohe = Decimal(input("""Ex: 500
        Enter your overhead expenses here: """))
                            op = Decimal(input("""Ex: 200
        Enter your operating profit here: """))
                            mrkup = ohe + op
                            print(f'Result = ${mrkup}')
                        except:
                            print("You didn't entered valid value. Ex(Over head expenses) = 200 , Ex1(Operating Profit) = 400")

                    # This is the part that calculates Rate of Markup on Cost
                    elif topic == topics["Rate of Markup on Cost"] or topic == topics["Rate of Markup on Cost"].lower():
                        try:
                            print("""Formula: Rate of Markup on cost = (Markup/Cost) x 100 """)
                            mrkup = Decimal(input("""Ex:50
        Enter your markup amount here: """))
                            cst = Decimal(input("""Ex:60
        Enter your cost here: """))
                            rmc = ( mrkup / cst ) * 100
                            print(f'Result = {rmc}%')

                        except:
                            print('You didn\'t entered valid value. Ex(Markup): 45 , Ex1(Cost): 50')

                    # This is the part that calculates Rate of Markup on Selling Price
                    elif topic == topics["Rate of Markup on Selling Price"] or topic == topics["Rate of Markup on Selling Price"].lower():
                        try:
                            print("Formula: Rate of Markup on Sellings Price = (Markup/Selling Price) x 100 ")
                            mrkup = Decimal(input("Enter your markup amount here: "))
                            sp = Decimal(input("Enter your selling price here: "))
                            rmsp = ( mrkup / sp ) * 100
                            print(f'Result = {rmsp}%')

                        except:
                            print(f'You didn\'t entered valid value. Ex(Markup): , Ex1(Selling Price): ')

                    # This is the part that calculates break even price
                    elif topic == topics["Break Even Price"] or topic == topics["Break Even Price"].lower():
                        try:
                            print("""Formula: Break Even Price = Cost + Overhead Expenses""")
                            cst = Decimal(input("""Ex: 500
        Enter your cost here: """))
                            ohe = Decimal(input("""Ex: 300
        Enter your overhead expenses: """))
                            bprc = cst + ohe
                            print(f'Result = ${bprc}')

                        except:
                            print(f'You didn\'t entered valid value. Ex(Cost): 300 , Ex1(Overhead Expenses): 400')

                    # This is the part that calculates reduced selling price
                    elif topic == topics["Reduced Selling Price"] or topic == topics["Reduced Selling Price"].lower():
                        try:
                            print("Formula: Reduced Selling Price = Selling Price - Markdown")
                            sp = Decimal(input("""Ex: 60
        Enter your selling price here: """))
                            mrkdwn = Decimal(input("""Ex: 10
        Enter your markdown amount here: """))
                            rsp = sp - mrkdwn
                            print(f'Result = ${mrkdwn}')

                        except:
                            print(f'You didn\'t entered valid value. Ex(Selling Price): 70 , Ex1(Markdwon): 20')

                    # This is the part that calculates amount of markdown
                    elif topic == topics["Amount of Markdown"] or topic == topics["Amount of Markdown"].lower():
                        try:
                            print("Formula: Amount of Markdown = Selling Price - Reduced Selling Price")
                            sp = Decimal(input("""Ex: 70
        Enter your selling price here: """))
                            sred = Decimal(input("""Ex: 50
        Enter your redused selling price: """))
                            amd = sp - sred
                            print(f'Result = ${amd}')

                        except:
                            print(f'You didn\'t entered valid value. Ex(Selling Price): 70 , Ex1(Reduced Selling Price): 50')

                    # This is the part that calculates Rate of Markdown
                    elif topic == topics["Rate of Markdown"] or topic == topics["Rate of Markdown"].lower():
                        try:
                            print("Formula: Rate of Markdown = (Markdown/Selling Price) x 100")
                            mrkdown = Decimal(input("""Ex: 30
        Enter your amount of markdown here: """))
                            sp = Decimal(input("""Ex: 50
        Enter your amount of selling price here: """))
                            rmd = ( mrkdown / sp ) * 100
                            print(f'Result = {rmd}%')

                        except:
                            print(f'You didn\'t entered valid value. Ex(Markdown): 20 , Ex1(Selling Price): 50')

                    # This is the part that calculates Reduced profit
                    elif topic == "RP":
                        try:
                            print("Formula: Reduced Profit = Reduced Selling Price - Cost - Overhead expenses")
                            rsp = Decimal(input("Enter your reduced selling price or selling price here: "))
                            cst = Decimal(input("Enter your cost here: "))
                            ohe = Decimal(input("Enter your overhead expenses here: "))
                            rp = rsp - cst - ohe
                            print("Result = ",rp)

                        except:
                            print(f'You didn\'t entered valid value. Ex(Reduced Selling Price) = 70 , Ex1(Cost) = 50, Ex2(Overhead Expenses) = 10')

                    # THis is the part that calculates reduced profit using markdown
                    elif topic == "RP2":
                        try:
                            print("Formula: Reduced Profit = Operating Profit - Markdown")
                            op = Decimal(input("Enter your operating profit here: "))
                            mrkdown = Decimal(input("Enter your markdown amount here: "))
                            rp2 = op - mrkdown
                            print("Result = ",rp2)
                        except:
                            print("You didn't entered valid value. Ex(Operating Profit) = 500, Ex1(Markdown) = 30")

                    # This is the part that calculates Net Amount of Markup
                    elif topic == "NAM":
                        try:
                            print("Formula: Net Amount of Markup = Total Sales - Total Cost")
                            ts = Decimal(input("Enter your total sales here: "))
                            tc = Decimal(input("Enter your total costs here: "))
                            nam = ts - tc
                            print("Result = ", nam)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Total Sales): 500 , Ex1(Total Cost): 300')

                    # This is the part that calculates Net Rate of Markup Based on Total Cost
                    elif topic == "NRMBTC":
                        try:
                            print("Formula: Net Rate of Markup Based on Total Cost = (Net Amount of Markup / Total Cost) x 100")
                            nam = Decimal(input("Enter your net amount of markup here: "))
                            tc = Decimal(input("Enter your total cost here: "))
                            nrmbtc = ( nam / tc ) * 100
                            print("Result = ",nrmbtc,"%")
                        except:
                            print(f'You didn\'t entered valid value. Ex(Amount of Markup): 50 , Ex1(Total Cost): 200')


                    # This is the part that calculates Net Rate of Markup Based on Total Sales
                    elif topic == "NRMBTS":
                        try:
                            print("Formula: Net Rate of Markup Based on Total Sales = (Net Amount of Markup / Total Sales) x 100")
                            nam = Decimal(input("Enter your net amount of markup here: "))
                            ts = Decimal(input("Enter your total sales here: "))
                            nrmbts = ( nam / ts ) * 100
                            print("Result = ",nrmbts,"%")
                        except:
                            print(f'You didn\'t entered valid value. Ex(Net Amount of Markup): 20 , Ex1(Total Sales): 500')

                    # this is the part that calculates total variable cost.
                    elif topic == "TVC":
                        try:
                            print("Formula: Total Variable Cost = Variable Cost x Number of Units Produced and Sold")
                            vc = Decimal(input("Enter your variable cost per unit here: "))
                            x = Decimal(input("Enter your number of units produced and sold here: "))
                            tvc = vc * x
                            print("Result = ",tvc)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Cost Per Unit): 20 , Ex1(Number of Units Produced and Sold): 50')


                    # This is the part that calculates total costs
                    elif topic == "TC":
                        try:
                            print("Formula: Total Cost = Fixed Costs for a Specific Period + Total Variable Cost")
                            fc = Decimal(input("Enter your Fixed cost for a specific period here: "))
                            tvc = Decimal(input("Enter your total variable cost here: "))
                            tc = fc + tvc
                            print("Result = ",tc)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Fixed Cost for a Specific Period): 500 , Ex1(Total Variable Cost): 30')

                    # This is the part that calculates total revenues.
                    elif topic == "TR":
                        try:
                            print("Formula: Total Revenue = Selling Price Per Unit x Number of Units Produced and Sold")
                            s = Decimal(input("Enter your selling price here: "))
                            x = Decimal(input("Enter your number of units produced and sold here: "))
                            tr = s * x
                            print("Result = ",tr)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Selling Price): 70 , Ex1(Number of Units Produced and Sold): 1000')

                    # This is the part that calculates Net income.
                    elif topic == "NI":
                        try:
                            print("Formula: Net Income = Total Revenue - Total Cost")
                            tr = Decimal(input("Enter your total revenue here: "))
                            tc = Decimal(input("Enter your total costs here: "))
                            ni = tr - tc
                            print("Result = ",ni)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Total Revenue): 700 , Ex1(Total Costs): 500')

                    # This is the part that show what is the meaning of at the break even point
                    elif topic == "ABE":
                        print("At the break even point total revenue is equal to total cost. TR = TC !")

                    # This is the part that calculates contribution margin per unit.
                    elif topic == "CMPU":
                        try:
                            print("Formula: Contribution Margin = Selling Price Per Unit - Variable Cost Per Unit")
                            s = Decimal(input("Enter your selling price per unit here: "))
                            vc = Decimal(input("Enter your variable cost here: "))
                            cmpu = s - vc
                            pritn("Result = ",cmpu)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Selling Price Per Unit): 80 , Ex1(Variable Cost): 50')

                    # This is the part that calculates
                    elif topic == "CR":
                        try:
                            print("Formula: Contribution Ratio = (Contribution Margin(Per Unit)/Selling Price Per Unit) x 100")
                            cm = Decimal(input("Enter your contiribution margin here: "))
                            s = Decimal(input("Enter your selling price here: "))
                            cr = ( cm / s ) * 100
                            print("Result = ",cr,"%")
                        except:
                            print(f'You didn\'t entered valid value. Ex(Contribution Margin): 20 , Ex1(Selling Price): 50')

                    # This is the part show what is the meaning of cost volume profit analysis
                    elif topic == "CVPA":
                        try:
                            answr = str(input("""
        The formula for cost volume profit analysis: S * x  = FC + (VC + x) + NI
        What it means that is Total revenue = Total cost + Net income
        Do you know your Total cost and Net income? (y/n) """))
                            if answr == 'y':
                                try:
                                    tc = Decimal(input("Enter your total cost here: "))
                                    ni = Decimal(input("Enter your net income here: "))
                                    cvpa = tc + ni
                                    print("Result = ",cvpa)
                                except:
                                    print(f'You didn\'t entered valid value. Ex(Total Costs) = 200 , Ex1(Net Income) = 500')


                            elif answr == 'n':
                                try:
                                    fc = Decimal(input("Enter your fixed costs here: "))
                                    vc = Decimal(input("Enter your variable cost here: "))
                                    ni = Decimal(input("Enter your net income here: "))
                                    x = Decimal(input("Enter your number of units produced and sold: "))
                                    cvpa = fc + ( vc * x ) + ni
                                    print("Result = ",cvpa)
                                except:
                                    print(f'You didn\'t entered valid value. Ex(Fixed Costs) = 900, Ex1(Variable Cost) = 10, Ex2(Net Income) = 2000, Ex3(Number of Units Produced and Sold) = 90')

                        except:
                            print(f'You didn\'t entered valid value. Ex(Do you know your Total Cost and Net Income): y')


                    # This is the part that calculates Number of Units produced and sold.
                    elif topic == "NU":
                        try:
                            print("Formula: Number of Units Produced and Sold = (Fixed Costs For a Specific Period + Net Income)/(Selling Price - Variable Costs Per Unit)")
                            fc = Decimal(input("Enter your fixed cost here: "))
                            ni = Decimal(input("Enter your net income here: "))
                            s = Decimal(input("Enter your selling price here: "))
                            vc = Decimal(input("Enter you variable cost here: "))
                            nu = ( fc + ni ) / ( s - vc )
                            print("Result = ",nu)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Fixed Cost) = 200 , Ex1(Net Income) = 500, Ex2(Selling Price) = 30, Ex3(Variable Cost) = 10')

                    # This is the part that calcuates Number of Units at the Break-Even Point:
                    elif topic == "NUBE":
                        try:
                            print("Formula: Number of Units at The Break Even Point = Fixed Costs for a Specific Priod / Contribution Margin Per Unit")
                            fc = Decimal(input("Enter your fixed costs here: "))
                            cm = Decimal(input("Enter your contribution margin per unit here: "))
                            nube = fc / cm
                            print("Result = ",nube)

                        except:
                            print(f'You didn\'t entered valid value. Ex(Fixed Costs) = 300 , Ex1(Contribution Margin Per Unit) = 20')

                    # This is the part that calculates contribution margin percentage.
                    elif topic == "CMP":
                        try:
                            print("Formula: Contribution Margin Percent = ((Total Revenue - Total Variable Cost) / Total Revenue) * 100")
                            tr = Decimal(input("Enter your total revenues here: "))
                            tvc = Decimal(input("Enter yor total variable cost here: "))
                            cmp = ( ( tr - tvc ) / tr ) * 100
                            print("Result = ",cmp,"%")

                        except:
                            print(f'You didn\'t entered valid value. Ex(Fixed Costs) = 300 , Ex1(Contribution Margin Per Unit) = 20')


                    # This is the part that calculates net income 2
                    elif topic == "NI2":
                        try:
                            print("Formula: Net Income = (Contribution Margin Percent x Total Revenue) - Fixed Cost or Net Income = Total Contribution Margin - Fixed Costs")
                            question = str(input("Do you know your total contribution margin? (y/n): ")).lower().strip()
                            if question == "y":
                                try:
                                    tcm = Decimal(input("Enter your total contribution margin here: "))
                                    fc = Decimal(input("Enter your fixed costs here: "))
                                    ni = tcm - fc
                                    print(f'Result = {ni}$')
                                except:
                                    print(f'You didn\'t entered valid value. Ex(Total Contribution Margin) = 300 , Ex1(Fixed Costs) = 200')

                            elif question == "n":
                                try:
                                    cmp = Decimal(input("Enter your Contribution Margin Percent here: "))
                                    tr = Decimal(input("Enter your Total Revenue here: "))
                                    fc = Decimal(input("Enter your Fixed Cost here: "))
                                    ni = (cmp * tr) - fc
                                    print(f'Result = {ni}$')
                                except:
                                    print(f'You didn\'t entered valid value. Ex(Contribution Margin Percent) = 3, Ex1(Total Revenue) = 900, Ex2(Fixed Cost) = 200')

                        except:
                            print(f'Enter y or n')
                    # This is the part that calculates total contribution margin.
                    elif topic == "TCM":
                        try:
                            print("Formula: Total Contribution Margin = Net Income - Fixed Costs")
                            ni = Decimal(input("Enter your net income here: "))
                            fc = Decimal(input("Enter your fixed costs here: "))
                            tmc = ni + fc
                            print("Result = ",tmc)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Contribution Margin Percent) = 3, Ex1(Total Revenue) = 900, Ex2(Fixed Cost) = 200')

                    # This is the part that calculates the simple interest
                    elif topic == "I":
                        try:
                            print("Formula: Amount of Interest = Principal x Simple Interest Rate x Time Period")
                            p = Decimal(input("Enter your principal here: "))
                            r = Decimal(input("""Enter your simple interest rate as a decimal number
        ex: 70% = 0.7
        Enter your simple interest here: """))
                            t = Decimal(input("Enter your time period here: "))
                            i = p * r * t
                            print("Result = ",i)

                        except:
                            print(f'You didn\'t entered valid value. Ex(Principal) = 500, Ex1(Simple Interest Rate) = 0.02')

                    # This is the part that calculates maturity value.
                    elif topic == "MV":
                        try:
                            print("Formula: Maturity Value = Principal + Amount of Interest")
                            answr = str(input("Do you know your Amount of Interest? (y/n) "))
                            if answr == 'y':
                                try:
                                    p = Decimal(input("Enter your principal here: "))
                                    i = Decimal(input("Enter your amount of interest here: "))
                                    mv = p + i
                                    print("Result = ",mv)
                                except:
                                    print(f'You didn\'t entered valid value. Ex(Principal) = 500, Ex1(Amount of Interest) = 300')

                            elif answr == 'n':
                                try:
                                    p = Decimal(input("Enter your principal here: "))
                                    r = Decimal(input("""Enter your simple interest rate as decimal number.
        ex: 70% = 0.7
        Enter your simple interest rate here: """))
                                    t = Decimal(input("""Enter your time period.
        Hint: If it's 4 months then enter 4
        Ex: 4
        here: """))
                                    mv2 = p * ( 1 + r * t )
                                    print("Result = ",mv2)
                                except:
                                    print(f'You didn\'t entered valid value. Ex(Principal) = 500, Ex1(Simple Interest Rate as Decimal Number) = 0.02, Ex2(Time Period) 4')

                        except:
                            print(f'Enter y or n')

                    # This is the part that calculates principal.
                    elif topic == "Pir":
                        try:
                            print("Formula: Principal = Maturity Value / (1 + (Simple Interest Rate x Time Period)) or Principal = Maturity Value x (1 + (Simple Interest Rate x Time Period)^-1)")
                            s = Decimal(input("Enter your maturity value here: "))
                            r = Decimal(input("""Enter your simple interest as decimal number.
                ex: 70% = 0.7
                Enter your simple interest rate here: """))
                            t = Decimal(input("Enter your time period here: "))
                            pir = s / ( 1 + (r * t))
                            print("Result = ",pir)

                        except:
                            print(f'You didn\'t entered valid value. Ex(Maturity Value) = 200, Ex1(Simple Interest Rate as Decimal Number) = 0.02, Ex2(Time Period) 4')

                    # This is that part that calcuates future value
                    elif topic == "FV":
                        try:
                            print("Formula: Future Value = Present Value(1 + Periodic Rate of Interest)^Number of compounding periods during the term")
                            pv = Decimal(input("Enter your present value here: "))
                            i = Decimal(input("""Enter your periodic rate of interest as decimal number.
        Hint: 30% = 0.3 or 35% = 0.35
        Ex: 0.02
        Enter your periodic rate of interest here: """))
                            n = Decimal(input("Enter your number of compounding periods during the term here: "))
                            fv = pv * ( 1 + i ) ** n
                            print("Result = ",fv)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Maturity Value) = 200, Ex1(Simple Interest Rate as Decimal Number) = 0.02, Ex2(Time Period) 4')

                    # This is the part that calculates present value.
                    elif topic == "PV":
                        try:
                            print("Formula: Present Value = Future Value / (1 + Periodic rate of interest)^Number of compounding periods during the term or Present Value = Feature Value x (1 + Periodic Rate of Interest)^-Number of compounding periods during the term")
                            fv = Decimal(input("Enter your future value here: "))
                            i = Decimal(input("""Enter your periodic rate of interest i as decimal number.
        ex: 30% = 0.3 or 35% = 0.35
        Enter your periodic rate of interest here: """))
                            n = Decimal(input("Enter your number of compounding periods during the term here: "))
                            pv = fv / ( ( 1 + i ) ** n )
                            print("Result = ",pv)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Future Value) = 500, Ex1(Periodic Rate of Interest) = 0.02, Ex2(Number of compounding periods during the term) 3')

                    # This is the part that calculates Amount of Compound Interest
                    elif topic == "ACI":
                        try:
                            print("Formula: Amount of compound interst = Future Value - Present Value")
                            fv = Decimal(input("Enter your future value here: "))
                            pv = Decimal(input("Enter your present value here: "))
                            aci = fv - pv
                            print("Result = ",aci,"$")
                        except:
                            print(f'You didn\'t entered valid value. Ex(Future Value) = 200, Ex1(Present Value) = 100')

                    # This is the part that calculates Periodic Interest Rate
                    elif topic == "PIR":
                        try:
                            print("Formula: Periodic Interest Rate = Nominal Annual Interest Rate / Number of compouding periods per year")
                            j = Decimal(input("Enter your nominal (stated or quoted) annual interest rate here: "))
                            m = Decimal(input("Enter your number of compounding periods per year (compounding frequency): "))
                            pir = j / m
                            print("Result = ",pir)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Nominal Annual Interest Rate) = 0.018, Ex1(Number of compoounding periods periods per ear) = 0.02')

                    # This is the part that calculates number of compounding periods
                    elif topic == "NCP":
                        try:
                            print("Formula: Number of Compounding Periods = Number of compouding periods per year x Time period or terms in yars")
                            m = Decimal(input("Enter your number of compounding periods per year (compounding frequency) here: "))
                            t = Decimal(input("Enter your Time period or term in years here: "))
                            ncp = m * t
                            print("Result = ",ncp)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Number of compounding periods per year (compounding frequency)) = 2, Ex1(Time period or term in year) = 5\nHint: Compounding Frequency = ("Annually": 1, "Semi-annual": 2, "Quarterly": 4, "Monthly": 12, "Daily": 365,)')

                    # This is the part that calculates periodci interest rate using future value and present value.
                    elif topic == "PIR2":
                        try:
                            print("Formula: Periodic Interest Rate = (Future Value / Present Value)^(1/Number of compounding periods during the term) - 1")
                            fv = Decimal(input("Enter your future value here: "))
                            pv = Decimal(input("Enter your present value here: "))
                            n = Decimal(input("Enter your number of compounding periods during the term n here: "))
                            pir2 = ( ( fv / pv ) ** ( 1 / n ) - 1 )
                            print("Result = ",pir2)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Future Value) = 500, Ex1(Present Value) = 300, Ex2(Number of compounding periods per year (compounding frequency)) = 2\nHint: Compounding Frequency = ("Annually": 1, "Semi-annual": 2, "Quarterly": 4, "Monthly": 12, "Daily": 365,)')

                    # This is the part that calculates nominal interest rate
                    elif topic == "NIR":
                        try:
                            print("Formula: Nominal Interest Rate = Number of Compounding Periods Per Year(Compunding frequency) x Periodic Rate of Interest")
                            m = Decimal(input("Enter your Number of compounding periods per year (compounding frequency) m here: "))
                            i = Decimal(input("""Enter your periodic rate of interest i as decimal number.
        ex: 30% = 0.3 or 35% = 0.35
        Enter your periodic rate of interest here: """))
                            j = m * i
                            print("Result = ",j)

                        except:
                            print(f'You didn\'t entered valid value. Ex(Number of compounding periods per year (compounding frequency)) = 2, Ex1(Periodic Rate of Interest) = 0.02\nHint: Compounding Frequency = ("Annually": 1, "Semi-annual": 2, "Quarterly": 4, "Monthly": 12, "Daily": 365,)')

                        # This is the part that calculates Number of compounding periods.
                    elif topic == "NCP2":
                        try:
                            print("Formula: Number of Compounding Periods = ln(Future Value / Present Value) / ln(1 + Periodic Rate of Interest)")
                            fv = Decimal(input("Enter your future value FV here: "))
                            pv = Decimal(input("Enter your present value PV here: "))
                            i = Decimal(input("""Enter your periodic rate of interest i as decimal number.
        ex: 30% = 0.3 or 35% = 0.35
        Enter your periodic rate of interest here: """))
                            ncp2 = math.log( fv / pv ) / math.log( 1 + i )
                            print("Result = ",ncp2)

                        except:
                            print(f'You didn\'t entered valid value. Ex(Future Value) = 700, Ex1(Present Value) = 500, Ex2(Periodic Rate of Interest) = 0.019')

                    # This is the part that calculates time period in years.
                    elif topic == "TPY":
                        try:
                            print("Formula: Time Period in Years = Number of compounding periods during the term / Number of compounding periods per year(compounding frequency)")
                            n = Decimal(input("Enter your number of compounding periods during the term n here: "))
                            m = Decimal(input("Enter your Number of compounding periods per year (compounding frequency) m here: "))
                            tpy = n / m
                            print("Result = ",tpy)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Number of compounding periods during the term) = 55.872, Ex1(Number of compounding periods per year (compounding frequency)) = 12\nHint: Compounding Frequency = ("Annually": 1, "Semi-annual": 2, "Quarterly": 4, "Monthly": 12, "Daily": 365,)')

                    # This is the part that calculates Effective Interest Rate
                    elif topic == "EIR":
                        try:
                            print("Formula: Effective Interest Rate = (1 + Periodic Interest Rate)^Number of compounding periods per year - 1")
                            i = Decimal(input("""Enter your periodic rate of interest i as decimal number.
                            ex: 30% = 0.3 or 35% = 0.35
                            Enter your periodic rate of interest here:
                            """))
                            m = Decimal(input("Enter your Number of compounding periods per year (compounding frequency) m here: "))
                            eir = ( ( 1 + i ) ** m ) - 1
                            print("Result = ",eir)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Periodic Rate of Interest) = 0.02, Ex1(Number of compounding periods per year (compounding frequency)) = 12\nHint: Compounding Frequency = ("Annually": 1, "Semi-annual": 2, "Quarterly": 4, "Monthly": 12, "Daily": 365,)')

                    # This is the part that calculates equivalent periodic interest rate.
                    elif topic == "EPIR":
                        try:
                            print("Formula: Equivalent Periodic Interest Rate = (1 + Periodic Interest Rate1)^(Number of compounding periods per year (compounding frequency)1 / Number of compounding periods per year (compounding frequency)2) - 1")
                            i1 = Decimal(input("""Enter your periodic rate of interest i as decimal number.
        ex: 30% = 0.3 or 35% = 0.35
        Enter your periodic rate of interest here: """))
                            m1 = Decimal(input("Enter your m1 Number of compounding periods per year (compounding frequency) here: "))
                            m2 = Decimal(input("Enter your m2 Number of compounding periods per year (compounding frequency) here: "))
                            epir = ( ( 1 + i1 ) ** ( m1 / m2 ) ) - 1
                            print("Result = ",epir)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Periodic Rate of interest) = 0.02, Ex1(Number of compounding periods per year (compounding frequency)) = 2, Ex2(Number of compounding periods per year (compounding frequency)) = 4\nHint: Compounding Frequency = ("Annually": 1, "Semi-annual": 2, "Quarterly": 4, "Monthly": 12, "Daily": 365,)')

                    # This is the part that calculates Equivalent Nominal Interest Rate
                    elif topic == "ENIR":
                        try:
                            print("Formula: Equivalent Nominal Interest Rate = Number of compounding periods per year (compounding frequency)2 x Periodic Rate of Interest2 ")
                            m2 = Decimal(input("Enter your Number of compounding periods per year (compounding frequency) m2 here: "))
                            i = Decimal(input("""Enter your periodic rate of interest i as decimal number.
        Ex: 30% = 0.3 or 35% = 0.35
        Enter your periodic rate of interest here: """))
                            enir = m2 * i
                            print("Result = ",enir)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Number of compounding periods per year (compounding frequency)2) = 2, Ex1(Periodic Rate of interest) = 0.018\nHint: Compounding Frequency = ("Annually": 1, "Semi-annual": 2, "Quarterly": 4, "Monthly": 12, "Daily": 365,)')

                    # This is the part that calculates future values of an ordinary simple annity.
                    elif topic == "FVOSA":
                        try:
                            print("Formula: Future Value of an Ordinary Simple Annuity = Amount of periodic payment in an annuity x [((1 + Interest rate per compouding period)^Total Number of payments during the term of an annuity - 1) / Interest rate per compounding period]")
                            pmt = Decimal(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
                            i = Decimal(input("""Enter your Interest Rate per compounding period.
        Hint: 30% = 0.3 or 35% = 0.35
        Ex: 0.02
        Enter your interest rate per compounding period(periodic interest rate): """))
                            n = Decimal(input("Enter your Total number of payments during the term of an annuity(n) here: "))
                            fvosa = pmt * ( ( ( ( 1 + i ) ** n ) - 1 ) / i )
                            print("Result = ",fvosa)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Amount of periodic payment in an annuity(PMT)) = 500, Ex1(Interest rate per compounding period) = 0.018, Ex2(Total number of payments during the term of an annuity(n)) = 30')

                    # This is the part that calculates Present value of an ordinary simple annuity.
                    elif topic == "PVOSA":
                        try:
                            print("Formula: Present Value of an Ordinary Simple Annuity = Amount of periodic payment in an annuity x [(1-(1+Interest rate per compounding period)^-Total number of payments during the term of an annuity) / Interest rate per compounding period]")
                            pmt = Decimal(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
                            i = Decimal(input("""Enter your Interest Rate per compounding period i as decimal number.
        Hint: 30% = 0.3 or 35% = 0.35
        Enter your Interest Rate per compounding period here: """))
                            n = Decimal(input("Enter your Total number of payments during the term of an annuity(n) here: "))
                            pvosa = pmt * ( ( 1 - ( ( 1 + i ) ** ( 1 / n ) ) ) / i )
                            print("Result = ",pvosa)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Amount of periodic payment in an annuity(PMT)) = 500, Ex1(Interest rate per compounding period) = 0.018, Ex2(Total number of payments during the term of an annuity(n)) = 30')

                    # This is the part that calculates Number of Compounding Periods per Payment Period
                    elif topic == "NCPPPP":
                        try:
                            print("Formula: Number of Compounding Periods per Payment Period = Number of compounding periods per year / Number of payments per year")
                            ncppy = Decimal(input("Enter your number of compounding periods per year here: "))
                            npp = Decimal(input("Enter your number of payments per year here: "))
                            ncpppp = ncppy / npp
                            print("Result = ",ncpppp)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Number of compounding peridos per year) = 12, Ex1(Number of payments per year) = 12')

                    # This is the part that calculates equivalent periodic interest rate per paymet period.
                    elif topic == "EPIRPP":
                        try:
                            print("Formula: Equivalent periodic Interest Rate per Payment Period = ((1 + Interest rate per compounding period)^Number of compounding periods per payment period) - 1")
                            i = Decimal(input("""Enter your Interest Rate per compounding period i as decimal number.
        Hint: 30% = 0.3 or 35% = 0.35
        Ex: 0.012
        Enter your Interest Rate per compounding period here: """))
                            c = Decimal(input("Enter your number of compounding period per payment period (c) here: "))
                            epirpp = ( ( 1 + i ) ** c ) - 1
                            print("Result = ",epirpp)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Interest rate per compounding period) = 0.012, Ex1(Number of compounding period per payment period) = 2')

                    # This is the part that calcuates future value of a simple annuity due.
                    elif topic == "FVSAD":
                        try:
                            print("Formula: Future Value of a Simple Annuity Due = Amount of Periodic Payment in an Annuity x [((1 + Interest Rate per Compounding Period)^Number of Compounding Periods per payment period - 1) / Interest Rate per Compounding Period] x (1 + Interest Rate Per Compounding Period)")
                            pmt = Decimal(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
                            i = Decimal(input("""Enter your Interest Rate per compounding period i as decimal number.
        Hint: 30% = 0.3 or 35% = 0.35
        Enter your Interest Rate per compounding period here: """))
                            n = Decimal(input("Enter your Total number of payments during the term of an annuity(n) here: "))
                            fvsad = pmt * ( ( ( (1 + i ) ** n ) - 1 ) / i ) * ( 1 + i )
                            print("Result = ",fvsad)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Amount of periodic payment in an annuity(PMT)) = 300, Ex1(Interest Rate Per Compounding Period) = 2, Ex2(Total number of payments during the term of an annuity(n)) = 30')

                    # This is the part that calculates present value of a simple annuity due.
                    elif topic == "PVSAD":
                        try:
                            print("Formula: Present Value of a Simple Annuity Due = Amount of Periodic Payment in an Annuity x [((1 - Interest Rate Per Compounding Period)^-Total Number of Payments During the term of an annuity -1) / Interest Rate Per Compounding Period] x (1 + Intereest Rate Per Compounding Period)")
                            pmt = Decimal(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
                            i = Decimal(input("""Enter your Interest Rate per compounding period i as decimal number.
        Hint: 30% = 0.3 or 35% = 0.35
        Ex: 0.005
        Enter your Interest Rate per compounding period here: """))
                            n = Decimal(input("Enter your Total number of payments during the term of an annuity(n) here: "))
                            pvsad = pmt * ( ( 1 - ( (1 + i ) ** ( 1 / n ) ) ) / i ) * ( 1 + i )
                            print("Result = ",pvsad)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Amount of periodic payment in an annuity(PMT)) = 300, Ex1(Interest Rate Per Compounding Period) = 2, Ex2(Total number of payments during the term of an annuity(n)) = 30')

                    # This is the part that calcualates number of payments given future value.
                    elif topic == "NPGFV":
                        try:
                            print("Formula: Number of Payments, Given 'FV' = ln[1+((Interest Rate per Compounding Period x  Future value of an ordinary annuity) / (Amount of Periodic Payment in an Annuity))] / ln(1 + Interest Rate Per Compounding Period)")
                            fv = Decimal(input("Enter your Future value of an ordinary annuity here: "))
                            pmt = Decimal(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
                            i = Decimal(input("""Enter your Interest Rate per compounding period i as decimal number.
        Hint: 30% = 0.3 or 35% = 0.35
        Ex: 0.012
        Enter your Interest Rate per compounding period here: """))
                            npgfv = math.log( 1 + ( ( i * fv ) / pmt ) ) / math.log( 1 + i )
                            print("Result = ",npgfv)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Future value of an ordinary annuity) = 500, Ex1(Amount of periodic payment in an annuity(PMT)) = 2, Ex2(Total number of payments during the term of an annuity(n)) = 30')


                    # This is the part that calcuates number of periods Number of Payments, Given 'PV'. It's calculating 'n'.
                    elif topic == "NPGPV":
                        try:
                            print("Formula: Number of Payments, Given'PV' = ln[1-((Interest Rate per Compounding Period x Persent value of an ordinary annuity) / (Amount of periodc paymet in an annuity)] / ln(1 + Interst rate per compounding period)")
                            pv = Decimal(input("Enter your  Persent value of an ordinary annuity here: "))
                            pmt = Decimal(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
                            i = Decimal(input("""Enter your Interest Rate per compounding period i as decimal number.
        Hint: 30% = 0.3 or 35% = 0.35
        Ex: 0.012
        Enter your periodic rate of interest here: """))
                            npgpv =  -math.log( 1 - ( ( i * pv ) / pmt ) ) / math.log( 1 + i )
                            print("Result = ",npgpv)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Present value of an ordinary annuity) = 500, Ex1(Amount of periodic payment in an annuity(PMT)) = 2, Ex2(Total number of payments during the term of an annuity(n)) = 30')

                    # This is the part that calcaulates time period in years.
                    elif topic == "TPY2":
                        try:
                            print("Formula: Time Period in Years = Number of compounding periods per payment period  / Number of payments per year")
                            n = Decimal(input("Enter your Total number of payments during the term of an annuity(n) here: "))
                            nppy = Decimal(input("Enter your Number of payments per year here: "))
                            tpy2 = n / nppy
                            print("Result = ",tpy2)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Total number of payments during the term of an annuity(n)) = 3, Ex1(Number of payments per year) = 9')

                    # This is the part that calculates number of payments given FV due.
                    elif topic == 'NPGFVD':
                        try:
                            print("Formula: Number of Payments, Given 'FVDue' = ln[1+((Interest Rate per Compounding Period x Present Value of an annuity due) / (Amount of periodic payment in an annuity x (1 + Interest Rate Per Compounding Period)))] / ln(1 + Interest Rate Per Compounding Period)")
                            print("I'm couldn't calculate this one I'm sory python can't calculate negative ln. But I can always provide the formula for the people ask for.")
                            fv = Decimal(input("Enter your Future Vale of an Annuity due here: "))
                            pmt = Decimal(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
                            i = Decimal(input("""Enter your Interest Rate Per Compounding Period i as decimal number.
        Hint: 30% = 0.3 or 35% = 0.35
        Ex: 0.012
        Enter your periodic rate of interest here: """))
                            npgfvd = math.log( 1 + ( ( i * fv ) / ( pmt * ( 1 + i ) ) ) ) / math.log( 1 + i )
                            print("Result = ",npgfvd)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Future Value of an Annuity due) = 700, Ex1(Amount of periodic payment in an annuity(PMT)) = 100, Ex2(Interest Rate Per Compounding Period) = 0.018')

                    # This is the part that calculates Number of Payments, Given ‘PV­Due ' it's calculating 'n'.
                    elif topic == "NPGPVD":
                        try:
                            print("Formula: ln[1-((Interest Rate per Compounding Period x Present Value of an annuity due) / (Amount of periodic payment in an annuity x (1 + Interest Rate Per Compounding Period)))] / ln(1+ Interest Rate Per Compounding Period)")
                            pv = Decimal(input("Enter your Present Value of an annuity due here: "))
                            pmt = Decimal(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
                            i = Decimal(input("""Enter your Interest Rate Per Compounding Period i as decimal number.
        Hint: 30% = 0.3 or 35% = 0.35
        Ex: 0.012
        Enter your Interest Rate Per Compounding Period here: """))
                            npgpvd = -math.log( 1 - ( ( i * pv ) / ( pmt * ( 1 + i ) ) ) ) / math.log( 1 + i )
                            print("Result = ", npgpvd)
                        except:
                            print(f'You didn\'t entered valid value. Ex(Present Value of an annuity due) = 700, Ex1(Amount of periodic payment in an annuity(PMT)) = 100, Ex2(Interest Rate Per Compounding Period) = 0.018')

                    else:
                        print("You didn't entered valid topic. Try to enter a valid topic code.")

                # This is the part for feature 3.
                elif feature == "3":
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "You select the business statistics calculator. This feature is still under development."')
                    os.chdir(calypsoLocation)
                    print("Under development.")

                # This else statement does his job if there is no value error in feature input so there are 3 features for example if you enter 5 this else statment will do it's job but if you enter b it will except the value error and except statement will do its job.
                else:
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "You didn\'t entered valied feature."')
                    os.chdir(calypsoLocation)
                    print("You didn't entered valied feature.")
                    print()

        elif "french" in mymessage and "translator" in mymessage or "french translator" in mymessage or mymessage == "english-french translator":
            # Left side for English right side for French
            # In the lists feminine is first masculine is second.
            frenchGlossary = {
            "administration": "administration",
            "advance": "avance",
            "am": "ai",
            "and": "et",
            "august": "août",
            "be": "être",
            "business": "enterprise",
            "by": "par",
            "call": "appelez",
            "calisthenics": "gymnastique suédoise",
            "diploma": "diplôme",
            "end": "finir",
            "from": "de",
            "graduating": "graduation",
            "i": "je",
            "in": "au",
            "is": "est",
            "i'm": "j'ai",
            "life": "vie",
            "like": "aimer",
            "marketing": "commercialisation",
            "me": "moi",
            "my": ["ma", "mon"],
            "m'appelez": "call me",
            "name": "nom",
            "of": "en",
            "old": ["vieille", "vieux"],
            "program": "programme",
            "programming": "programmation",
            "school": "l'école",
            "schools": "écoles",
            "started": "a débuté",
            "studying": "en train d'étudier",
            "to": "a",
            "the": ["la", "le"],
            "this": ["cette", "ce"],
            "usually": "d'habitude",
            "wake": "réveiller",
            "will": "sera",
            "with": "avec",
            "years": ["années", "ans"],
            }

            while True:
                os.chdir(eSpeakContainer[0])
                os.system('espeak -v+f2 "Enter your sentence."')
                os.chdir(calypsoLocation)
                mymessage = str(input("Enter your sentence here: "))
                message = mymessage.lower().strip()
                if mymessage == "exit" or mymessage == "":
                    break

                else:
                    frenchTranslator = message.split(" ")

                    list = [ str(l) for l in frenchTranslator ]

                    newList = []

                    for w in list:
                        if "." in w:
                            index = w.find(".")
                            w = w[:index]
                        if "," in w:
                            index = w.find(",")
                            w = w[:index]
                        if ":" in w:
                            index = w.find(":")
                            w = w[:index]
                        if ";" in w:
                            index = w.find(";")
                            w = w[:index]
                        if "!" in w:
                            index = w.find("!")
                            w = w[:index]
                        if "?" in w:
                            index = w.find("?")
                            w = w[:index]

                        newList.append(w)

                    frenchTranslator = newList

                    frenchText = ""

                    for w in frenchTranslator:
                        if w in frenchGlossary:
                            frenchText += f'{frenchGlossary[w]} '

                        elif w not in frenchGlossary:
                            frenchText += f'{w.capitalize()} '

                    print(frenchText)
                    os.chdir(eSpeakContainer[0])
                    os.system(f'espeak -vfr+f2 "{frenchText}"')
                    os.chdir(calypsoLocation)

        elif "download audio" in mymessage or "download music" in mymessage or "download" in mymessage and "audio" in mymessage or "download" in mymessage and "music" in mymessage:
            while True:
                try:
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "Enter the youtube url here."')
                    os.chdir(calypsoLocation)
                    url = input("Enter the youtube url here: ")

                    if url == "exit":
                        break

                    else:
                        yt = YouTube(f'{url}')

                        # extract only audio
                        video = yt.streams.filter(only_audio=True).first()
                        destFAudios = f'{os.getcwd()}\\downloaded_musics'

                        if os.path.exists(destFAudios):
                            os.chdir(eSpeakContainer[0])
                            os.system('espeak -v+f2 "Musics will be downloaded to downloaded_musics folder."')
                            os.chdir(calypsoLocation)
                            print("Musics will be downloaded to downloaded_musics folder.")
                        else:
                            os.mkdir(f'{os.getcwd()}\\downloaded_musics')

                        # download the file
                        out_file = video.download(output_path=destFAudios)

                        # save the file
                        base, ext = os.path.splitext(out_file)
                        new_file = base + '.mp3'
                        os.rename(out_file, new_file)

                        # result of success
                        print(yt.title + " has been successfully downloaded.")

                except:
                    print("You didn't entered a valid value. You should be entering a url as fallows: https://www.youtube.com/watch?v=htrxWYQayk0")

        elif "download video" in mymessage or "download" in mymessage and "video" in mymessage:
            while True:
                try:
                    os.chdir(eSpeakContainer[0])
                    os.system('espeak -v+f2 "Enter you the url here."')
                    os.chdir(calypsoLocation)
                    url = input("Enter you the url here: ")

                    if url == "exit":
                        break

                    else:
                        yt = YouTube(f'{url}')
                        destFVideos = f'{os.getcwd()}\\downloaded_videos'

                        if os.path.exists(destFVideos):
                            os.chdir(eSpeakContainer[0])
                            os.system('espeak -v+f2 "Videos will be downloaded to downloaded_videos folder."')
                            os.chdir(calypsoLocation)
                            print("Videos will be downloaded to downloaded_videos folder.")
                        else:
                            os.mkdir(f'{os.getcwd()}\\downloaded_videos')

                        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(destFVideos)
                        print(yt.title + " has been successfully downloaded.")

                except:
                    print("You didn't entered a valid value. You should be entering a url as fallows: https://www.youtube.com/watch?v=htrxWYQayk0")

        # This is the part that Calipso doesn't understand what you are saying.
        else:
            os.chdir(eSpeakContainer[0])
            os.system(f'espeak -v+f2 "Here are the results that I found for {mymessage}."')
            os.chdir(calypsoLocation)
            lenQuestionWord = len("question")
            questionWordIndex = message.find('question')+lenQuestionWord+1 # Plus one is to get rid of from the white space.
            searchQ = message[questionWordIndex:]
            url = "https://www.google.com.tr/search?q={}".format(searchQ)
            webbrowser.open_new_tab(url)
