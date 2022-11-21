import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,2,100)

y = 3*x**4+8*x**3-6*6
y1 = x + np.sin(x)
y2 = (x**3+5)/(x**2+2)
y3 = np.log(x**4+1)-4


plt.plot(x,y, 'b:',linewidth=5)
plt.plot(x,y1,'r:',linewidth=5)
plt.plot(x,y2,'g:',linewidth=5)
plt.plot(x,y3,'y:',linewidth=5)
plt.grid(color='black',linestyle=':')
plt.show()