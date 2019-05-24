# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:08:26 2019

@author: zhen.li
"""

class LogisticRegression:
    def _init_(self, lr = 0.01, num_iter = 100000, fit_intercept = True, verbose = False):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        
    def _add_intercept(self, x):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis = 1)
    
    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def _loss(self, h, y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()
    
    def fit(self, X, y):
        if self.fit_intercept:
            X = self._add_intercept(X)
            
        self.theta = np.zeros(X.shape[1])
        
        for i in range(self. num_iter):
            z = np.dot(X, self.theta)
            h = self._sigmoid(z)
            gradient = np.dot(X.T, (h - y)/y.size)
            self.theta -= self.lr * gradient
            
            if (self.verbose == True and i % 10000 == 0):
                z = np.dot(X, self.theta)
                h = self._sigmoid(z)
                print(f'loss:{self._loss(h, y)}\t')
    
    def predict_prob(self, X):
        if self.fit_intercept:
            X = self._add_intercept(X)
        return self._sigmoid(np.dot(X, self.theta))

    def predict(self, X, threshold):
        return self.predict_prob(X) >= threshold        
        