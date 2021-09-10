#Copyright © 2021 All rights reserved. Doga Ege Ozden

import matplotlib.pyplot as plt
import numpy as np

# List of the digital media contents
socialmediacontents = np.array(["Facebook Post", "Instagram Post", "Twitter Tweet&Retweet", "LinkedIn Post", "Youtube Video"])

# List of average number of posts per day
dailypostsmean = np.array([0.6, 0.7, 2.4, 0.9, 2.4])

font1 = {'family':'serif','color':'#0d94fb','size':20}
font2 = {'family':'serif','color':'#ffd966','size':15}

plt.title("Social Media Platforms By Digital Media", fontdict = font1)
plt.xlabel("Social Media Digital Content", fontdict = font2)
plt.ylabel("Average Number of Posts Per Day", fontdict = font2)
plt.bar(socialmediacontents, dailypostsmean, color="#0d94fb")
plt.show()
