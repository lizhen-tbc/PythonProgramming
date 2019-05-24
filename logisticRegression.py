# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:28:10 2019

@author: zhen.li
"""
from sklearn import *
import numpy as np
import pandas as pd
from scipy import stats
#from sklearn.datasets import load_iris

iris = sklearn.datasets.load_iris()
X = iris.data[:, :2]
y = (iris.target != 0) * 1

def sigmoid(z):
    return 1/(1 + np.exp(-z))

z = np.dot(x, theta)
h = sigmoid(z)

def loss(h, y):
    return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

gredient = np.dot(X.T, (h - y))/y.shape[0]

