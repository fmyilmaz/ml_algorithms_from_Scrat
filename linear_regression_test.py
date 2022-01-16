from statistics import linear_regression
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets

X, y = datasets.make_regression(n_samples= 100, n_features= 1, noise= 20, random_state= 4)
X_train, y_train, X_test, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1234)

from linear_regression import LinearRegression

regress = LinearRegression()
regress.fit(X_train, y_train)
predict = regress.predict(X_test)

def mean_squared_error(y_ture, y_predicted):
    return np.mean((y_true - y_predicted) ** 2)


print(mean_squared_error(y_test, predict))