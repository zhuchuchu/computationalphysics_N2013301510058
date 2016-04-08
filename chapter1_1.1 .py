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

