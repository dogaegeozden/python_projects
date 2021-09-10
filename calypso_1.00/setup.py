#Copyright © 2021 All rights reserved. Doga Ege Ozden

import os
import getpass

# OPTION 1: You can use bin folder and settings files to control calypso
# This is start up settings. So, if you want calypso to start on boot you should see bootsettings file.
startUpSetting = None
sString = "Start Calypso at every computer start up = "
lStrring = "Location to start Calypso on every start up = "
sStatuCheck = False
allFileNames = []

with open("bin\\bootsettings.txt", "r") as bSF:
    for ln in bSF:
        if sString in ln:
            sIndex = ln.find(sString)+len(sString)

            if "Yes" in ln[sIndex:] or "yes" in ln[sIndex:] or ln[sIndex:sIndex+3] == "Yes" or ln[sIndex:] == "yes":
                sStatuCheck = True
            else:
                sStatuCheck = False

with open("bin\\bootsettings.txt", "r") as bSF:
    if sStatuCheck == True:
        for lin in bSF:
            if lStrring in lin:
                lIndex = lin.find(lStrring)+len(lStrring)
                startUpSetting = lin[lIndex:lin.find(lin[-1])]
    else:
        startUpSetting = os.getcwd()

calypsoLocation = startUpSetting

# This is the part that you installed required packages
os.system(f'pip freeze > {calypsoLocation}\\system_installations_check.txt')

rPackages = []

with open(f'{calypsoLocation}\\requirements.txt', "r") as a:
    for line in a:
        pac = line
        rPackages.append(pac[:-1])

with open(f'{calypsoLocation}\\system_installations_check.txt', "r") as b:
    b_contents = b.read()

for i in range(len(rPackages)):
    if b_contents.find(rPackages[i]) != -1: # This means if it contains
        print("Required package is installed.")

    elif b_contents.find(rPackages[i]) == -1:
        print("Required package is not installed. Installing...")
        os.system(f'python -m pip install {rPackages[i]}')

# These are the variables required for espeak package control
eSpeakContainer = []
eSpeakFN = "espeak.exe" # This variable is for identifying, if espeak is installed on the device.
eSpeakStp = "setup_espeak-1.48.04.exe"

# These are the variables required for graphviz package control
graphVizContainer = []
gVIFN = "Uninstall.exe" # This variable is for identifying, if graphviz is installed on the device.
gVStp = "stable_windows_10_cmake_Release_x64_graphviz-install-2.48.0-win64.exe"
allFileNames = []

# DEVELOPMENT OPTIONS
# OPTION 1 YOU CAN SET THE SPEECH PACKAGE TO AN RELATIVE PATH TO MAKE IT START FASTER.
# eSpeakContainer.append(calypsoLocation + "\\" + "eSpeak(location)\\eSpeak\\command_line")

# OPTION 2 THIS IS THE PART THAT CALYPSO FIND IT'S OWN SPEECH PACKAGE
# This is the path that Calypso installs it's own speeh package
for path, dirname, filename in os.walk(calypsoLocation):
    for file in os.listdir(path):
        allFileNames.append(file)

    # This is the part that Calypso finds it's own speech package
    if eSpeakFN in os.listdir(path):
        eSpeakFP = path
        eSpeakContainer.append(eSpeakFP)

    if gVIFN in os.listdir(path):
        gVFP = path
        graphVizContainer.append(graphVizContainer)


if eSpeakFN in allFileNames:
    print("Speech package is installed on this device.")

else:
    print("Install the espeak to it's location. Refer to the docs to learn it's location.")
    for path, dirname, filename in os.walk(calypsoLocation):
        if eSpeakStp in os.listdir(path):
            eSpeakStpP = path
            os.chdir(eSpeakStpP)
            os.startfile(eSpeakStp)
            os.chdir(calypsoLocation)

if gVIFN in allFileNames:
    print("Graphviz is installed on this device.")

else:
    print("Install the graphviz to it's location. Refer to the docs to learn it's location.")
    for path, dirname, filename in os.walk(calypsoLocation):
        if gVStp in os.listdir(path):
            gVStpP = path
            os.chdir(gVStpP)
            os.startfile(gVStp)
            os.chdir(calypsoLocation)

cLSV = f'    calypsoLocation = "{startUpSetting}"\n'

calypsoPy = open("calypso.py", "r")
list_of_lines = calypsoPy.readlines()
listOfWantedLines = []

for line in list_of_lines:
    if "calypsoLocation" in line:
        listOfWantedLines.append(line)

# print(listOfWantedLines[0])

index = list_of_lines.index(listOfWantedLines[0])
list_of_lines[index] = cLSV

calypsoPy = open("calypso.py", "w")
calypsoPy.writelines(list_of_lines)
calypsoPy.close()
