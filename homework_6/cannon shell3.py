from pylab import *
from math import *

g = 9.8
b2m = 4e-5

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

class isothermal_drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
	factor = exp( - current_state.y / 1e4)
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - factor * b2m * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - factor * b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

class adiabatic_drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
	factor = (1 - 6.5e-3 * current_state.y / 288.15) ** 2.5
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt * factor
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

b = drag_cannon(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'c', label = 'with drag')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = cannon(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'m',label='no drag')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

c = isothermal_drag_cannon(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
c.shoot()
c.show_trajectory()
plot(x,y,'b',label='isothermal approximation')
legend(loc='best',prop={'size':11},frameon=False)
c_final=x[-1]

d = adiabatic_drag_cannon(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
d.shoot()
d.show_trajectory()
plot(x,y,'y',label='adiabatic approximation')
legend(loc='best',prop={'size':11},frameon=False)
d_final=x[-1]

text(10000,16000,r'$\theta=45^\circ$')
title('trajectory of cannon shell with different drag')
xlabel('x(km)')
ylabel('y(km)')
xlim(0,60000)
ylim(0,18000)
show()
