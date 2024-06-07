import os
import sys

model_path = './model'


if not os.path.exists(model_path):
	print('Model does not exist. First run <training.py>')
	exit(1)
thetas = {}
with open(model_path, 'r') as file:
	content = file.read()
	lines = content.split('\n')

	for line in lines:
		if "=" in line:
			key, value = line.split("=")
			thetas[key.strip()] = float(value)
	
	file.close()

theta0 = thetas.get("theta0")
theta1 = thetas.get("theta1")

if theta0 == None or theta1 == None:
	print("At least one theta is missing")
	exit(1)

print("Type exit to quit the program")
while (42):
	val = input("\nEnter a milage to estimate the price for: ")
	if val == "exit":
		exit()
	# Attempt to convert the argument to an integer
	try:
		milage = int(val)
		if milage < 0:
				print("Negative milage does not make sense.")
				continue
	except ValueError:
		print("Unable to convert the argument to an integer.")
		continue
	estimated_price = theta0 + milage * theta1
	if estimated_price < 0:
		estimated_price = 0
	print("The estimated price for " + str(milage) + "[km] is: " + str(estimated_price) + "\n")

