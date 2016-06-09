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
                  0.0,1.0,4.1,
                  -1.0,1.0,4.1)
plotter.setAxesBounds(-0.1,4.1,-0.5,4.2)
plotter.axesDecorations('Sketch of a Function','x','f (x)')

axes = plotter.getAxes()
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.spines['bottom'].set_position(('data',0))
axes.yaxis.set_ticks_position('left')
axes.spines['left'].set_position(('data',0))

#plt.show()
plt.savefig('emptyAxes.pgf',format='pgf')

