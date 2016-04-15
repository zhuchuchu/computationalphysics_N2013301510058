N = []
t = []
dt = input('dt->')
a = 10
b = input('b->')
N.append(1000.)
t.append(0)
end_time = input('end time->')

for i in range(int(end_time / dt)):
	tmp = N[i] + (a*N[i] - b*N[i]**2)* dt
	N.append(tmp)
	t.append(dt * (i + 1))
	print t[-1], N[-1]
import matplotlib.pyplot as plt
plt.plot(t,N)
plt.title('population growth problems using Euler method(b<0.01)')
plt.xlabel('t / year')
plt.ylabel('N (population)')
plt.show()


