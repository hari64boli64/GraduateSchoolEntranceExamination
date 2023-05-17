import math
import numpy as np
import matplotlib.pyplot as plt


def _f(x):
    assert 0 <= x <= 1
    if x <= 1 / 2:
        return x + 1 / 2
    else:
        return 2 - 2 * x


def f(n, x):
    for _ in range(n):
        x = _f(x)
    return x


def visFn():
    fig, axes = plt.subplots(5, 2, figsize=(20, 8))
    for n in range(1, 10 + 1):
        Xs = np.linspace(0, 1, 2**10)
        axes[(n - 1) // 2][(n - 1) % 2].plot(Xs, [f(n, x) for x in Xs])
        axes[(n - 1) // 2][(n - 1) % 2].set_title(f"f^{n}(x)")
    fig.suptitle("f^n(x)")
    plt.tight_layout()
    plt.savefig("4.png")


def calcLogNp():
    A = np.array([[0, 1], [1, 1]], dtype=object)
    for n in range(1, 10):
        An = np.linalg.matrix_power(A, n)
        print(f"n: {n}, A^n: {An.tolist()}")
        print(f"trace: {np.trace(An)}")
    print("=" * 10)
    print(
        f"limit of logN(p)/p: ",
        math.log(np.trace(np.linalg.matrix_power(A, 1 << 20))) / (1 << 20),
    )
    print(f"{math.log((1+math.sqrt(5))/2)=}")


def main():
    visFn()
    calcLogNp()


if __name__ == "__main__":
    main()
