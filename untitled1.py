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