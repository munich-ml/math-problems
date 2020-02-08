# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:06:03 2019

@author: holge
"""

import math
import numpy as np
import matplotlib.pyplot as plt


def angles_to_cartesian(angles):
    """
    Converts polar angles (assumes radius 1) to cartesian x, y coordinates.

    Parameters
    ----------
    angles : list
        angles in degrees

    Returns
    -------
    xs : list
        cartesian x coordinates
    ys : list
        cartesian x coordinates
    """    
    xs = [math.cos(angle/180*math.pi) for angle in angles]
    ys = [math.sin(angle/180*math.pi) for angle in angles]
    return (xs, ys)    


def cartesian_to_angular(x, y):
    """
    Converts a pair of cartesian x, y coordinates to a radius with angle
    """    
    angle = 180/math.pi * math.atan(y/x)
    radius = math.sqrt(x*x + y*y)
    return (radius, angle)    


fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)

# draw circle with radius 1
cx, cy = angles_to_cartesian(np.arange(0, 360, 0.1))
ax.plot(cx, cy, "k-", label="circle 1")

# draw angular samples
angles = [45, 315]
xs, ys = angles_to_cartesian(angles)
ax.plot(xs, ys, "bo", label="angles")

# compute and plot mean
mx = np.array(xs).mean()
my = np.array(ys).mean()

ax.plot(mx, my, "rD", label="mean")
ax.plot((0, mx), (0, my), "r-")
print("radius = {:.2f}, mean angle = {:.1f}°".format(*cartesian_to_angular(mx, my)))

# beautify plot
ax.grid(True)
SCALE = 1.2
ax.set(title="", xlabel='x', ylabel="y", xlim=(-SCALE, SCALE), ylim=(-SCALE, SCALE))   
ax.legend()
plt.show()
