import matplotlib.pyplot as plt
import numpy as np

class EULER(object):
    def __init__(self, _theta0=0.1/np.pi, _omg0=0, _t0=0., _l=9.8/(4*(np.pi)**2),_g=9.8, _dt=0.01, _time=10.):
        self.theta, self.omg, self.t = [_theta0], [_omg0], [_t0]
        self.l, self.g, self.dt, self.time, self.n= _l, _g, _dt, _time, int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]-self.g/self.l*self.theta[-1]*self.dt-self.omg[-1]*self.dt+0.2*np.sin(2.*np.pi*self.t[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-2]*self.dt)
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '--',label='Euler Method')

class CROMER(EULER):
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
 	    self.omg.append(self.omg[-1]-self.g/self.l*self.theta[-1]*self.dt-self.omg[-1]*self.dt+0.2*np.sin(2.*np.pi*self.t[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '--',label='Euler-Cromer Method')
        
fig= plt.figure(figsize=(10,5))
ax1 = plt.subplot()

comp= EULER()
comp.calculate()
comp.plot_theta(ax1)
comp= CROMER()
comp.calculate()
comp.plot_theta(ax1)

ax1.set_title('the resonance of linear, forced Pendulum with friction',fontsize=14)
ax1.set_xlabel('time'+r'$ /\tau $',fontsize=14)
ax1.set_ylabel('Angel (rad)',fontsize=14)
ax1.legend(fontsize=12,loc='best')
plt.show(fig)
