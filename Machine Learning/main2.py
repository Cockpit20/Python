import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

diabetes=datasets.load_diabetes()

diabetes_X=np.array([[1],[2],[3]])

diabetes_X_train=diabetes_X
diabetes_X_test=diabetes_X

diabetes_Y_train=np.array([[1],[2],[3]])
diabetes_Y_test=np.array([[1],[2],[3]])

model=linear_model.LinearRegression()

model.fit(diabetes_X_train,diabetes_Y_train)
diabetes_y_predicted=model.predict(diabetes_X_test)

print("Mean squared error is: ",mean_squared_error(diabetes_Y_test,diabetes_y_predicted))

print("Weights: ",model.coef_)
print("Intercept: ",model.intercept_)

plt.scatter(diabetes_X_test,diabetes_Y_test)
plt.plot(diabetes_X_test,diabetes_y_predicted)

plt.show()

# Mean squared error is:  3035.060115291269
# Weights:  [941.43097333]
# Intercept:  153.39713623331644