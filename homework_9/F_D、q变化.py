import matplotlib.pyplot as plt
import numpy as np
import math

class CROMER1(object):
    def __init__(self, _theta0=0.2, _omg0=0., _t0=0., _l=9.8,_g=9.8, _dt=0.04, _time=60.):
        self.theta, self.omg, self.t = [_theta0], [_omg0], [_t0]
	self.F_D=[0.0,0.5,1.2]
        self.q=[0.0,0.5,1.2]
        self.l, self.g, self.dt, self.time, self.n= _l, _g, _dt, _time, int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]+(-self.g/self.l*np.sin(self.theta[-1])-self.q[1]*self.omg[-1]+self.F_D[0]*np.sin(2./3.*self.t[-1]))*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-2]*self.dt)
            if self.theta[i+1]<-math.pi:
               self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
	       self.theta[i+1]=self.theta[i+1]-2*math.pi	
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '--',label=r'$F_D=0$')
    def plot_omega(self,_ax):
        _ax.plot(self.t, self.omg, '--',label=r'$F_D=0$')         

class CROMER2(CROMER1):
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]+(-self.g/self.l*np.sin(self.theta[-1])-self.q[1]*self.omg[-1]+self.F_D[1]*np.sin(2./3.*self.t[-1]))*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
            if self.theta[i+1]<-math.pi:
               self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
               self.theta[i+1]=self.theta[i+1]-2*math.pi
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '--',label=r'$F_D=0.5$')
    def plot_omega(self,_ax):
        _ax.plot(self.t, self.omg, '--',label=r'$F_D=0.5$')
        
class CROMER3(CROMER1):
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.omg.append(self.omg[-1]+(-self.g/self.l*np.sin(self.theta[-1])-self.q[1]*self.omg[-1]+self.F_D[2]*np.sin(2./3.*self.t[-1]))*self.dt)
            self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
            if self.theta[i+1]<-math.pi:
               self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
               self.theta[i+1]=self.theta[i+1]-2*math.pi
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '--',label=r'$F_D=1.2$')
    def plot_omega(self,_ax):
        _ax.plot(self.t, self.omg, '--',label=r'$F_D=1.2$')
        
fig= plt.figure(figsize=(13,8))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

comp= CROMER1()
comp.calculate()
comp.plot_theta(ax1)
comp.plot_omega(ax2)
comp= CROMER2()
comp.calculate()
comp.plot_theta(ax1)
comp.plot_omega(ax2)
comp= CROMER3()
comp.calculate()
comp.plot_theta(ax1)
comp.plot_omega(ax2)
ax1.set_title(r'$\theta$ versus time',fontsize=14)
ax2.set_title(r'$\omega$ versus time',fontsize=14)
ax1.set_xlabel('time(s)',fontsize=14)
ax1.set_ylabel(r'$\theta$ (radians)',fontsize=14)
ax2.set_xlabel('time(s)',fontsize=14)
ax2.set_ylabel(r'$\omega$(radians/s)',fontsize=14)
ax1.legend(fontsize=12,loc='best')
ax2.legend(fontsize=12,loc='best')
plt.show(fig)
