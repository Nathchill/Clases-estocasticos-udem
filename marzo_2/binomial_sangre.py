# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:31:25 2023

@author: b12s301e19
"""

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
Definición de la VA binomial: X ~ Bin(n,p)

X: Numero de hijos con sangre tipo O
- n: Numero de hijos
- p: 0.25
- q: 1 - p = 0.75
"""

X = stats.binom(n = 5, p = 0.25)
x = [0, 1, 2, 3, 4, 5]

# P(X = 3)
P_3 = X.pmf(k = 3)
print("P_3 = ", P_3)

"""
--------------------------- P(X>3) -------------------------
"""
# P(X = 4)
P_4 = X.pmf(k = 4)
# P(X = 5)
P_5 = X.pmf(k = 5)

P_mayor3 = P_4 + P_5
print("P(X>3) = ", P_mayor3)


# --------------------------- PFM

pmf = X.pmf(k = x)
print(x)
print(pmf)

# GRafica
plt.plot(x, pmf, 'bs', ms=10)
plt.vlines(x, 0, pmf, colors='b', lw = 5, alpha=0.5)
plt.xlabel("Numero de hijos con sangre tipo O")
plt.ylabel("Probabilidad")


# --------------------------- PFM Acumulada

pfa = X.cdf([0, 1, 2, 3, 4, 5])
print(x)
print(pfa)
plt.figure()

plt.plot(x, pfa, 'rs', ms=10)
plt.vlines(x, 0, pfa, colors='r', lw = 5, alpha=0.5)
plt.xlabel("Numero acumulado de hijos con sangre tipo O")
plt.ylabel("Probabilidad")

P2_mayor3 = 1 - pfa[3]
print("Forma 2: P(X>3) = ", P2_mayor3)