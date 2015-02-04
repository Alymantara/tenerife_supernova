import numpy as n
import matplotlib.pyplot as plt
import sn_maker as sn
reload(sn)


plt.ion()

fig1= plt.figure(1)
plt.clf()

t = n.arange(-15,130,0.5)

par = n.array([25,0.001,25.0,8.0,10.0,3.0,4.0])

mag = sn.sn_ia(t,par)
plt.plot(t,mag)

plt.ylim(1000,min(mag))

plt.draw()
plt.show()