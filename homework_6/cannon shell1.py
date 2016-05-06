from pylab import *
from math import *

g = 9.8
b2m = 1e-5

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

class adiabatic_drag_cannon(cannon):
    def next_state(self, current_state):
        pass


a = cannon(flight_state(0, 0, 700*cos(pi*30/180), 700*sin(pi*30/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'r',label = r'$\theta=30^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
a_final = x[-1]

b = drag_cannon(flight_state(0, 0, 700*cos(pi*30/180), 700*sin(pi*30/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'r--', label = r'$drag\theta=30^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = cannon(flight_state(0, 0, 700*cos(pi*35/180), 700*sin(pi*35/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'b',label=r'$\theta=35^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

b = drag_cannon(flight_state(0, 0, 700*cos(pi*35/180), 700*sin(pi*35/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'b--', label = r'$drag\theta=35^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = cannon(flight_state(0, 0, 700*cos(pi*40/180), 700*sin(pi*40/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'y',label=r'$\theta=40^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

b = drag_cannon(flight_state(0, 0, 700*cos(pi*40/180), 700*sin(pi*40/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'y--', label = r'$drag\theta=40^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = cannon(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'c',label=r'$\theta=45^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

b = drag_cannon(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'c--', label = r'$drag\theta=45^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = cannon(flight_state(0, 0, 700*cos(pi*50/180), 700*sin(pi*50/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'g',label=r'$\theta=50^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

b = drag_cannon(flight_state(0, 0, 700*cos(pi*50/180), 700*sin(pi*50/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'g--', label = r'$drag\theta=50^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = cannon(flight_state(0, 0, 700*cos(pi*55/180), 700*sin(pi*55/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,color='m',label=r'$\theta=55^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

b = drag_cannon(flight_state(0, 0, 700*cos(pi*55/180), 700*sin(pi*55/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'m--', label = r'$drag\theta=55^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

title('trajectory of cannon shell')
xlabel('x(km)')
ylabel('y(km)')
show()


