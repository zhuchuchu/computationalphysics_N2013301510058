import matplotlib.pyplot as plt
import numpy as np
import math
import pylab as pl

class CROMER_1(object):
    def __init__(self, _theta0=0.2, _omg0=0., _t0=0., _l=9.8,_g=9.8, _dt=6.0*math.pi/1000, _time=6000.0,):
        self.theta, self.omg, self.t = [_theta0], [_omg0], [_t0]
        self.l, self.g, self.dt, self.time, self.n= _l, _g, _dt, _time, int(_time/_dt)
        self.F_D=[0.0,0.5,1.2]
        self.q=[0,0.5,1.2]
        self.theta1=[]
        self.omg1=[]
        self.p=0
    def calculate(self):
        for i in range(self.n):
            self.omg.append(self.omg[i]+(-self.g/self.l*math.sin(self.theta[i])-self.q[1]*self.omg[i]+self.F_D[1]*math.sin(2./3.*self.t[i]))*self.dt)
            self.theta.append(self.theta[i]+self.omg[i+1]*self.dt)
            if self.theta[i+1]<-math.pi:
               self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
               self.theta[i+1]=self.theta[i+1]-2*math.pi
            self.t.append(self.t[i]+self.dt)
            self.p=i%1000
            if i%1000==375:
               self.theta1.append(self.theta[-1])
               self.omg1.append(self.omg[-1])
        self.theta1=self.theta1[100:]
        self.omg1=self.omg1[100:]
    def plot_theta1(self,_ax):
        _ax.axes.scatter(self.theta1, self.omg1, marker='o',color='m',label=r'$q=0.5 F_D=0.5$')

class CROMER_2(CROMER_1):
    def calculate(self):
        for i in range(self.n):
            self.omg.append(self.omg[i]+(-self.g/self.l*math.sin(self.theta[i])-self.q[1]*self.omg[i]+self.F_D[2]*math.sin(2./3.*self.t[i]))*self.dt)
            self.theta.append(self.theta[i]+self.omg[i+1]*self.dt)
            if self.theta[i+1]<-math.pi:
               self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
               self.theta[i+1]=self.theta[i+1]-2*math.pi
            self.t.append(self.t[i]+self.dt)
            if i%1000==375:
               self.theta1.append(self.theta[-1])
               self.omg1.append(self.omg[-1])
        self.theta1=self.theta1[100:]
        self.omg1=self.omg1[100:]
    def plot_theta2(self,_ax):
        _ax.axes.scatter(self.theta1,self.omg1,marker='o',color='b',label=r'$q=0.5 F_D=1.2$')

class CROMER_3(CROMER_1):
    def calculate(self):
        for i in range(self.n):
            self.omg.append(self.omg[i]+(-self.g/self.l*math.sin(self.theta[i])-self.q[0]*self.omg[i]+self.F_D[0]*math.sin(2./3.*self.t[i]))*self.dt)
            self.theta.append(self.theta[i]+self.omg[i+1]*self.dt)
            if self.theta[i+1]<-math.pi:
               self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
               self.theta[i+1]=self.theta[i+1]-2*math.pi
            self.t.append(self.t[i]+self.dt)
            if i%1000==375:
               self.theta1.append(self.theta[-1])
               self.omg1.append(self.omg[-1])
        self.theta1=self.theta1[100:]
        self.omg1=self.omg1[100:]
    def plot_theta3(self,_ax):
        _ax.axes.scatter(self.theta1,self.omg1,marker='o',color='b',label=r'$q=0 F_D=0$')

fig= plt.figure(figsize=(20,9))
ax1 = plt.subplot(132)
ax2 = plt.subplot(133)
ax3 = plt.subplot(131)
comp= CROMER_1()
comp.calculate()
comp.plot_theta1(ax1)
comp=CROMER_2()
comp.calculate()
comp.plot_theta2(ax2)
comp=CROMER_3()
comp.calculate()
comp.plot_theta3(ax3)

ax1.set_title(r'$\omega$ versus $\theta$',fontsize=14)
ax2.set_title(r'$\omega$ versus $\theta$',fontsize=14)
ax3.set_title(r'$\omega$ versus $\theta$',fontsize=14)
ax1.set_ylabel(r'$\omega$(radians/s)',fontsize=14)
ax1.set_xlabel(r'$\theta$ (radians)',fontsize=14)
ax2.set_xlabel(r'$\theta$(radians)',fontsize=14)
ax2.set_ylabel(r'$\omega$(radians/s)',fontsize=14)
ax3.set_xlabel(r'$\theta$(radians)',fontsize=14)
ax3.set_ylabel(r'$\omega$(radians/s)',fontsize=14)
ax1.legend(fontsize=20,loc='best')
ax2.legend(fontsize=20,loc='best')
ax3.legend(fontsize=20,loc='best')
plt.show(fig)
