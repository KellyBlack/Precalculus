#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
from matplotlib.patches import FancyArrowPatch
from matplotlib.patches import Ellipse
import math

import sys

from BasicPlot import BasicPlot

plotter = BasicPlot()
plt.figure(num=1,frameon=False)

###############################
plt.close('all')
plotter.clearPlot()
plotter.setFigure(None,(10,3.5))
#plt.xkcd(scale=.6) #randomness=1,length=1,scale=0)

x = np.arange(0,5,0.02)
plotter.setupGrid(0.3,'--',
                  0.0,np.pi/2,3.0*np.pi,
                  -1.0,1.0,1.1)
plotter.setAxesBounds(0,8.1,-1.1,1.1)
plotter.axesDecorations('Y-coordinate Of The Earth',r"$\theta$",'y')
plotter.xAxisLabels(np.arange(0.0,3.0*np.pi,0.5*np.pi),
                   ["0",r"$\frac{\pi}{2}$",r"$\pi$",r"$\frac{3\pi}{2}$",r"$2\pi$",r"$\frac{5\pi}{2}$"])

axes = plotter.getAxes()
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.spines['bottom'].set_position(('data',0))
axes.yaxis.set_ticks_position('left')
axes.spines['left'].set_position(('data',0))
axes.xaxis.set_label_coords(0.95, 0.45)
axes.yaxis.set_label_coords(-0.05, 0.95)

#plt.show()
plt.savefig('emptyAxesEarthY.pgf',format='pgf')

###############################
plt.close('all')
plotter.clearPlot()
plotter.setFigure(None,(10,3.5))
#plt.xkcd(scale=.6) #randomness=1,length=1,scale=0)

x = np.arange(0,5,0.02)
plotter.setupGrid(0.3,'--',
                  0.0,np.pi/2,3.0*np.pi,
                  -1.0,1.0,1.1)
plotter.setAxesBounds(0,8.1,-1.1,1.1)
plotter.axesDecorations('X-coordinate Of The Earth',r"$\theta$",'x')
plotter.xAxisLabels(np.arange(0.0,3.0*np.pi,0.5*np.pi),
                   ["0",r"$\frac{\pi}{2}$",r"$\pi$",r"$\frac{3\pi}{2}$",r"$2\pi$",r"$\frac{5\pi}{2}$"])

axes = plotter.getAxes()
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.spines['bottom'].set_position(('data',0))
axes.yaxis.set_ticks_position('left')
axes.spines['left'].set_position(('data',0))
axes.xaxis.set_label_coords(0.95, 0.45)
axes.yaxis.set_label_coords(-0.05, 0.95)

#plt.show()
plt.savefig('emptyAxesEarthX.pgf',format='pgf')

