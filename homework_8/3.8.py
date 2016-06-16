import matplotlib.pyplot as plt
import numpy as np

class EULER1(object):
    def __init__(self, _theta0=1., _omg0=0, _t0=0., _l=1.,_g=9.8, _dt=0.01, _time=10.):
        self.theta, self.omg, self.t = [_theta0], [_omg0], [_t0]
        self.l, self.g, self.dt, self.time, self.n= _l, _g, _dt, _time, int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]-self.g/self.l*np.sin(self.theta[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-2]*self.dt)

class CROMER1(EULER1):
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]-self.g/self.l*np.sin(self.theta[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '--',label=r'$\theta_0=1$')

class EULER2(object):
    def __init__(self, _theta0=2., _omg0=0, _t0=0., _l=1.,_g=9.8, _dt=0.01, _time=10.):
        self.theta, self.omg, self.t = [_theta0], [_omg0], [_t0]
        self.l, self.g, self.dt, self.time, self.n= _l, _g, _dt, _time, int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]-self.g/self.l*np.sin(self.theta[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-2]*self.dt)

class CROMER2(EULER2):
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]-self.g/self.l*np.sin(self.theta[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '--',label=r'$\theta_0=2$')
        
class EULER4(object):
    def __init__(self, _theta0=4., _omg0=0, _t0=0., _l=1.,_g=9.8, _dt=0.01, _time=10.):
        self.theta, self.omg, self.t = [_theta0], [_omg0], [_t0]
        self.l, self.g, self.dt, self.time, self.n= _l, _g, _dt, _time, int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]-self.g/self.l*np.sin(self.theta[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-2]*self.dt)

class CROMER4(EULER4):
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]-self.g/self.l*np.sin(self.theta[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '--',label=r'$\theta_0=4$')

class EULER8(object):
    def __init__(self, _theta0=8., _omg0=0, _t0=0., _l=1.,_g=9.8, _dt=0.01, _time=10.):
        self.theta, self.omg, self.t = [_theta0], [_omg0], [_t0]
        self.l, self.g, self.dt, self.time, self.n= _l, _g, _dt, _time, int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]-self.g/self.l*np.sin(self.theta[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-2]*self.dt)

class CROMER8(EULER8):
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]-self.g/self.l*np.sin(self.theta[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '--',label=r'$\theta_0=8$')

class EULER16(object):
    def __init__(self, _theta0=16., _omg0=0, _t0=0., _l=1.,_g=9.8, _dt=0.01, _time=10.):
        self.theta, self.omg, self.t = [_theta0], [_omg0], [_t0]
        self.l, self.g, self.dt, self.time, self.n= _l, _g, _dt, _time, int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]-self.g/self.l*np.sin(self.theta[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-2]*self.dt)

class CROMER16(EULER16):
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]-self.g/self.l*np.sin(self.theta[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '--',label=r'$\theta_0=16$')
        
fig= plt.figure(figsize=(25,5))
ax1 = plt.subplot()

comp= CROMER1()
comp.calculate()
comp.plot_theta(ax1)
comp= CROMER2()
comp.calculate()
comp.plot_theta(ax1)
comp= CROMER4()
comp.calculate()
comp.plot_theta(ax1)
comp= CROMER8()
comp.calculate()
comp.plot_theta(ax1)
comp= CROMER16()
comp.calculate()
comp.plot_theta(ax1)

ax1.set_title('large angles pendulum without friction',fontsize=14)
ax1.set_xlabel('time'+r'$ /\tau $',fontsize=14)
ax1.set_ylabel('Angel (rad)',fontsize=14)
ax1.legend(fontsize=12,loc='best')
plt.show(fig)
