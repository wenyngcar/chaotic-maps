%matplotlib qt

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import random
import numpy as np

population_size = 1000

lb_x = -5.0
ub_x = 5.0
lb_y = -10.0
ub_y = 10.0

def f(x, y):
    return ((x**4 - 16*x**2 + 5*x)/2) + ((y**4 - 16*y**2 + 5*y)/2)

def logistic(x):
    return 4*x*(1-x)

def generate_value(lb, ub, chaotic):
    return lb + (ub - lb) * chaotic

logistic_series_x = []
logistic_series_y = []

x = 0.30
y = 0.80

logistic_series_x.append(x)
logistic_series_y.append(y)

for i in range(population_size):
    next_in_series = logistic(logistic_series_x[i])
    logistic_series_x.append(next_in_series)

for i in range(population_size):
    next_in_series = logistic(logistic_series_y[i])
    logistic_series_y.append(next_in_series)

xline = []
yline = []
zline = []

for i in range(population_size):
    value = generate_value(lb_x, ub_x, logistic_series_x[i])
    xline.append(value)

for i in range(population_size):
    value = generate_value(lb_y, ub_y, logistic_series_y[i])
    yline.append(value)

for i in range(population_size):
    zline.append(f(xline[i], yline[i]))

axl = plt.axes(projection='3d')
axl.scatter3D(xline, yline, zline, c=zline, cmap='hot', s=7)
axl.set_xlabel('x')
axl.set_ylabel('y')
axl.set_zlabel('f')
