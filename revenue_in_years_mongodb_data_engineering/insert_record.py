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

# Database querying
print(myclient.list_database_names())
mylist = []

# YEAR 2010
# book
for i in range(1, 300): # 300 book sold
    record = {"_id": i, "item_name": "book", "value": 15, "time": "2010-05-5"}
    mylist.append(record)

# head phones
for a in range(300, 500): # 200 headphones sold
    record = {"_id": a, "item_name": "head_phones", "value": 25, "time": "2010-06-5"}
    mylist.append(record)

# blue light glasses
for b in range(500, 750): #250 head phones sold
    record = {"_id": b, "item_name": "blue_light_glasses", "value": 50, "time": "2010-06-5"}
    mylist.append(record)

# YEAR 2011
# book
for i in range(750,1100): # 350 book sold
    record = {"_id": i, "item_name": "book", "value": 15, "time": "2011-02-5"}
    mylist.append(record)

# head phones
for a in range(1100, 1300): # 200 headphones sold
    record = {"_id": a, "item_name": "head_phones", "value": 25, "time": "2011-03-5"}
    mylist.append(record)

# blue light glasses
for b in range(1300, 1600): # 300 headphones sold
    record = {"_id": b, "item_name": "blue_light_glasses", "value": 50, "time": "2011-05-5"}
    mylist.append(record)

# YEAR 2012
# book
for i in range(1600,1800): # 200 book sold
    record = {"_id": i, "item_name": "book", "value": 15, "time": "2012-05-5"}
    mylist.append(record)

# head phones
for a in range(1800, 1900): # 100 headphones sold
    record = {"_id": a, "item_name": "head_phones", "value": 25, "time": "2012-04-5"}
    mylist.append(record)

# blue light glasses
for b in range(1900, 2000): # 100 headphones sold
    record = {"_id": b, "item_name": "blue_light_glasses", "value": 50, "time": "2012-09-5"}
    mylist.append(record)

# YEAR 2013
# book
for i in range(2000, 2300): # 300 booksold
    record = {"_id": i, "item_name": "book", "value": 15, "time": "2013-05-5"}
    mylist.append(record)

# head phones
for a in range(2300, 2800): # 500 books sold
    record = {"_id": a, "item_name": "head_phones", "value": 25, "time": "2013-05-5"}
    mylist.append(record)

# blue light glasses
for b in range(2800, 3150): # 350 books sold
    record = {"_id": b, "item_name": "blue_light_glasses", "value": 50, "time": "2013-05-5"}
    mylist.append(record)

# YEAR 2014
# book
for i in range(3150, 3300): # 150 books sold
    record = {"_id": i, "item_name": "book", "value": 15, "time": "2014-05-5"}
    mylist.append(record)

# head phones
for a in range(3300, 4000): # 700 head phones sold
    record = {"_id": a, "item_name": "head_phones", "value": 25, "time": "2014-05-5"}
    mylist.append(record)

# blue light glasses
for b in range(4000, 4550): # 550 blue light glasses sold.
    record = {"_id": b, "item_name": "blue_light_glasses", "value": 50, "time": "2014-05-5"}
    mylist.append(record)

# YEAR 2015
# book
for i in range(4550,4700): # 150 books sold
    record = {"_id": i, "item_name": "book", "value": 15, "time": "2015-05-5"}
    mylist.append(record)

# head phones
for a in range(4700, 4800): # 100 head phones sold
    record = {"_id": a, "item_name": "head_phones", "value": 25, "time": "2015-05-5"}
    mylist.append(record)

# blue light glasses
for b in range(4800,4900): # 100 b l g sold
    record = {"_id": b, "item_name": "blue_light_glasses", "value": 50, "time": "2015-05-5"}
    mylist.append(record)

# YEAR 2016
# book
for i in range(4900, 5400): # 500 books sold
    record = {"_id": i, "item_name": "book", "value": 15, "time": "2016-05-5"}
    mylist.append(record)

# head phones
for a in range(5400, 6300): # 900 head phones sold
    record = {"_id": a, "item_name": "head_phones", "value": 25, "time": "2016-05-5"}
    mylist.append(record)

# blue light glasses
for b in range(6300,7000): # 700 blue light glasses sold
    record = {"_id": b, "item_name": "blue_light_glasses", "value": 50, "time": "2016-05-5"}
    mylist.append(record)

# YEAR 2017
# book
for i in range(7400, 7800): # 400 books sold
    record = {"_id": i, "item_name": "book", "value": 15, "time": "2017-05-5"}
    mylist.append(record)

# head phones
for a in range(7800, 8600): # 800 head phones sold
    record = {"_id": a, "item_name": "head_phones", "value": 25, "time": "2017-05-5"}
    mylist.append(record)

# blue light glasses
for b in range(8600, 9200): # 600 blg sold
    record = {"_id": b, "item_name": "blue_light_glasses", "value": 50, "time": "2017-05-5"}
    mylist.append(record)

# YEAR 2018
# book
for i in range(9200,10000): # 800 books sold
    record = {"_id": i, "item_name": "book", "value": 15, "time": "2018-05-5"}
    mylist.append(record)

# head phones
for a in range(10000,11000): # 1000 head phones sold
    record = {"_id": a, "item_name": "head_phones", "value": 25, "time": "2018-05-5"}
    mylist.append(record)

# blue light glasses
for b in range(11000, 11700): # 700 blg sold
    record = {"_id": b, "item_name": "blue_light_glasses", "value": 50, "time": "2018-05-5"}
    mylist.append(record)

# YEAR 2019
# book
for i in range(11700, 12300): # 600 books sold
    record = {"_id": i, "item_name": "book", "value": 15, "time": "2019-05-5"}
    mylist.append(record)

# head phones
for a in range(12300, 13100): # 800 head phones sold
    record = {"_id": a, "item_name": "head_phones", "value": 25, "time": "2019-05-5"}
    mylist.append(record)

# blue light glasses
for b in range(13100, 13600): # 500 head phones sold
    record = {"_id": b, "item_name": "blue_light_glasses", "value": 50, "time": "2019-05-5"}
    mylist.append(record)

# YEAR 2020
# book
for i in range(13600, 14000): # 400 books sold
    record = {"_id": i, "item_name": "book", "value": 15, "time": "2020-05-5"}
    mylist.append(record)

# head phones
for a in range(14000, 14400): # 400 head phones sold
    record = {"_id": a, "item_name": "head_phones", "value": 25, "time": "2020-05-5"}
    mylist.append(record)

# blue light glasses
for b in range(14400, 14650): # 250 head phones
    record = {"_id": b, "item_name": "blue_light_glasses", "value": 50, "time": "2020-05-5"}
    mylist.append(record)

# YEAR 2021

# book
for i in range(14650, 15400): # 750 books sold
    record = {"_id": i, "item_name": "book", "value": 15, "time": "2021-05-5"}
    mylist.append(record)

# head phones
for a in range(15400, 16100): # 700 head phones sold
    record = {"_id": a, "item_name": "head_phones", "value": 25, "time": "2021-05-5"}
    mylist.append(record)

# blue light glasses
for b in range(16100, 16600): # 500 blg sold
    record = {"_id": b, "item_name": "blue_light_glasses", "value": 50, "time": "2021-05-5"}
    mylist.append(record)

# print(mylist)

x = mycol.insert_many(mylist)

#print a list of the _id values of the inserted documents:
print(x.inserted_ids)
