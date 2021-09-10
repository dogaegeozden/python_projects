#Copyright © 2021 All rights reserved. Doga Ege Ozden

import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal

tsotc = Decimal(input("Enter the total sales of the company here: "))
tsotm = Decimal(input("Enter the total sales of the market here: "))
marketshare = (tsotc / tsotm) * 100
print(marketshare)

tcs = marketshare
os = 100 - marketshare

y = np.array([tcs, os])
mylabels = ["2nd Shot", "Others"]
myexplode = [0.2, 0]

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}


plt.title("Market share", fontdict = font1)
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.xlabel("Canada", fontdict = font2)
plt.legend(title = "Companies")
plt.show()
