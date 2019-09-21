# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:57:07 2019

@author: samsung
"""


import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# A사 입찰가 평균과 표준편자 
A_mean = 0.8
A_std = 0.10 
# B사 입찰가 평균과 표준편자 
B_mean = 0.85
B_std = 0.05

#입찰가 평균 및 표준편차
estim = 0.75
estd = 0.05

x = np.linspace(0.5,1.0,51)

pwin = (1-norm.cdf((x-A_mean)/A_std)) * (1-norm.cdf((x-B_mean)/B_std))

rel = norm.cdf((x-estim)/estd)

profit = pwin*norm.pdf((x-estim)/estd)

max_profit=np.max(profit)
max_index = np.where(max_profit==profit)

print(max_profit,x[max_index],pwin[max_index])

fig = plt.figure()

ax = fig.subplots(1, 1)

ax.plot(x, pwin,
        'r-', lw=5, alpha=0.6, label='Winning Probabilty')

#ax.plot(x, rel,
#        'b-', lw=5, alpha=0.6, label='Reliability')

ax.plot(x, profit,
        'g-', lw=5, alpha=0.6, label='Profit')

plt.show()
