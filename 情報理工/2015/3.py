import math
import numpy as np
import matplotlib.pyplot as plt

MAX_R = 3
fig = plt.figure(figsize=(15, 15))
fig.suptitle("Problem 3", fontsize=20)


# 直交座標表示
ax1 = plt.subplot(221)
ax1.set_aspect("equal")
raw_x = np.linspace(-MAX_R, MAX_R, 500 + 1)
raw_y = np.linspace(-MAX_R, MAX_R, 500 + 1)
x, y = np.meshgrid(raw_x, raw_y)
dxdt = x - y - x * (x**2 + y**2) + (x * y) / (np.sqrt(x**2 + y**2))
dydt = x + y - y * (x**2 + y**2) - (x * x) / (np.sqrt(x**2 + y**2))
ax1.streamplot(x=x, y=y, u=dxdt, v=dydt, color="deepskyblue", density=1.5)
ax1.set_xlim(-MAX_R, MAX_R)
ax1.set_ylim(-MAX_R, MAX_R)
ax1.set_title("flow in cartesian coordinate")

# 極座標表示
ax2 = plt.subplot(222, projection="polar")
raw_r = np.linspace(0, MAX_R, 100 + 1)
raw_p = np.linspace(-math.pi, math.pi, 360 * 10 + 1)
r, p = np.meshgrid(raw_r, raw_p)
drdt = r - r**3
dpdt = 1 - np.cos(p)
ax2.streamplot(x=p.T, y=r.T, u=dpdt.T, v=drdt.T, color="limegreen", density=1.5)
ax2.set_ylim(0, MAX_R)
ax2.set_title("flow in polar coordinate")

# r-t graph
ax3 = plt.subplot(223)
t = np.linspace(0, 10, 1000)
for r0 in [0.5, 1, 1.5, 2, 2.5, 3]:
    r = np.sqrt(1 / ((1 / (r0**2) - 1) * np.exp(-2 * t) + 1))
    ax3.plot(t, r, label=f"r0:{r0}")
ax3.set_xlabel("t")
ax3.set_ylabel("r")
ax3.legend()
ax3.set_title("r-t graph")

# p-t graph
ax4 = plt.subplot(224)
t = np.linspace(0, 10, 1000)
for _p0 in range(8):
    p0 = math.pi / 8 * _p0
    p = 2 * np.arctan(1 / (-t + 1 / np.tan(p0 / 2)))
    ax4.plot(t, p, label=f"p0:{_p0}π/8")
ax4.set_xlabel("t")
ax4.set_ylabel("p")
ax4.legend()
ax4.set_title("p-t graph")

plt.tight_layout()

# plt.show()
plt.savefig("情報理工/2015/3.png")
