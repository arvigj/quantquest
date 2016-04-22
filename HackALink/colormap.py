import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import *
import pylab as p
import sys

a = []
for i in range(0, 50, 1):
	a.append(i)

data = np.loadtxt(sys.argv[1],unpack=True,usecols=a[0:],delimiter=',')
data = data.transpose()
labels = np.loadtxt(sys.argv[1],unpack=True,usecols=[50],dtype=str,delimiter=',')

fig, ax = plt.subplots()

for i in xrange(0,50):
	data[i,i] = 0

ax.pcolor(data,cmap='Blues')
plt.rcParams.update({'font.size':8})
ax.invert_yaxis()
ax.xaxis.tick_top()
plt.xticks(rotation=0)
ax.set_yticks(np.arange(0, 50, 1))
ax.set_xticks(np.arange(0, 50, 1))
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)

#p.colorbar()
plt.show()