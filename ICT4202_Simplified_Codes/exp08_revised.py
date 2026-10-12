
# Experiment 8: Supervised Learning - Linear Regression

# NumPy handles numerical data and arrays.
import numpy as np

# Matplotlib is used to draw the graph.
import matplotlib.pyplot as plt

# Import the linear regression algorithm.
from sklearn.linear_model import LinearRegression


# Input feature: study hours.
# Each inner list represents one sample with one feature.
X = np.array([[1], [2], [3], [4], [5], [6]])

# Target values: the observed scores for those study hours.
y = np.array([3, 5, 7, 9, 11, 13])


# Create the model and train it using X and y.
# fit() learns the best-fitting straight line.
model = LinearRegression().fit(X, y)


# Print the slope of the fitted line.
# coef_[0] is the coefficient of the first input feature.
print("Slope:", model.coef_[0])

# Print the intercept, which is the predicted value at X = 0.
print("Intercept:", model.intercept_)

# Predict the score for 7 study hours.
# predict() expects a 2D input array.
print("Prediction for 7 hours:", model.predict([[7]])[0])

# Print the R-squared score on the training data.
# A value of 1 means a perfect fit on these observations.
print("R^2:", model.score(X, y))


# Plot the original observations as points.
# X[:, 0] extracts the study-hour values from the 2D array.
plt.scatter(X[:, 0], y, label="Observed")

# Plot the scores predicted by the fitted regression line.
plt.plot(X[:, 0], model.predict(X), label="Fitted line")

# Add labels to the horizontal and vertical axes.
plt.xlabel("Study hours")
plt.ylabel("Score")

# Display the legend explaining the points and line.
plt.legend()

# Display the graph.
plt.show()
