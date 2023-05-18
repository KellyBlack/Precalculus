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

x = np.arange(0,2.0*np.pi,np.pi/100)
plotter.setupGrid(0.3,'--',
                  -1.0,0.5,1.1,
                  -1.0,0.5,1.1)
plotter.setAxesBounds(-1.2,1.2,-1.2,1.2)
plotter.axesDecorations(r'The Plainfield 500$\pi$',r"x",r'y')
plotter.addFunction(np.cos(x),np.sin(x),'k')
plotter.setAxesValue('equal')

plotter.addFunction([0,np.sqrt(2)/2],[0,np.sqrt(2)/2],'k')
plotter.filledCircle(np.sqrt(2)/2,np.sqrt(2)/2,0.02)
plotter.placeText(0.12*np.cos(np.pi/10),0.12*np.sin(np.pi/10),r"$\theta$",size=22)

axes = plotter.getAxes()
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.spines['bottom'].set_position(('data',0))
axes.yaxis.set_ticks_position('left')
axes.spines['left'].set_position(('data',0))
axes.xaxis.set_label_coords(0.97, 0.45)
axes.yaxis.set_label_coords(0.45, 0.95)

#plt.show()
plt.savefig('plainfield500.pgf',format='pgf')

