import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df_sorted = df.sort_values(by='km')

def cost_function(df, intercept, slope):
	cost = 0
	for index, row in df.iterrows():
		km = row['km']
		price = row['price']
		cost += (price - (intercept + slope * km)) ** 2
	return cost / len(df)

def gradient_descent(df):
	# Normalize the data
	km_mean = df['km'].mean()
	km_std = df['km'].std()
	price_mean = df['price'].mean()
	price_std = df['price'].std()

	normalized_df = df.copy()
	normalized_df['km'] = (df['km'] - km_mean) / km_std
	normalized_df['price'] = (df['price'] - price_mean) / price_std

	# Start values for the intercept (theta0) and the slope (theta1) of the linear regression
	theta0 = 0.0
	theta1 = 0.0
	threshold = 1e-6
	max_iterations = 10000
	learning_rate = 0.001
	m = len(normalized_df)  # Number of data points
	c = -(1 / m)

	for i in range(max_iterations):
		gradient_theta0 = 0.0
		gradient_theta1 = 0.0

		# Calculate the gradients
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
			break

		theta0 = new_theta0
		theta1 = new_theta1

	# Denormalize the parameters
	theta1_original = theta1 * price_std / km_std
	theta0_original = price_mean + (theta0 * price_std) - (theta1_original * km_mean)

	return theta0_original, theta1_original

# Run gradient descent and get the optimized thetas
theta0, theta1 = gradient_descent(df_sorted)

print('Optimized thetas: ', theta0, theta1)

# Plotting the data points
plt.figure(figsize=(10, 6))
plt.plot(df_sorted['km'], df_sorted['price'], marker='o', linestyle='None', label='Data points')

# Plotting the regression line
x_values = np.linspace(df_sorted['km'].min(), df_sorted['km'].max(), 100)
y_values = theta0 + theta1 * x_values
plt.plot(x_values, y_values, color='red', label='Regression line')

# Adding labels and legend
plt.title('Price vs Kilometers')
plt.xlabel('Kilometers (km)')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
