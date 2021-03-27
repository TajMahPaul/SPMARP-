import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression

def main():
    # (Time, kms)
    data = [
        (12,9), (9,6.7), (16, 11.6), (11, 10.7), (19, 16.3), (13, 12), (19, 16.7), (17, 12), (16, 13.1), (12, 8.1),
        (13,9.9), (14, 12.5), (20, 18.4), (23, 20.2), (3, 2), (11, 8.4), (7, 4.1), (9, 6.1), (14, 11.2), (18, 13.7),
        (21, 16.5), (11, 8.2), (8, 5.7), (9, 6.0), (7, 4.2), (16, 13.4), (19, 17.9), (16, 15.8), (19, 15.2), (6, 4.4)
    ]
    X = []
    Y = []
    for d in data:
        X.append(d[1])
        Y.append(d[0])
    X = np.array(X).reshape(-1, 1)
    Y = np.array(Y).reshape(-1, 1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X) 
    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    
    # The coefficients
    print('Coefficient: \n', linear_regressor.coef_)
    print('Intercept: \n', linear_regressor.intercept_)
    plt.ylabel("Time (min)")
    plt.xlabel("Distance (km)")
    plt.title('Linear regression: Time vs Distance in Surrey')
    plt.show()
if __name__ == "__main__":
    main()