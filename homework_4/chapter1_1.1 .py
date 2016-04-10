V = [] #declare the arrays we will need
t = []

g = 9.8 #declare the parameters we will need
end_time = 10

V.append(1000.) #initialize
t.append(0.)

dt = input ('dt->') #change dt 

for i in range(int(end_time / dt)):
	tmp = V[i] - g * dt
	V.append(tmp)
	t.append(dt * (i + 1))
	print t[-1], V[-1]

import numpy as np
import matplotlib.pyplot as plt
plt.plot(t,V,'g')
plt.title('the velocity of a freely falling object')
plt.xlabel('t(s)')
plt.ylabel('V(m/s)')
plt.show()
savefig("homework1_1.jpg")
