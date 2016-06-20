import matplotlib.pyplot as plt
import numpy as np
import math

class planet(object):
    def __init__(self,_v0=[0.,-2./3.*np.sqrt(6.*np.pi)],_t=0., _dt=0.0001, _time=7.):
        self.x, self.y, = [1], [0.]
	self.vx, self.vy, = [_v0[0]], [_v0[1]]
	self.t = [_t]
        self.dt, self.time, self.n=_dt, _time, int(_time/_dt)
	self.m=4*np.pi
    def calculate(self):
        for i in range(self.n):
            self.r=np.sqrt(self.x[-1]**2+self.y[-1]**2)
            self.vx.append(self.vx[-1]+self.dt*(-self.m*self.x[-1]/self.r**3))
            self.vy.append(self.vy[-1]+self.dt*(-self.m*self.y[-1]/self.r**3))
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
    def plot_x_y(self,_ax):
	_ax.plot(self.x, self.y,label=r'$\beta$=2')  

class planet2(planet):
    def calculate(self):
        for i in range(self.n):
            self.r=np.sqrt(self.x[-1]**2+self.y[-1]**2)
            self.vx.append(self.vx[-1]+self.dt*(-self.m*self.x[-1]/self.r**3.05))
            self.vy.append(self.vy[-1]+self.dt*(-self.m*self.y[-1]/self.r**3.05))
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
    def plot_x_y2(self,_ax):
	_ax.plot(self.x, self.y,label=r'$\beta$=2.05')  

class planet3(planet):
    def calculate(self):
        for i in range(self.n):
            self.r=np.sqrt(self.x[-1]**2+self.y[-1]**2)
            self.vx.append(self.vx[-1]+self.dt*(-self.m*self.x[-1]/self.r**3.15))
            self.vy.append(self.vy[-1]+self.dt*(-self.m*self.y[-1]/self.r**3.15))
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
    def plot_x_y3(self,_ax):
	_ax.plot(self.x, self.y,label=r'$\beta$=2.15')  

class planet4(planet):
    def calculate(self):
        for i in range(self.n):
            self.r=np.sqrt(self.x[-1]**2+self.y[-1]**2)
            self.vx.append(self.vx[-1]+self.dt*(-self.m*self.x[-1]/self.r**3.25))
            self.vy.append(self.vy[-1]+self.dt*(-self.m*self.y[-1]/self.r**3.25))
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
    def plot_x_y4(self,_ax):
	_ax.plot(self.x, self.y,label=r'$\beta$=2.25')  

fig=plt.figure(figsize=(10,5)) 
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
ax3 = plt.subplot(221)
ax4 = plt.subplot(222)
comp= planet()
comp.calculate()
comp.plot_x_y(ax1)
comp= planet2()
comp.calculate()
comp.plot_x_y2(ax2)
comp= planet3()
comp.calculate()
comp.plot_x_y3(ax3)
comp= planet4()
comp.calculate()
comp.plot_x_y4(ax4)
ax1.set_xlabel(r'$x$'+' (AU)',fontsize=18)
ax1.set_ylabel(r'$y$'+' (AU)',fontsize=18)
ax2.set_xlabel(r'$x$'+' (AU)',fontsize=18)
ax2.set_ylabel(r'$y$'+' (AU)',fontsize=18)
ax3.set_ylabel(r'$y$'+' (AU)',fontsize=18)
ax3.set_title('binary system',fontsize=18)
ax4.set_title('binary system',fontsize=18)
ax1.legend(loc='lower right')
ax2.legend(loc='lower right')
ax3.legend(loc='lower right')
ax4.legend(loc='lower right')
plt.show(fig)
