import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import random
import numpy as numpy

population_size = 1000

lb_x = -5.0
ub_x = 5.0
lb_y = -10.0
ub_y = 10.0

def f(x, y):
    return ((x**4 - 16*x**2 + 5*x)/2) + ((y**4 - 16*y**2 + 5*y)/2)

def generate_value(lb, ub):
    return lb + (ub - lb) * random.random()

xline = []
yline = []
zline = []

# Generate pseudo-random values for x and y
for i in range(population_size):
    xline.append(generate_value(lb_x, ub_x))
    yline.append(generate_value(lb_y, ub_y))
    zline.append(f(xline[i], yline[i]))

xline = numpy.array(xline)
yline = numpy.array(yline)
zline = numpy.array(zline)

axl = plt.axes(projection='3d')
axl.scatter3D(xline, yline, zline, c=zline, cmap='hot', s=7)
axl.set_xlabel('x')
axl.set_ylabel('y')
axl.set_zlabel('z')

plt.savefig("3d_plot.png")