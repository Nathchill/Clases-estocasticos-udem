# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:35:10 2023

@author: b12s301e19
"""


import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


"""
X ~ Geom(p)

X: Numero de personas que ve el supertazon

Parametros:
p = 0.4
"""

X = stats.geom(p = 0.4)

# d
media = X.mean()
print("Media =",media)

# e
P7 = X.pmf(7)
print("P(X=7) =", P7)


# e
P3_o_4 = sum(X.pmf([3, 4]))
print("P(X = 3 o X = 4) =", P3_o_4)

# PFM
x = np.arange(0,21)
PFM = X.pmf(x)

print(x)
print(PFM)


# GRafica
plt.plot(x, PFM, 'bs', ms=10)
plt.vlines(x, 0, PFM, colors='b', lw = 5, alpha=0.5)
plt.xlabel("Numero personas que ven el supertazon")
plt.ylabel("Probabilidad")



