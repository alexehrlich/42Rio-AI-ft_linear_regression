# Under construction :)

# ft_linear_regression
This project is about creating simple machine learing model in form of regression line to make predictions of a car price depending on the milage. The first program trains the model by finding the optimal slope and intercept of the regression using the gradient descent algorithm. The second program uses that trained model to make a prediction.

## Preparing the training data
Since the price and the milage values differ immensly in their range, it is necessary to normalize the data to acheive stable and faster convergence of the gradient descent algorithm used later. There are many ways to do that. Two of them are: 
- The Min-Max-Normaliztion is the most intuitive. It maps the values inbetween [0, 1]. Thoug it is not very good in handling outliers.
- The Z-Score-Normalization shifts the mean of the data set to 0 and the standard deviation to 1.

After some research I found out especially for this algorithm the Z-Score-Normalization is the way to do it.

## Training the model with gradient descent
The training involves finding the regression line which fits the given training data the best, meaning that the squared sum of the errors - the cost - made is at its minimum. For different regression lines, we get different costs. Therefore the cost function depends on the intercept($Θ_0$) and the slope ($Θ_1$):
$$cost(Θ_1, Θ_1) = \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$

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
