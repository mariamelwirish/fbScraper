import numpy as np
from handler import sorting
from scrapper import scraping
import matplotlib.pyplot as plt
from datetime import datetime
pageName = scraping()
data = sorting(pageName)
shares = data[0]
comments = data[1]
likes = data[2]
scores: dict = data[3]

shareeeees = []
shareeeeesY = []
for uu, oo in shares.items():
    dataaae = datetime.strptime(uu,'%Y-%m-%d %H:%M:%S')
    shareeeees.append(dataaae.day)
    shareeeeesY.append(oo)
plt.scatter(shareeeees,shareeeeesY)

commmmmmmment = []
commmmmmmmentY = []
for uu, oo in comments.items():
    dataaae = datetime.strptime(uu,'%Y-%m-%d %H:%M:%S')
    commmmmmmment.append(dataaae.day)
    commmmmmmmentY.append(oo)
plt.scatter(commmmmmmment,commmmmmmmentY)

Likkkkkkes = []
LikkkkkkesY = []
for uu, oo in likes.items():
    dataaae = datetime.strptime(uu,'%Y-%m-%d %H:%M:%S')
    Likkkkkkes.append(dataaae.day)
    LikkkkkkesY.append(oo)
plt.scatter(Likkkkkkes,LikkkkkkesY)
plt.show()
