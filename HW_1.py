# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 21:25:09 2019

@author: grace.kohn
"""

# Import Matplotlib and Numpy packages
import matplotlib.pyplot as plt
import numpy as np

# Generate Inputs (x)
x = np.arange(0, 2*np.pi, 0.2);

# Generate Wave Output (y)
cos_wave = np.cos(x)
sin_wave = np.sin(x)

# Plot waves
plt.plot(x, cos_wave)
plt.plot(x, sin_wave)

# Label Axes
plt.xlabel('x')
plt.ylabel('y')

# Add grid to plot
plt.grid(True, which='both')
plt.axhline(y=0, color='b')

 # Display plot
plt.show()
