import math
import os
from typing import List

import matplotlib.pyplot as plt
from numba import njit
from tqdm import tqdm


@njit
def f(A: List[int], B: List[int]):
    m = len(A)
    n = len(B)
    total = 0.0
    for i in range(m):
        sub = 0.0
        for j in range(n):
            sub += math.exp(-abs(A[i] - B[j]))
        total += 1 / (sub / n)
    return math.log(total / m)


@njit
def g(s):
    m = int(2e3)
    n = int(2e3)
    A = [s + (i / m) for i in range(m)]
    B = [j / n for j in range(n)]
    return f(A, B)


def h(z):
    ret = 0
    cnt = int(1e4)
    for i in range(cnt):
        x = i / cnt
        ret += math.exp(-abs(z - x))
    return ret / cnt


def main():
    Z = [(i - 300) / 100 for i in range(600)]
    hZ = []
    for z in tqdm(Z):
        hZ.append(h(z))
    plt.plot(Z, hZ)
    plt.xlabel("z")
    plt.ylabel("h(z)")
    plt.title("(1)")
    # plt.show()
    plt.savefig(os.path.join(os.path.dirname(__file__), "1.png"), bbox_inches="tight")
    plt.clf()

    S = [(i - 300) / 100 for i in range(600)]
    gS = []
    for s in tqdm(S):
        gS.append(g(s))
    plt.plot(S, gS)
    plt.xlabel("s")
    plt.ylabel("g(s)")
    plt.title("(4)")
    # plt.show()
    plt.savefig(os.path.join(os.path.dirname(__file__), "4.png"), bbox_inches="tight")
    plt.clf()


if __name__ == "__main__":
    main()
