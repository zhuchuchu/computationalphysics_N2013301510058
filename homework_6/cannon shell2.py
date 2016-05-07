from pylab import *
from math import *

g = 9.8
b2m = 1e-5
a2=2e-5
a3=3e-5
a4=4e-5
a5=5e-5
a10=1e-4
a20=2e-4

class flight_state:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.t = _t

class cannon:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt
        #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
	next_t = current_state.t + self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, next_t)

    def shoot(self):
        while not(self.cannon_flight_state[-1].y < 0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0
        #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy


    def show_trajectory(self):
	global x,y        
	x = []
        y = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)

class drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

class drag_cannon2(cannon):
    def next_state(self, current_state):
        global g, a2
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - a2 * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - a2 * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

class drag_cannon3(cannon):
    def next_state(self, current_state):
        global g, a3
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - a3 * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - a3 * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

class drag_cannon4(cannon):
    def next_state(self, current_state):
        global g, a4
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - a4 * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - a4 * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

class drag_cannon5(cannon):
    def next_state(self, current_state):
        global g, a5
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - a5 * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - a5 * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

class drag_cannon10(cannon):
    def next_state(self, current_state):
        global g, a10
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - a10 * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - a10 * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

class drag_cannon20(cannon):
    def next_state(self, current_state):
        global g, a20
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - a20 * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - a20 * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)


b = drag_cannon(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'c', label = r'$\frac{B2}{m}=1 \times e^{-5}$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = drag_cannon2(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'m',label=r'$\frac{B2}{m}=2 \times e^{-5}$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

c = drag_cannon3(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
c.shoot()
c.show_trajectory()
plot(x,y,'b',label=r'$\frac{B2}{m}=3 \times e^{-5}$')
legend(loc='best',prop={'size':11},frameon=False)
c_final=x[-1]

d = drag_cannon4(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
d.shoot()
d.show_trajectory()
plot(x,y,'y',label=r'$\frac{B2}{m}=4 \times e^{-5}$')
legend(loc='best',prop={'size':11},frameon=False)
d_final=x[-1]

e = drag_cannon5(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
e.shoot()
e.show_trajectory()
plot(x,y,'r',label=r'$\frac{B2}{m}=5 \times e^{-5}$')
legend(loc='best',prop={'size':11},frameon=False)
e_final=x[-1]

f = drag_cannon10(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
f.shoot()
f.show_trajectory()
plot(x,y,'g',label=r'$\frac{B2}{m}=10 \times e^{-5}$')
legend(loc='best',prop={'size':11},frameon=False)
f_final=x[-1]

h = drag_cannon10(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
h.shoot()
h.show_trajectory()
plot(x,y,'k',label=r'$\frac{B2}{m}=20 \times e^{-5}$')
legend(loc='best',prop={'size':11},frameon=False)
h_final=x[-1]

text(40000,16000,r'$\theta=45^\circ$')
title('trajectory of cannon shell with different b2m')
xlabel('x(km)')
ylabel('y(km)')
xlim(0,60000)
ylim(0,18000)
show()
