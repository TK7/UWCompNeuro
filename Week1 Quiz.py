# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 21:56:59 2016

@author: Capybara
"""
#Week 1 Python Quiz
#100% - 14/14

import numpy as np
#1
Ac = np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
#2
Amat = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])

B1 = Amat[1:, [0, 2]]
B2 = Amat[[0, 2], 1:]
B3 = Amat[:, :]
B4 = Amat[[0, 2], 2:]

#4
a=np.array([1,2,3,4])
b1 = a[:2]
b2 = a[4:]
b6 = a[:5]
b7 = np.ones(5, )
b8 = np.ones((5, 5))

#5
x2=np.random.rand(100)

#6
#x2[x2>0.5]=1
#7
#x1=(x2 > 0.91).nonzero()[0][:3]
#8
#import pickle
#with open('data.pickle', 'rb') as f:
#    data = pickle.load(f)
#9
datadict = {'a': 3, 'c': 9, 'b': 5}
datadict['b'] = 100

#10
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, step=0.05)
y = np.sin(x**2)
plt.plot(x,y)
plt.show()

#11
x4 = np.array([1,2,3,4,5])
y4=x4**3

#12
x5 = np.array([[1, 2, 3], [2, 3, 4]])
x5 *= 5
x5 -= 1
x5[x5 > 10] = 0
x5 = x5.T

#13
#y = False
#if x in [2, 5, 9]:
#    y = True
#    
#y = x in [2, 5, 9]
#
#if x in [2, 5, 9]:
#    y = True
#else:
#    y = False

#14
x7 = np.arange(5)
y7 = -np.arange(5)
x7[y7 < -2] = 0
import pdb; pdb.set_trace()
x7 *= 9
print(x7)