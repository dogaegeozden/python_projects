import numpy as np
import matplotlib.pyplot as plt

y = np.array([300, 310, 340, 320, 340, 415, 420, 390, 455, 445, 460])
x = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])

plt.title("Revenue")
plt.xlabel("Years")
plt.ylabel("Total Sales")

plt.plot(x, y)

plt.grid()

plt.show()
