from pylab import *
from math import *

g = 9.8

class flight_state:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.t = _t

class baseball:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.baseball_flight_state = []
        self.baseball_flight_state.append(_fs)
        self.dt = _dt
        #print self.baseball_flight_state[-1].x, self.baseball_flight_state[-1].y, self.baseball_flight_state[-1].vx, self.baseball_flight_state[-1].vy

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
        while not(self.baseball_flight_state[-1].y < 0):
            self.baseball_flight_state.append(self.next_state(self.baseball_flight_state[-1]))
        r = - self.baseball_flight_state[-2].y / self.baseball_flight_state[-1].y
        self.baseball_flight_state[-1].x = (self.baseball_flight_state[-2].x + r * self.baseball_flight_state[-1].x) / (r + 1)
        self.baseball_flight_state[-1].y = 0
        #print self.baseball_flight_state[-1].x, self.baseball_flight_state[-1].y, self.baseball_flight_state[-1].vx, self.baseball_flight_state[-1].vy


    def show_trajectory(self):
	global x,y        
	x = []
        y = []
        for fs in self.baseball_flight_state:
            x.append(fs.x)
            y.append(fs.y)

class drag_baseball(baseball):
    def next_state(self, current_state):
        global g
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
	b2m = 0.0039 + 0.0058/(1.+math.exp((v-35)/5))        
	next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

b = drag_baseball(flight_state(0, 0, 49*cos(pi*35/180), 49*sin(pi*35/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'c', label = 'with drag')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = baseball(flight_state(0, 0, 49*cos(pi*35/180), 49*sin(pi*35/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'m',label='no drag')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

text(10000,16000,r'$\theta=35^\circ$')
title('trajectory of baseball with and without drag')
xlabel('x(m)')
ylabel('y(m)')
show()
