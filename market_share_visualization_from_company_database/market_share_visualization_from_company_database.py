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

totalCS = 0
for s in mycol.find({},{ "_id": 0, "item_name": 1, "value": 1 }):
    totalCS += s["value"]

print(totalCS)
# # Data visualization
theCompName = input("Enter your company name here: ")
tsotm = Decimal(input("Enter the total sales of the market here: "))

marketshare = (totalCS / tsotm) * 100
print(marketshare)

tcs = marketshare
os = 100 - marketshare

y = np.array([tcs, os])
mylabels = [theCompName, "Others"]
myexplode = [0.2, 0]

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Market share", fontdict = font1)
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.xlabel("Canada", fontdict = font2)
plt.legend(title = "Companies")
plt.show()
