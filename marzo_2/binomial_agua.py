# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:05:31 2023

@author: b12s301e19
"""

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

X = stats.binom(n = 21, p = 1/3)
x = np.arange(0,22)

# P(X = 3)
P_4 = X.pmf(4)
print("P(X=4) = ", P_4)


# P(X = 3)
P_ge_10 = 1 - X.cdf(9)
print("P(X>=10) = ", P_ge_10)

# PMF
PMF = X.pmf(x)

P2_ge_10 = sum(PMF[10:])
print("P(X>=10) = ", P2_ge_10)

CDF = X.cdf(x)
print(x)
print(PMF)

plt.plot(x, CDF, 'rs', ms=10)
plt.vlines(x, 0, CDF, colors='r', lw = 5, alpha=0.5)
plt.xlabel("Numero de estudiantes que identifica correctamente el tipo de agua del baso")
plt.ylabel("Probabilidad")
