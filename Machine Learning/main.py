import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

breast_cancer=datasets.load_breast_cancer()

breast_cancer_X=breast_cancer.data

breast_cancer_X_train=breast_cancer_X[:-30]
breast_cancer_X_test=breast_cancer_X[-30:]

breast_cancer_Y_train=breast_cancer.target[:-30]
breast_cancer_Y_test=breast_cancer.target[-30:]

model=linear_model.LinearRegression()

model.fit(breast_cancer_X_train,breast_cancer_Y_train)
breast_cancer_y_predicted=model.predict(breast_cancer_X_test)

print("Mean squared error is: ",mean_squared_error(breast_cancer_Y_test,breast_cancer_y_predicted))

print("Weights: ",model.coef_)
print("Intercept: ",model.intercept_)

# plt.scatter(breast_cancer_X_test,breast_cancer_Y_test)
# plt.plot(breast_cancer_X_test,breast_cancer_y_predicted)

# plt.show()

# Mean squared error is:  3035.060115291269
# Weights:  [941.43097333]
# Intercept:  153.39713623331644