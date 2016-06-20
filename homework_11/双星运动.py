import matplotlib.pyplot as plt
import numpy as np
import math

class planet(object):
    def __init__(self,_v10=[0.,1./3.*np.sqrt(6.*np.pi)],_v20=[0.,-2./3.*np.sqrt(6.*np.pi)],_t=0., _dt=0.0001, _time=7.):
        self.x1, self.y1, self.x2, self.y2, = [0.5], [0.], [-0.5], [0.]
	self.vx1, self.vy1, self.vx2, self.vy2, = [_v10[0]], [_v10[1]], [_v20[0]], [_v20[1]]
	self.t = [_t]
        self.dt, self.time, self.n=_dt, _time, int(_time/_dt)
	self.m1=4*np.pi
    def calculate(self):
        for i in range(self.n):
            self.r=np.sqrt((self.x1[-1]-self.x2[-1])**2+(self.y1[-1]-self.y2[-1])**2)
            self.vx1.append(self.vx1[-1]+self.dt*(-self.m1/3.*(self.x1[-1]-self.x2[-1])/self.r**3))
            self.vy1.append(self.vy1[-1]+self.dt*(-self.m1/3.*(self.y1[-1]-self.y2[-1])/self.r**3))
            self.vx2.append(self.vx2[-1]+self.dt*(-self.m1*(self.x2[-1]-self.x1[-1])/self.r**3))
            self.vy2.append(self.vy2[-1]+self.dt*(-self.m1*(self.y2[-1]-self.y1[-1])/self.r**3))
            self.x1.append(self.x1[-1]+self.dt*self.vx1[-1])
            self.y1.append(self.y1[-1]+self.dt*self.vy1[-1])
            self.x2.append(self.x2[-1]+self.dt*self.vx2[-1])
            self.y2.append(self.y2[-1]+self.dt*self.vy2[-1])
    def plot_x_y(self,_ax):
        _ax.plot(self.x1, self.y1,label='star '+r'$M_1$')   
	_ax.plot(self.x2, self.y2,label='star '+r'$M_2$')  

class planet2(planet):
    def calculate(self):
        for i in range(self.n):
            self.r=np.sqrt((self.x1[-1]-self.x2[-1])**2+(self.y1[-1]-self.y2[-1])**2)
            self.vx1.append(self.vx1[-1]+self.dt*(-self.m1/2.*(self.x1[-1]-self.x2[-1])/self.r**3))
            self.vy1.append(self.vy1[-1]+self.dt*(-self.m1/2.*(self.y1[-1]-self.y2[-1])/self.r**3))
            self.vx2.append(self.vx2[-1]+self.dt*(-self.m1*(self.x2[-1]-self.x1[-1])/self.r**3))
            self.vy2.append(self.vy2[-1]+self.dt*(-self.m1*(self.y2[-1]-self.y1[-1])/self.r**3))
            self.x1.append(self.x1[-1]+self.dt*self.vx1[-1])
            self.y1.append(self.y1[-1]+self.dt*self.vy1[-1])
            self.x2.append(self.x2[-1]+self.dt*self.vx2[-1])
            self.y2.append(self.y2[-1]+self.dt*self.vy2[-1])
    def plot_x_y2(self,_ax):
        _ax.plot(self.x1, self.y1,label='star '+r'$M_1$')   
	_ax.plot(self.x2, self.y2,label='star '+r'$M_2$')  

fig=plt.figure(figsize=(10,5)) 
ax1=plt.axes([0.1,0.1,0.35,0.7])
ax2=plt.axes([0.6,0.1,0.35,0.7])
ax1.set_xlim(-0.8,1.4)
ax1.set_ylim(-1.2,1.0)
ax2.set_xlim(-1.,1.2)
ax2.set_ylim(-1.4,0.8)
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
comp= planet()
comp.calculate()
comp.plot_x_y(ax1)
comp= planet2()
comp.calculate()
comp.plot_x_y2(ax2)

ax1.set_xlabel(r'$x$'+' (AU)',fontsize=18)
ax1.set_ylabel(r'$y$'+' (AU)',fontsize=18)
ax2.set_xlabel(r'$x$'+' (AU)',fontsize=18)
ax2.set_ylabel(r'$y$'+' (AU)',fontsize=18)
ax1.set_title(r'$M_1=3M_2$ binary system',fontsize=18)
ax2.set_title(r'$M_1=2M_2$ binary system',fontsize=18)
ax1.legend(loc='lower right')
ax2.legend(loc='lower right')
plt.show(fig)
