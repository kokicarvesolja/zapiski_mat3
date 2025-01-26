#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr

# primer singularne rešitve, primer 7.17

def singularna(x, C):
    return np.cosh(x - C)

c_vrednosti = [-1, 0, 1]
c1, c2, c3, c4, c5 = cmr.take_cmap_colors('cmr.chroma', 5, cmap_range = (.3, .9),
                                   return_fmt='hex')

x = np.linspace(-4, 10, 1000)

fig, ax = plt.subplots()

#plottanje treh vrednosti za C=-1, 0, 1
for vrednost, col in zip(c_vrednosti, [c1, c2, c3]):
    ax.plot(x, singularna(x, vrednost), color=col,
            label=f'C = {vrednost}', zorder=2)

# drawing C_0
ax.plot(x, singularna(x, 5), color=c5, label=r'$C = C_0$', zorder=2)
#singularna rešitev
ax.hlines(1, -4, 10, color=c4, label='singularna rešitev', zorder=1)
# hiding tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])
# hiding tick marks
ax.set_xticks([])
ax.set_yticks([])

# drawing x=0
ax.vlines(0, 0, 5, color='k', zorder=3, alpha=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_ylim(bottom=0, top=5)

ax.legend()
ax.set_title(r'Splošne in singularna rešitev $\mathrm{ch}(x - C)$')
fig.tight_layout()
fig.savefig('./figures/singularna.png')
plt.close()
# Clairautova singularna rešitev, primer 7.11

fig1, ax1 = plt.subplots()
d1, d2, d3, d4, d5, d6 = cmr.take_cmap_colors('cmr.chroma', 6,
                                              cmap_range = (.3, .9),
                                              return_fmt='hex')
def clair(x, C):
    return C * (x + C)

def clair_sing(x):
    return - (x ** 2) / 4

d_vrednosti = np.array([2, 1, 0, 1/2, 1/4])
x2 = np.linspace(-5, 5, 1000)

for i, c in zip(d_vrednosti, [d6, d2, d3, d4, d5]):
    ax1.plot(x2, clair(x2, i), color=c, label=rf'D = $\pm$ {i}')

for i, c in zip(- d_vrednosti, [d6, d2, d3, d4, d5]):
    ax1.plot(x2, clair(x2, i), color=c)

# drawing singularno rešitev
ax1.plot(x2, clair_sing(x2), color=d1, label='singularna rešitev')
# hiding tick labels
ax1.set_yticklabels([])
ax1.set_xticklabels([])
# hiding tick marks
ax1.set_xticks([])
ax1.set_yticks([])

# drawing x=0
ax1.vlines(0, -6, 15, color='k', zorder=3, alpha=0.5)
ax1.hlines(0, -5, 5, color='k', zorder=3, alpha=0.5)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
# other miscs
ax1.legend()
ax1.set_title(r"Rešitev Clairautove enačbe $y = xy' + y' ^2$")
fig1.tight_layout()
fig1.savefig('./figures/clair.png')
plt.close()

# Eksponentna spirala, primer 7.5

# redefining x2

x2 = np.linspace(-5, 5, 1000)
phi = np.linspace(0, 10 * np.pi, 1000)

def spirala(x, D=0.1):
    return np.exp(x) * D

fig, ax = plt.subplots()

ax.plot(spirala(x2) * np.cos(phi), spirala(x2) * np.sin(phi), color=d1)
ax.plot(x2, x2, color=d6, label='ni definirano')
ax.legend()
# hiding tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])
# hiding tick marks
ax.set_xticks([])
ax.set_yticks([])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Eksponentna spirala')
fig.tight_layout()
fig.savefig('./figures/eksp_spirala.png')
plt.close()


# primer 154

def resitev(x, D, l=2):
    return np.sinh(D) * ( x + l / np.cosh(D))

def star(x, l=2):
    return np.sign(l) * (np.abs(l)) **(2/3) \
        - np.sign(x) * (np.abs(x)) **(2/3)

# redefining x2

x2 = np.linspace(-5, 5, 1000)
start = 0.1
stop = 5
step = 0.15
print(int((stop - start) / step))
# colors
colors = cmr.take_cmap_colors('cmr.gem', int((stop - start) / step),
                              cmap_range = (.3, .9),
                              return_fmt='hex')
fig, ax = plt.subplots()

ax.plot(x2, star(x2), color='r', zorder=10)

for d, e in zip(np.arange(start, stop, step=step), colors):
    zvezda = resitev(x2, d)
    x2 = x2[zvezda > 0]
    zvezda = zvezda[zvezda > 0]
    zvezda = zvezda[x2 < 0]
    x2 = x2[x2 < 0]
    ax.plot(x2, zvezda)
    ax.plot(-x2, zvezda)
    ax.plot(-x2, -zvezda)
    ax.plot(x2, -zvezda)


ax.hlines(0, -2.5, 2.5, color='k', zorder=10, alpha=0.5)
ax.vlines(0, -2, 2, color='k', zorder=10, alpha=0.5)

# miscs
ax.set_ylim(-2, 2)
ax.set_xlim(-2.5, 2.5)
# hiding tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])
## hiding tick marks
ax.set_xticks([])
ax.set_yticks([])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Rešitev enačbe')
fig.tight_layout()
fig.savefig('./figures/resitev_enacbe.png')
plt.close()
