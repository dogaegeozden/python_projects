#Copyright © 2021 All rights reserved. Doga Ege Ozden

import matplotlib.pyplot as plt
import numpy as np

socialmediaplatforms = np.array(["Facebook", "Instagram", "Twitter", "LinkedIn", "Youtube"])
fallowers = np.array([575238, 47900, 102900, 477672, 32900])

font1 = {'family':'serif','color':'#0d94fb','size':20}
font2 = {'family':'serif','color':'#ffd966','size':15}

plt.title("Social Media Platforms By Fallowers", fontdict = font1)
plt.xlabel("Socal Media Platforms", fontdict = font2)
plt.ylabel("Fallowers", fontdict = font2)
plt.bar(socialmediaplatforms, fallowers, color="#0d94fb")
plt.show()
