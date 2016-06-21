import matplotlib.pyplot as plt
import numpy as np
import math

class Lorentz1(object):
    def __init__(self, _x=1., _y=0., _z=0., _t=0., _dt=0.0001, _time=30.):
        self.x, self.y, self.z, self.t = [_x], [_y], [_z], [_t]
        self.dt, self.time, self.n=_dt, _time, int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.x.append(self.x[-1]+10*(self.y[-1]-self.x[-1])*self.dt)
	    self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+5.*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-8./3.*self.z[-1])*self.dt)
    def plot_time_z1(self,_ax):
        _ax.plot(self.x, self.z, label=r'$r=5$')   
    
    def plot_section_zx(self,_ax,_secy=0.):          
        self.z_sec, self.x_sec = [], []
        self.secy = _secy
        for i in range(len(self.t)):
            if abs(self.y[i]-self.secy)<4E-3:
                self.z_sec.append(self.z[i])
                self.x_sec.append(self.x[i])
        if len(self.z_sec)>0:
            _ax.plot(self.x_sec,self.z_sec,'ok',markersize=4,label=r'$r=10$')

class Lorentz2(object):
    def __init__(self, _x=1., _y=0., _z=0., _t=0., _dt=0.0001, _time=30.):
        self.x, self.y, self.z, self.t = [_x], [_y], [_z], [_t]
        self.dt, self.time, self.n=_dt, _time, int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.x.append(self.x[-1]+10*(self.y[-1]-self.x[-1])*self.dt)
	    self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+10.*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-8./3.*self.z[-1])*self.dt)
    def plot_time_z2(self,_ax):
        _ax.plot(self.x, self.z, label=r'$r=10$')  
  
    def plot_section_zx(self,_ax,_secy=0.):          
        self.z_sec, self.x_sec = [], []
        self.secy = _secy
        for i in range(len(self.t)):
            if abs(self.y[i]-self.secy)<4E-3:
                self.z_sec.append(self.z[i])
                self.x_sec.append(self.x[i])
        if len(self.z_sec)>0:
            _ax.plot(self.x_sec,self.z_sec,'ok',markersize=4,label=r'$r=10$')

class Lorentz3(object):
    def __init__(self, _x=1., _y=0., _z=0., _t=0., _dt=0.0001, _time=30.):
        self.x, self.y, self.z, self.t = [_x], [_y], [_z], [_t]
        self.dt, self.time, self.n=_dt, _time, int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.x.append(self.x[-1]+10*(self.y[-1]-self.x[-1])*self.dt)
	    self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+15.*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-8./3.*self.z[-1])*self.dt)
    def plot_time_z3(self,_ax):
        _ax.plot(self.x, self.z, label=r'$r=15$')  

    def plot_section_zx(self,_ax,_secy=0.):          
        self.z_sec, self.x_sec = [], []
        self.secy = _secy
        for i in range(len(self.t)):
            if abs(self.y[i]-self.secy)<4E-3:
                self.z_sec.append(self.z[i])
                self.x_sec.append(self.x[i])
        if len(self.z_sec)>0:
            _ax.plot(self.x_sec,self.z_sec,'ok',markersize=4,label=r'$r=10$')
   
class Lorentz4(object):
    def __init__(self, _x=1., _y=0., _z=0., _t=0., _dt=0.0001, _time=30.):
        self.x, self.y, self.z, self.t = [_x], [_y], [_z], [_t]
        self.dt, self.time, self.n=_dt, _time, int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.t.append(self.t[-1]+self.dt)
	    self.x.append(self.x[-1]+10*(self.y[-1]-self.x[-1])*self.dt)
	    self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+25.*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-8./3.*self.z[-1])*self.dt)
    def plot_time_z4(self,_ax):
        _ax.plot(self.x, self.z,label=r'$r=25$') 
 
    def plot_section_zx(self,_ax,_secy=0.):          
        self.z_sec, self.x_sec = [], []
        self.secy = _secy
        for i in range(len(self.t)):
            if abs(self.y[i]-self.secy)<4E-3:
                self.z_sec.append(self.z[i])
                self.x_sec.append(self.x[i])
        if len(self.z_sec)>0:
            _ax.plot(self.x_sec,self.z_sec,'ok',markersize=4,label=r'$r=10$')

fig= plt.figure()
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
ax3 = plt.subplot(221)
ax4 = plt.subplot(222)
comp= Lorentz1()
comp.calculate()
comp.plot_time_z1(ax1)
comp= Lorentz2()
comp.calculate()
comp.plot_time_z2(ax2)
comp= Lorentz3()
comp.calculate()
comp.plot_time_z3(ax3)
comp= Lorentz4()
comp.calculate()
comp.plot_time_z4(ax4)
ax1.set_title(r'Lorentz modle z versus x')
ax1.set_ylabel('z',fontsize=14)
ax4.set_xlabel('x',fontsize=14)
ax1.legend(loc='best')
ax2.legend(loc='best')
ax3.legend(loc='best')
ax4.legend(loc='best')
plt.show(fig)

fig= plt.figure()
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
ax3 = plt.subplot(221)
ax4 = plt.subplot(222)
comp= Lorentz1()
comp.calculate()
comp.plot_section_zx(ax1)
comp= Lorentz2()
comp.calculate()
comp.plot_section_zx(ax2)
comp= Lorentz3()
comp.calculate()
comp.plot_section_zx(ax3)
comp= Lorentz4()
comp.calculate()
comp.plot_section_zx(ax4)
ax1.set_title(r'Lorentz modle z versus x when y=0')
ax1.set_ylabel('z',fontsize=14)
ax4.set_xlabel('x',fontsize=14)
ax1.legend(loc='best')
ax2.legend(loc='best')
ax3.legend(loc='best')
ax4.legend(loc='best')
plt.show(fig)
