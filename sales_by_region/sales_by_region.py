import matplotlib.pyplot as plt
import numpy as np

regions = np.array(["Canada", "USA", "China"])
sales = np.array([675000000, 11098000000, 14682000000])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Market by region", fontdict = font1)
plt.xlabel("Regions", fontdict = font2)
plt.ylabel("Sales in dollars", fontdict = font2)
plt.bar(regions, sales, color="orange")
plt.show()
