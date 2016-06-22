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
plotter.setFigure(None,(10,3.5))
plotter.clearPlot()
#plt.xkcd(scale=.6) #randomness=1,length=1,scale=0)

plotter.setupGrid(0.3,'--',
                  -3.0*np.pi,np.pi/2,3.0*np.pi,
                  -3.0,1.0,3.1)
plotter.setAxesBounds(-9.5,9.5,-3.1,3.1)
plotter.axesDecorations('Shifted Sine',r"$x$",'f,g')
plotter.xAxisLabels(np.arange(-3.0*np.pi,3.0*np.pi+0.5,0.5*np.pi),
                   [r"$-3\pi$",r"$-\frac{5\pi}{2}$",
                    r"$-2\pi$",r"$-\frac{3\pi}{2}$",
                    r"$-\pi$",r"$-\frac{\pi}{2}$",
                    "0",r"$\frac{\pi}{2}$",
                    r"$\pi$",r"$\frac{3\pi}{2}$",
                    r"$2\pi$",r"$\frac{5\pi}{2}$",r"$3\pi$"])
#plotter.setAspectRation(.8)

axes = plotter.getAxes()
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.spines['bottom'].set_position(('data',0))
axes.yaxis.set_ticks_position('left')
axes.spines['left'].set_position(('data',0))
axes.xaxis.set_label_coords(0.95, 0.53)
axes.yaxis.set_label_coords(0.45, 0.95)

#plt.show()
plt.savefig('trigGraphs_1.pgf',format='pgf')


###############################
plt.close('all')
plotter.setFigure(None,(10,3.5))
plotter.clearPlot()
#plt.xkcd(scale=.6) #randomness=1,length=1,scale=0)

plotter.setupGrid(0.3,'--',
                  -3.0*np.pi,np.pi/2,3.0*np.pi,
                  -3.0,1.0,5.1)
plotter.setAxesBounds(-9.5,9.5,-3.1,5.1)
plotter.axesDecorations('Shifted Sine',r"$x$",'h,p')
plotter.xAxisLabels(np.arange(-3.0*np.pi,3.0*np.pi+0.5,0.5*np.pi),
                   [r"$-3\pi$",r"$-\frac{5\pi}{2}$",
                    r"$-2\pi$",r"$-\frac{3\pi}{2}$",
                    r"$-\pi$",r"$-\frac{\pi}{2}$",
                    "0",r"$\frac{\pi}{2}$",
                    r"$\pi$",r"$\frac{3\pi}{2}$",
                    r"$2\pi$",r"$\frac{5\pi}{2}$",r"$3\pi$"])
#plotter.setAspectRation(.8)

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
plt.savefig('trigGraphs_2.pgf',format='pgf')

###############################
plt.close('all')
plotter.setFigure(None,(10,3.5))
plotter.clearPlot()
#plt.xkcd(scale=.6) #randomness=1,length=1,scale=0)

plotter.setupGrid(0.3,'--',
                  -3.0,0.5,3.0,
                  -2.0,1.0,5.1)
plotter.setAxesBounds(-3.1,3.1,-2.1,5.1)
plotter.axesDecorations('Shifted Function',r"$x$",'q,w')
plotter.xAxisLabels(np.arange(-3.0,3.1,0.5),np.arange(-3.0,3.1,0.5))
#plotter.setAspectRation(.8)

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
plt.savefig('trigGraphs_3.pgf',format='pgf')

###############################
plt.close('all')
plotter.setFigure(None,(10,3.5))
plotter.clearPlot()
#plt.xkcd(scale=.6) #randomness=1,length=1,scale=0)

plotter.setupGrid(0.3,'--',
                  -4.0,1.0,4.1,
                  -2.0,1.0,3.1)
plotter.setAxesBounds(-4.1,4.1,-2.1,3.1)
plotter.axesDecorations('Shifted Function',r"$x$",'D')
#plotter.xAxisLabels(np.arange(-4.0,4.1,1.0),np.arange(-2.0,3.1,1.0))
#plotter.setAspectRation(.8)

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
plt.savefig('trigGraphs_4.pgf',format='pgf')

###############################
plt.close('all')
plotter.setFigure(None,(10,3.5))
plotter.clearPlot()
#plt.xkcd(scale=.6) #randomness=1,length=1,scale=0)

plotter.setupGrid(0.3,'--',
                  -4.0,1.0,4.1,
                  -5.0,1.0,1.6)
plotter.setAxesBounds(-4.1,4.1,-5.1,1.6)
plotter.axesDecorations('Shifted Function',r"$x$",'L')
#plotter.xAxisLabels(np.arange(-4.0,4.1,1.0),np.arange(-2.0,3.1,1.0))
#plotter.setAspectRation(.8)

axes = plotter.getAxes()
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.spines['bottom'].set_position(('data',0))
axes.yaxis.set_ticks_position('left')
axes.spines['left'].set_position(('data',0))
axes.xaxis.set_label_coords(0.95, 0.82)
axes.yaxis.set_label_coords(0.45, 0.95)

#plt.show()
plt.savefig('trigGraphs_5.pgf',format='pgf')

