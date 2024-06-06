# ft_linear_regression
This project is about creating simple machine learing model in form of regression line to make predictions of a car price depending on the milage. The first program trains the model by finding the optimal slope and intercept of the regression using the gradient descent algorithm. The second program uses that trained model to make a prediction.

## Training the model with gradient descent
The training involves finding the regression line which fits the given training data the best, meaning that the squared sum of the errors - the cost - made is at its minimum. The cost function therefore is: 
$$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2
$$

The regression line is described by $estimated price(km) = Θ_0 + Θ_1 * km$.
The minimal cost is determined with the gradient descent algorithm by testing different values for $Θ_0$ and $Θ_1$. 

The algorithm works as follows:
- Set $Θ_0$ and $Θ_1$ to 0.

## Installation

Provide step-by-step instructions on how to install and set up your project. Include any prerequisites or dependencies needed.

```bash
# Example installation commands
git clone https://github.com/yourusername/yourproject.git
cd yourproject
npm install
