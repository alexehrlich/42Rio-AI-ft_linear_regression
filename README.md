# Under construction :)

# ft_linear_regression
This project is about creating simple machine learing model in form of regression line to make predictions of a car price depending on the milage. The first program trains the model by finding the optimal slope and intercept of the regression using the gradient descent algorithm. The second program uses that trained model to make a prediction.

## Preparing the training data
Since the price and the milage values differ immensly in their range, it is necessary to normalize the data to acheive stable and faster convergence of the gradient descent algorithm used later. There are many ways to do that. Two of them are: 
- The Min-Max-Normaliztion is the most intuitive. It maps the values inbetween [0, 1]. Thoug it is not very good in handling outliers.
- The Z-Score-Normalization shifts the mean of the data set to 0 and the standard deviation to 1.

After some research I found out especially for this algorithm the Z-Score-Normalization is the way to do it.

## Training the model with gradient descent

When training a linear regression model, the goal is to find the regression line that best fits the given training data. This means minimizing the sum of the squared errors, which is known as the cost. Different regression lines will yield different costs, as the cost function depends on both the intercept $Θ_0$ and the slope $Θ_1$.

The cost function is defines as:

![lin_reg1](https://raw.githubusercontent.com/alexehrlich/42Rio-AI-ft_linear_regression/main/images/formulas.png)

The objective is to find the values of $Θ_0$ and $Θ_1$ that minimize this cost function. In other words finding the tangent of the cost function being close to 0. By doing so, we ensure that the regression line we obtain is the one that best fits the training data, resulting in the smallest possible sum of squared errors. This can be visualized as follows:

![lin_reg1](https://raw.githubusercontent.com/alexehrlich/42Rio-AI-ft_linear_regression/main/images/cost.png)

Finding the optimal values for $Θ_0$ and $Θ_1$ can be done with gradient descent. To calculate the tangent for the different values for $Θ_0$ and $Θ_1$ we have to do partial derivation with respect to $Θ_0$ and $Θ_1$ - the so called gradients. Applying the chain rule we get those formulas for the gradients:

![lin_reg1](https://raw.githubusercontent.com/alexehrlich/42Rio-AI-ft_linear_regression/main/images/gradients.png)

The algorithm works like this:
1. Set $Θ_0$ and $Θ_1$ to a random value, in our case to 0.
3. Define the learning rate $η$. It defines which set size we apply to the $Θ_0$ and $Θ_1$ to update them during the learning process.
4. Define a threshold for a satisfying convergence and a max iteration limit to stop the algorithm.
5. Compute the current gradients with the formulas from above. (Looks harder than it actually is :) )
6. If both gradients meet the hit the threshold -> Return $Θ_0$ and $Θ_1$ and denormalizethem. Your done :)
7. Else: Update $Θ_0$ and $Θ_1$ with the step size. The step size is the product of the current gradient and the step size. Repeat from step 4.


## Usage
1. Run `training.py`. The $Θ_0$ and $Θ_1$ are safed to a seperate `model` file. The program also plots the data, the normalized data and the cost function.
  ![lin_reg1](https://raw.githubusercontent.com/alexehrlich/42Rio-AI-ft_linear_regression/main/images/plot.png)
2. Run `prediction.py <milage>`. It reads the file and prompts the prediction.
