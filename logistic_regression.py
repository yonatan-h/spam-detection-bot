import numpy as np
import matplotlib.pyplot as plt



class LogisticRegression:
    #0.1 500000
    #277 39 0.1 10000 500+500
    def __init__(self, learning_rate=0.1, num_iter=10000, w=None, num_features=1):
        self.learning_rate = learning_rate
        self.num_iter = num_iter
        if (w is not None): self.w = w
        else: self.w = np.zeros(num_features)
        
        self.b = 0
    
    def _sigmoid(self, num):
        return 1 / (1 + np.exp(-num))
    
    def fit(self, X, y):
        if y.size == 0:
            raise ValueError('y cannot be empty')
        for i in range(self.num_iter):
            print('Logistic regression fitting for the ', i, 'th time')
            errors = self.predict(X) - y 
            gradients = np.dot(errors, X)/y.size

            self.w -= self.learning_rate * gradients
            self.b -= self.learning_rate * np.sum(errors) / y.size
    
    def predict(self, X):
        weighted_sums = np.dot(self.w, X.T) + self.b
        y_predicteds = self._sigmoid(weighted_sums)
        return y_predicteds
    
    def predict_solid(self, X):
        y_predicteds = np.where (self.predict(X) > 0.5, 1, 0)
        return y_predicteds
    
    def measure_error(self, X, y):
        return np.sum(np.abs(self.predict(X) - y)) / y.size


