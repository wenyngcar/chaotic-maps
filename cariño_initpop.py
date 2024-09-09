%matplotlib widget
import matplotlib.pyplot as plt
import math

population_size = 500

lb_x = -10.0
ub_x = 50
lb_y = -1.0
ub_y = 10.0

init_x = 0.30
init_y = 0.80

def f(x, y):
    return (math.sin(3 * math.pi * x)**2) + (x - 2)**2 * (1 + math.sin(3 * math.pi * y)**2) + (y - 1)**2 * (1 + math.sin(2 * math.pi * y)**2)

def generate_value(lb, ub, chaotic):
    return lb + (ub - lb) * chaotic

# Function for Sinusoidal Map
def sinusoidal_map(init_x, init_y):
    def sinusoidal(x):
        return math.sin(math.pi * x)
    
    sinusoidal_series_x = []
    sinusoidal_series_y = []

    populate_solution(sinusoidal, sinusoidal_series_x, sinusoidal_series_y, init_x, init_y)
    plot_solution(sinusoidal_series_x, sinusoidal_series_y)

# Function for Logistic Map
def logistic_map(init_x, init_y):
    def logistic(x):
        return 4*x*(1-x)
    
    logistic_series_x = []
    logistic_series_y = []

    populate_solution(logistic, logistic_series_x, logistic_series_y, init_x, init_y)
    plot_solution(logistic_series_x, logistic_series_y)

# Populating the list (<chaotic map> series) of each Chaotic Map.
def populate_solution(chaotic_formula, series_x, series_y, init_x, init_y):
    series_x.append(init_x)
    series_y.append(init_y)
    
    for i in range(population_size):
        series_x.append(chaotic_formula(series_x[i]))
        series_y.append(chaotic_formula(series_y[i]))

# For graph
def plot_solution(series_x, series_y):
    xline = []
    yline = []
    zline = []

    for i in range(population_size):
        xline.append(generate_value(lb_x, ub_x, series_x[i]))
        yline.append(generate_value(lb_y, ub_y, series_y[i]))
        zline.append(f(xline[i],yline[i]))

    axl = plt.axes(projection='3d')
    axl.scatter3D(xline, yline, zline, c = zline, cmap = 'hot', s = 7)
    axl.set_xlabel('x')
    axl.set_ylabel('y')
    axl.set_zlabel('f')

