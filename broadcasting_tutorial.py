# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:15:39 2020

@author: Chase
"""

# broadcasting example
import numpy as np
logit = np.random.rand(1,4)
logit2 = np.random.rand(3,4)

test = logit * logit2
testmin = np.amin(test,axis=1)

# for loop method

test2 = np.zeros((2,4))
# loop through the (2,1) array, starting with logit[0,0]
for i in range(len(logit)):
    # loop through the (2,4) array, staring with logit2[0,0]
    for j in range(logit2.shape[1]):
        test2[i,j] = logit[i]*logit2[i,j]