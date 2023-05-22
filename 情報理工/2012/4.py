import matplotlib.pyplot as plt
import random
import numpy as np
from tqdm import tqdm


def g_0(x1, x2):
    return -3 * x1 * x1 + 4 * x1 * x2 + 2 * x2 * x2


def g_1(x1, x2):
    return -2 * x1 * x1 - 2 * x1 * x2 - x2 * x2 + 4


def g_2(x1, x2):
    return x1 * x1 - 1


def solve():
    ans = -1e9
    best_x1 = 0
    best_x2 = 0
    for _ in tqdm(range(int(1e5))):
        x1 = random.random() * 10 - 5
        x2 = random.random() * 10 - 5
        if g_1(x1, x2) >= 0 and g_2(x1, x2) >= 0:
            ans = max(ans, g_0(x1, x2))
            if ans == g_0(x1, x2):
                best_x1 = x1
                best_x2 = x2
    print(f"ans: {ans} x1: {best_x1} x2: {best_x2}")

    x1 = np.linspace(-5, 5, 1000)
    x2 = np.linspace(-5, 5, 1000)
    X1, X2 = np.meshgrid(x1, x2)

    Z = g_0(X1, X2)
    Z[g_1(X1, X2) < 0] -= 100
    Z[g_2(X1, X2) < 0] -= 100
    plt.imshow(Z, extent=[-5, 5, -5, 5], origin="lower")
    plt.title("visualization of problem")
    plt.savefig("4_vis.png")
    plt.close()

    Z[g_1(X1, X2) < 0] = np.nan
    Z[g_2(X1, X2) < 0] = np.nan
    plt.imshow(Z, extent=[-5, 5, -5, 5], origin="lower")
    plt.colorbar()
    plt.title("maximize g_0 s.t. g_1 >= 0, g_2 >= 0")
    plt.savefig("4_actual.png")
    plt.close()


def solve2():
    ans = +1e9
    best_t1 = 0
    best_t2 = 0
    for _ in tqdm(range(int(1e5))):
        t1 = random.random() * 20 - 10
        t2 = random.random() * 20 - 10
        A = np.array([[3 + 2 * t1 - t2, -2 + t1], [-2 + t1, -2 + t1]])
        if np.all(np.linalg.eigvals(A) >= 0):
            ans = min(ans, 4 * t1 - t2)
            if ans == 4 * t1 - t2:
                best_t1 = t1
                best_t2 = t2
    print(f"ans: {ans} t1: {best_t1} t2: {best_t2}")


def main():
    solve()
    # solve2()


if __name__ == "__main__":
    main()
