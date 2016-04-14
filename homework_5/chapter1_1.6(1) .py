import numpy as np
t=np.arange(0,20,1);
y=1000*np.exp(10*t)
import matplotlib.pyplot as plt
plt.plot(t,y,'r')
plt.title('population growth problem while b=0')
plt.xlabel('time')
plt.ylabel('population N')
plt.show()
