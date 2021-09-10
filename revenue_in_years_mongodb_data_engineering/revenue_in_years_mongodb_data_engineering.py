#Copyright © 2021 All rights reserved. Doga Ege Ozden
#Note: If you have 2 users that has access to database userNameD = <username> if you have only 1 usernameD = userName 

import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal
import pymongo

# Required User Inputs for database connection.
userName = input("Enter your user name\nEx:myadminuser \nhere: ")
passwd = input("Enter your password\nEx:12345 \nhere: ")
dB = input("Enter your database name\nEx:mydatabase \nhere: ")
cS = input("Enter your connection string\nEx:mongodb+srv://test:<password>@learningmongopython.rtucf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority \nhere: ")
cN = input("Enter your column name\nEx:sales \nhere: ")


# Default Variables in Connection String. Hint you should chance these.
userNameD = userName
passwdD = "<password>"
dBD = "myFirstDatabase"

# Conection string organization
un1 = cS.find(userNameD)
un2 = cS.find(userNameD)+len(userNameD)

p1 = cS.find(passwdD)
p2 = cS.find(passwdD)+len(passwdD)

d1 = cS.find(dBD)
d2 = cS.find(dBD)+len(dBD)

cS = cS[:un1]+userName+cS[un2:p1]+passwd+cS[p2:d1]+dB+cS[d2:]

print(cS)

# Database Connection
myclient = pymongo.MongoClient(cS)

# Database querying
print(myclient.list_database_names())
mydb = myclient[dB]
mycol = mydb[cN]

tSPY = []
years = []

ts_2010 = 0
ts_2011 = 0
ts_2012 = 0
ts_2013 = 0
ts_2014 = 0
ts_2015 = 0
ts_2016 = 0
ts_2017 = 0
ts_2018 = 0
ts_2019 = 0
ts_2020 = 0
ts_2021 = 0

for s in mycol.find({},{ "_id": 1, "item_name": 1, "value": 1, "time":1 }):
    if s["time"].find("2010") != -1:
        ts_2010 += s["value"]
    elif s["time"].find("2011") != -1:
        ts_2011 += s["value"]
    elif s["time"].find("2012") != -1:
        ts_2012 += s["value"]
    elif s["time"].find("2013") != -1:
        ts_2013 += s["value"]
    elif s["time"].find("2014") != -1:
        ts_2014 += s["value"]
    elif s["time"].find("2015") != -1:
        ts_2015 += s["value"]
    elif s["time"].find("2016") != -1:
        ts_2016 += s["value"]
    elif s["time"].find("2017") != -1:
        ts_2017 += s["value"]
    elif s["time"].find("2018") != -1:
        ts_2018 += s["value"]
    elif s["time"].find("2019") != -1:
        ts_2019 += s["value"]
    elif s["time"].find("2020") != -1:
        ts_2020 += s["value"]
    elif s["time"].find("2021") != -1:
        ts_2021 += s["value"]

tSPY.append(ts_2010)
tSPY.append(ts_2011)
tSPY.append(ts_2012)
tSPY.append(ts_2013)
tSPY.append(ts_2014)
tSPY.append(ts_2015)
tSPY.append(ts_2016)
tSPY.append(ts_2017)
tSPY.append(ts_2018)
tSPY.append(ts_2019)
tSPY.append(ts_2020)
tSPY.append(ts_2021)

for y in range(2010,2022):
    years.append(y)

print(tSPY)
print(years)

plt.title("Revenue")
plt.xlabel("Years")
plt.ylabel("Total Sales")

plt.plot(years, tSPY)

plt.grid()

plt.show()
