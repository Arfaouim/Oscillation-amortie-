import matplotlib.pyplot as plt
import numpy as np

x=np.arange(start=-10, stop=10, step=0.001)
def f(x):
    return 5*np.sin(30*x)*np.exp(-x)

fig=plt.figure()
ax=plt.axes()
ax.plot(x,f(x))
plt.axis('tight')
plt.show()
