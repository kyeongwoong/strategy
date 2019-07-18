# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:57:07 2019

@author: samsung
"""


import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


fig, ax = plt.subplots(1, 1)

#mean, var, skew, kurt = norm.stats(moments='mvsk')
#x = np.linspace(norm.ppf(0.01),
#                norm.ppf(0.99), 100)
#ax.plot(x, norm.cdf(x),
#        'r-', lw=5, alpha=0.6, label='norm pdf')

A_mean = 0.8
A_std = 0.10 
B_mean = 0.9
B_std = 0.10

estim = 0.75
estd = 0.10

x = np.linspace(0.5,1.0,51)

pwin = (1-norm.cdf((x-A_mean)/A_std)) * (1-norm.cdf((x-B_mean)/B_std))

rel = norm.cdf((x-estim)/estd)

profit = pwin*norm.pdf((x-estim)/estd)

print(x,profit)

ax.plot(x, pwin,
        'r-', lw=5, alpha=0.6, label='Winning Probabilty')
ax.plot(x, rel,
        'b-', label='Reliability')
ax.plot(x, profit,
        'g-', label='Profit')
