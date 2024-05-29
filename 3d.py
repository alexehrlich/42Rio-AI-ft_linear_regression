import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Your data
km = np.array([240000, 139800, 150500, 185530, 176000, 114800, 166800, 89000, 144500, 84000, 82029, 63060, 74000, 97500, 67000, 76025, 48235, 93000, 60949, 65674, 54000, 68500, 22899, 61789])
price = np.array([3650, 3800, 4400, 4450, 5250, 5350, 5800, 5990, 5999, 6200, 6390, 6390, 6600, 6800, 6800, 6900, 6900, 6990, 7490, 7555, 7990, 7990, 7990, 8290])

# Define the cost function (sum of squared residuals)
def cost_function(a, b, x, y):
    m = len(y)
    total_error = 0
    for i in range(m):
        total_error += (a * x[i] + b - y[i]) ** 2
    return total_error / m

# Create a grid of a and b values
a_values = np.linspace(-0.1, 0.1, 100)
b_values = np.linspace(-5000, 5000, 100)
A, B = np.meshgrid(a_values, b_values)

# Calculate the cost function for each combination of a and b
costs = np.zeros_like(A)
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        costs[i, j] = cost_function(A[i, j], B[i, j], km, price)

# Plot the 3D surface
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A, B, costs, cmap='viridis')

# Add labels and title
ax.set_title('Cost Function Surface')
ax.set_xlabel('Parameter a')
ax.set_ylabel('Parameter b')
ax.set_zlabel('Cost')

plt.show()
