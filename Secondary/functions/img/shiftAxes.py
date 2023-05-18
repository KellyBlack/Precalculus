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
                  -5.0,1.0,5.1,
                  -5.0,1.0,5.1)
plotter.setAxesBounds(-5.1,5.1,-5.1,5.1)
plotter.axesDecorations('Comparing Shifted Functions','x','y')

axes = plotter.getAxes()
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.spines['bottom'].set_position(('data',0))
axes.yaxis.set_ticks_position('left')
axes.spines['left'].set_position(('data',0))
axes.xaxis.set_label_coords(0.95, 0.45)
axes.yaxis.set_label_coords(0.45, 0.95)


#plt.show()
plt.savefig('emptyAxesShifted.pgf',format='pgf')


