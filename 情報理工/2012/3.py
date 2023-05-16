import matplotlib.pyplot as plt
import numpy as np

LAMBDA = 3
A = 10.0
B = 2.0
maxN = 15
timeStep = 100
timeLen = 2
dt = 1 / timeStep

N = np.arange(0, maxN, 1, dtype=np.int64)
P = (
    np.exp(-LAMBDA)
    * np.power(LAMBDA, N)
    / np.array([np.math.factorial(i) for i in range(maxN)])
).tolist()
Ps = [P]

for t in range(timeLen * timeStep):
    newP = [0 for _ in range(maxN)]
    for n in range(maxN):
        if n + 1 < maxN:
            newP[n + 1] += P[n] * A * dt
        if n - 1 >= 0:
            newP[n - 1] += P[n] * n * B * dt
        newP[n] += (1 - A * dt - n * B * dt) * P[n]
    Ps.append(newP)
    P = newP
Ps = np.array(Ps)

for t in range(0, timeLen * timeStep, timeLen * timeStep // 20):
    Mt = A / B + (LAMBDA - A / B) * np.exp(-B * (t / timeStep))
    analysis = [Mt**n / np.math.factorial(n) * np.exp(-Mt) for n in range(maxN)]
    plt.plot(
        N,
        Ps[t],
        label="simulation",
        linestyle="dashed",
        marker="o",
        markersize=3,
        linewidth=0.5,
        alpha=0.5,
        color="red",
    )
    plt.plot(
        N,
        analysis,
        label="analytical",
        linestyle="dashed",
        marker="o",
        markersize=3,
        linewidth=0.5,
        alpha=0.5,
        color="blue",
    )

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())
plt.title("Poisson Process")
plt.savefig("3.png")
