import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from normalizer import DataNormalizer
from datetime import datetime
import os


# This function adds up all the error (Squared residuals) for the known data points wie have for
# a given slope and intercept. This formula has a minimum, we are searching for.
# Therefor we search the smallest gratient with respect to intercept (theta0) and
# slope (theta1) with the gradient descent algorithm.
def cost_function(df, intercept, slope):
	cost = 0
	for index, row in df.iterrows():
		km = row['km']
		price = row['price']
		cost += (price - (intercept + slope * km)) ** 2
	return cost / len(df)


def gradient_descent(normalized_df):
	# Start values for the intercept (theta0) and the slope (theta1) of the linear regression
	theta0 = 0.0
	theta1 = 0.0
	threshold = 1e-6
	max_iterations = 10000
	learning_rate = 0.001
	m = len(normalized_df)  # Number of data points
	c = -(1 / m)

	for i in range(max_iterations):
		# As required by the subject they are set to 0 before the training.
		gradient_theta0 = 0.0
		gradient_theta1 = 0.0

		# Calculate the gradient for the current choice of theta0 and theata 1 with all
		# the points from the data set.
		for index, row in normalized_df.iterrows():
			km = row['km']
			price = row['price']
			error = price - (theta0 + theta1 * km)
			gradient_theta0 += error
			gradient_theta1 += error * km

		# Average the gradients
		gradient_theta0 *= c
		gradient_theta1 *= c

		# Update the parameters
		new_theta0 = theta0 - learning_rate * gradient_theta0
		new_theta1 = theta1 - learning_rate * gradient_theta1

		# Check for convergence
		if abs(theta0 - new_theta0) < threshold and abs(theta1 - new_theta1) < threshold:
			return new_theta0, new_theta1

		theta0 = new_theta0
		theta1 = new_theta1

	return theta0, theta1

print("Train the model with the data from data.csv...\n")

if not os.path.exists("./data.csv"):
	print('./data.csv does not exist')
	exit(1)

#read the data from the csv into a panda data frame
df = pd.read_csv('data.csv')

# Normalize the training data for efficiency and convergence reasons
nm = DataNormalizer(df)
normalized_data = nm.normalize()

# Run gradient descent and get the optimized normalized thetas
theta0_normalized, theta1_normalized = gradient_descent(normalized_data)

# Denormalize the thetas
theta0, theta1 = nm.denormalize_thetas(theta0_normalized, theta1_normalized)

#Write the optimzed thetas to a file to use them from the prediction
# TODO: Add last updated model
print('Optimized thetas: ', theta0, theta1)
with open('model', 'w') as file:
	file.write('Last model creation: ' + str(datetime.now()) + '\n')
	file.write('\ttheta0=' + str(theta0) + '\n')
	file.write('\ttheta1=' + str(theta1) + '\n')
	file.close()

print("Generating the plots...\n")
# Generate the grid for intercept and slope values. Here linespace creates
# a line from 0 to 20000 with 100 evenly spaced values. 
intercept_values = np.linspace(0, 20000, 100)
slope_values = np.linspace(-0.1, 0.1, 100)
intercept_grid, slope_grid = np.meshgrid(intercept_values, slope_values)

# Compute the cost function for each pair of intercept and slope
cost_values = np.zeros_like(intercept_grid)

for i in range(intercept_grid.shape[0]):
	for j in range(intercept_grid.shape[1]):
		cost_values[i, j] = cost_function(df, intercept_grid[i, j], slope_grid[i, j])

# Plotting the data points
figure = plt.figure(figsize=(14, 8))

# Plot the original data points and regression line
axis1 = figure.add_subplot(2, 2, 1)
axis1.plot(df['km'], df['price'], marker='o', linestyle='None', label='Data points')
x_values = np.linspace(df['km'].min(), df['km'].max(), 100)
y_values = theta0 + theta1 * x_values
axis1.plot(x_values, y_values, color='red', label='Regression line')
axis1.set_title('Price vs Kilometers')
axis1.set_xlabel('Kilometers (km)')
axis1.set_ylabel('Price')
axis1.legend()
axis1.grid(True)

# Plot the normalized data points and regression line
axis2 = figure.add_subplot(2, 2, 3)
axis2.plot(normalized_data['km'], normalized_data['price'], marker='o', linestyle='None', label='Normalized Data points')
x_values_n = np.linspace(normalized_data['km'].min(), normalized_data['km'].max(), 100)
y_values_n = theta0_normalized + theta1_normalized * x_values_n
axis2.plot(x_values_n, y_values_n, color='red', label='Regression line')
axis2.set_title('Normalized: Price vs Kilometers')
axis2.set_xlabel('km')
axis2.set_ylabel('pr')
axis2.legend()
axis2.grid(True)

# Plot the 3D surface of the cost function
axis3 = figure.add_subplot(1, 2, 2, projection='3d')
axis3.plot_surface(intercept_grid, slope_grid, cost_values, cmap='viridis')
axis3.set_xlabel('Intercept')
axis3.set_ylabel('Slope')
axis3.set_zlabel('Cost')
axis3.set_title('Cost Function Surface Plot')

# Display the plot
plt.show()
