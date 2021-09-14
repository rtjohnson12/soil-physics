
# Bundle of Capillaries
from vpython import *
import numpy as np
from math import sqrt

from IPython.display import display

display(background = color.white)

n = 100
x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)
r = np.zeros(n)

for i in range(n):
    check = 0
    while(check == 0):
        x[i] = random() - 0.5
        z[i] = random() - 0.5
        check = 1
        for j in range(i):
            if ((x[i] - x[j])**2. + (z[i] - z[j])**2. < r[j]**2.):
                check = 0
        if not (x[i]**2. + z[i]**2. < 0.2**2.): check = 0
        r[i] = ((random()*4 - 2)**2. + 0.5)/4*0.1
        for j in range(i):
            if ((x[i] - x[j])**2. + (z[i] - z[j])**2. < (r[j] + r[i])**2.):
                r[i] = sqrt((x[i] - x[j])**2. + (z[i] + z[j])**2.) - r[j]
    for i in range(n):
        cylinder(pos = vector(x[i], -.5, z[i]), axis = vector(0, 2, 0), radius = r[i])


