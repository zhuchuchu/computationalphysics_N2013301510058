N = []
t = []
dt = input('dt->')
a = 10
N.append(1000.)
t.append(0)
end_time = input('end time->')

for i in range(int(end_time / dt)):
	tmp = N[i] + a * N[i] * dt
	N.append(tmp)
	t.append(dt * (i + 1))
	print t[-1], N[-1]
import matplotlib.pyplot as plt
plt.plot(t,N)
plt.title('population growth problem while b=0 (using Euler method)')
plt.xlabel('t / year')
plt.ylabel('N (population)')
plt.show()


