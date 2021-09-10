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
userNameD = "test"
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
mylist = [
  { "_id": 1, "item_name": "a_book", "value": 15},
  { "_id": 2, "item_name": "a_book", "value": 15},
  { "_id": 3, "item_name": "a_book", "value": 15},
  { "_id": 4, "item_name": "a_book", "value": 15},
  { "_id": 5, "item_name": "b_book", "value": 20},
  { "_id": 6, "item_name": "b_book", "value": 20},
  { "_id": 7, "item_name": "b_book", "value": 20},
  { "_id": 8, "item_name": "b_book", "value": 20},
  { "_id": 9, "item_name": "b_book", "value": 20},
  { "_id": 10, "item_name": "c_book", "value": 30},
  { "_id": 11, "item_name": "c_book", "value": 30},
  { "_id": 12, "item_name": "c_book", "value": 30},
  { "_id": 13, "item_name": "c_book", "value": 30},
  { "_id": 14, "item_name": "c_book", "value": 30}
]

x = mycol.insert_many(mylist)

#print a list of the _id values of the inserted documents:
print(x.inserted_ids)
