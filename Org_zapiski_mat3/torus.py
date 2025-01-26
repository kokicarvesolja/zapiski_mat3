#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

kot = np.linspace(0, 2 * np.pi, 100)
r = 1

U, V = np.meshgrid(kot, kot)

#print(len(kot), len(r))

x_koord = (5 + r * np.cos(V)) * np.cos(U)
y_koord = (5 + r * np.cos(V)) * np.sin(U)
z_koord = r * np.sin(V)


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x_koord, y_koord, z_koord, antialiased=True)
ax.set_zlim(-3, 3)

fig.savefig('torus.png')
plt.close
