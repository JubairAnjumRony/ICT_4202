# Experiment 8: Supervised Learning - Linear Regression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([3, 5, 7, 9, 11, 13])

model = LinearRegression().fit(X, y)
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Prediction for 7 hours:", model.predict([[7]])[0])
print("R^2:", model.score(X, y))

plt.scatter(X[:, 0], y, label="Observed")
plt.plot(X[:, 0], model.predict(X), label="Fitted line")
plt.xlabel("Study hours")
plt.ylabel("Score")
plt.legend()
plt.show()
