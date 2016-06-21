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
plotter.clearPlot()
#plt.xkcd(scale=.6) #randomness=1,length=1,scale=0)

x = np.arange(0,5,0.02)
plotter.setupGrid(0.3,'--',
                  0.0,np.pi/2,3.0*np.pi,
                  -1.0,1.0,1.1)
plotter.setAxesBounds(0,8.1,-1.1,1.1)
plotter.axesDecorations('Sine',r"$\theta$",'sin')
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
plt.savefig('emptySineAxes.pgf',format='pgf')

###############################
plotter.clearPlot()
#plt.xkcd(scale=.6) #randomness=1,length=1,scale=0)

x = np.arange(0,5,0.02)
plotter.setupGrid(0.3,'--',
                  0.0,np.pi/2,3.0*np.pi,
                  -1.0,1.0,1.1)
plotter.setAxesBounds(0,8.1,-1.1,1.1)
plotter.axesDecorations('Cosine',r"$\theta$",'cos')
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
plt.savefig('emptyAxesCosine.pgf',format='pgf')

