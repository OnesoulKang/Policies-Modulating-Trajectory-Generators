import numpy as np
import matplotlib.pyplot as plt

### make a reference trajectory
from math import pi, cos, sin
theta = np.arange(-0.1, 2*pi, 0.1)

traj1 = []
r1 = 0.1
for t in theta:
    traj1.append((r1 * cos(t) - r1, r1 * sin(t)))

traj2 = []
r2 = 0.5
for t in theta:
    traj2.append((r2 * cos(t+pi) + r2, r2 * sin(t+pi)))

ref_traj = np.vstack((traj1, traj2))    
x, y = zip(*ref_traj)
plt.plot(x,y)
plt.show()