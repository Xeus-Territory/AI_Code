import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from regex import R

def prod(w, X):
   return np.dot(w.T, X)


def sigmoid(s):
   return 1 / (1 + np.exp(-s))


def my_logistic_sigmoid_regression(X, y, w_init, eta, epsilon=1e-3, M=10000):
   w = [w_init]
   N = X.shape[1]
   d = X.shape[0]
   count = 0
   check_w_after = 20
   while count < M:
       # mix data
       mix_id = np.random.permutation(N)
       for i in mix_id:
           xi = X[:, i].reshape(d, 1)
           yi = y[i]
           zi = sigmoid(np.dot(w[-1].T, xi))
           w_new = w[-1] + eta * (yi - zi) * xi
           count += 1
           # stopping criteria
           if count % check_w_after == 0:
               if np.linalg.norm(w_new - w[-check_w_after]) < epsilon:
                   return w
           w.append(w_new)
   return w

# method display
# def display(w):
#    # old
#    # X0 = X[0, np.where(y == 0)][0]
#    # new
#    X0 = X[0, np.where(y == 0)][0]
#    y0 = y[np.where(y == 0)]
#    # old
#    # X1 = X[0, np.where(y == 1)][0]
#    X1 = X[0, np.where(y == 1)][0]
#    y1 = y[np.where(y == 1)]

#    plt.plot(X0, y0, 'ro', markersize=8)
#    plt.plot(X1, y1, 'bs', markersize=8)
#    xx = np.linspace(0, 6, 1000)
#    w0 = w[-1][0][0]
#    w1 = w[-1][1][0]
#    threshold = -w0 / w1
#    yy = sigmoid(w0 + w1 * xx)
#    plt.axis([-2, 8, -1, 2])
#    plt.plot(xx, yy, 'g-', linewidth=2)
#    plt.plot(threshold, .5, 'y^', markersize=8)
#    plt.xlabel('studying hours')
#    plt.ylabel('predicted probability of pass')
#    plt.show()


if __name__ == '__main__':
   print("ok")
   # data:
   data = pd.read_csv('input.csv')
   data_ = pd.read_csv('output_04 .csv')
   print(data["Labeling"].unique())
   conditions = ["Iris-setosa", "Iris-versicolor"]
   values = [0, 1]
   data["Labeling"] = data["Labeling"].replace(conditions, values)
   sepal_length = data['sepal_length'].values
   sepal_width = data['sepal_width'].values
   petal_length = data['petal_length'].values
   petal_width = data['petal_width'].values
   X = np.array([sepal_length, sepal_width, petal_length, petal_width])
   y = data["Labeling"].values
   print(X)
   print(y)
   Xbar = np.concatenate((np.ones((1, X.shape[1])), X), axis=0)
   epsilon = .05
   d = Xbar.shape[0]
   w_init = np.random.randn(d, 1)
   w = my_logistic_sigmoid_regression(Xbar, y, w_init, epsilon)
   print(w[-1].T)
   yi = sigmoid(np.dot(w[-1].T, Xbar))
   print(yi)
   
   X_pred = np.array([data_['sepal_length'].values, data_['sepal_width'].values, data_['petal_length'].values, data_['petal_width'].values])
   print(X_pred)
   Xbar = np.concatenate((np.ones((1, X_pred.shape[1])), X_pred), axis=0)
   yi = sigmoid(np.dot(w[-1].T, Xbar))
   result = []
   for i in yi[0]:
         if i >= 0.5:
               result.append(1)
         else:
               result.append(0)
   
   print(result)
   #display(w)