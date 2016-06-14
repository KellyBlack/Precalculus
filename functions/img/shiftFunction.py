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

x = np.arange(-8,8,0.02)
y = np.sin(5/np.pi * x)
plotter.setupGrid(0.3,'--',
                  -8.0,1.0,8.1,
                  -8.0,1.0,8.1)
plotter.setAxesBounds(-8.1,8.1,-8.1,8.1)
plotter.axesDecorations('Shifted Function','x','y')
plotter.addFunction(x,y,'--k')

y = 3+2*np.sin(5/np.pi * (x-0))
plotter.addFunction(x,y,'k')

axes = plotter.getAxes()
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.spines['bottom'].set_position(('data',0))
axes.yaxis.set_ticks_position('left')
axes.spines['left'].set_position(('data',0))

#plt.show()
plt.savefig('scaledSine.pgf',format='pgf')

###############################
plotter.clearPlot()
#plt.xkcd(scale=.6) #randomness=1,length=1,scale=0)

x = np.arange(-8,8,0.02)
y = np.sin(5/np.pi * x)
plotter.setupGrid(0.3,'--',
                  -8.0,1.0,8.1,
                  -8.0,1.0,8.1)
plotter.setAxesBounds(-8.1,8.1,-8.1,8.1)
plotter.axesDecorations('Shifted Function','x','y')
plotter.addFunction(x,y,'--k')

y = 3+2*np.sin(5/np.pi * (x-1))
plotter.addFunction(x,y,'k')

axes = plotter.getAxes()
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.spines['bottom'].set_position(('data',0))
axes.yaxis.set_ticks_position('left')
axes.spines['left'].set_position(('data',0))

#plt.show()
plt.savefig('scaledShiftedSine.pgf',format='pgf')


