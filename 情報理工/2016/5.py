import math
import random
import numpy as np
from typing import List


def makeProblem(problemNo: int):
    assert 1 <= problemNo <= 4
    zeroRate = random.random()
    generator = random.random
    n = random.randint(1, 10)
    if problemNo == 1:
        zeroRate = 0.0
    if problemNo == 2:
        generator = lambda: random.randint(0, 1)
    if problemNo == 4:
        n = 16
        zeroRate = 1 / n
        generator = lambda: random.randint(1, 5)
    As = [0 if random.random() < zeroRate else generator() for _ in range(n)]
    return n, As


def check(n: int, As: List[int], solver: callable):
    # fがアルゴリズム, dataがデータ構造に対応する
    f, data = solver(n, As)
    # 全てのクエリに対して正しい答えが返ってくるかチェックする
    for s in range(1, n + 1):
        for t in range(s, n + 1):
            ans = f(s, t, data)
            print(s, t, ans)
            if not np.isclose(ans, math.prod(As[s - 1 : t])):
                raise Exception("Wrong Answer")
    print("ok!")


def solve1(n: int, As: List[int]) -> callable:
    """
    \prod_{i=s}^{t}A[i] =
    (\prod_{i=1}^{t}A[i]) / (\prod_{i=1}^{s-1}A[i])
    """
    Ps = [1.0]
    for i in range(n):
        Ps.append(Ps[-1] * As[i])

    def f(s: int, t: int, Ps: List[int]):
        return Ps[t] / Ps[s - 1]

    return f, Ps


def solve2(n: int, As: List[int]) -> callable:
    """
    0の個数を数えて、
    [s,t]間でその個数の増減がないかを調べれば良い
    """
    numOfZeros = [0]
    for i in range(n):
        numOfZeros.append(numOfZeros[-1] + int(As[i] == 0))

    def f(s: int, t: int, numOfZeros: List[int]):
        return 0 if numOfZeros[t] != numOfZeros[s - 1] else 1

    return f, numOfZeros


def solve3(n: int, As: List[int]) -> callable:
    """
    (1)と(2)を組み合わせるだけで良い
    Psは、0が出てきたらリセットの意味で1にする
    """
    Ps = [1.0]
    for i in range(n):
        Ps.append(Ps[-1] * As[i])
        if Ps[-1] == 0:
            Ps[-1] = 1

    numOfZeros = [0]
    for i in range(n):
        numOfZeros.append(numOfZeros[-1] + int(As[i] == 0))

    def f(s: int, t: int, Ps_numOfZeros: List[int]):
        Ps, numOfZeros = Ps_numOfZeros
        return 0 if numOfZeros[t] != numOfZeros[s - 1] else Ps[t] / Ps[s - 1]

    return f, (Ps, numOfZeros)


def vis4():
    """
    SegmentTree、もしくは、BinaryIndexedTreeで検索
    空間計算量は、O(logN)のように思えるが、
    よくよく考えると、2N-1で抑えられている

    出力例:

    As=[3, 1, 4, 1, 3, 3, 3, 2, 1, 3, 3, 0, 5, 4, 3, 5]

    0段目:   0---------------------------------------------
    1段目: 648---------------------  0---------------------
    2段目:  12--------- 54---------  0---------300---------
    3段目:   3---  4---  9---  6---  3---  0--- 20--- 15---
    4段目:   3  1  4  1  3  3  3  2  1  3  3  0  5  4  3  5
    """
    n, As = makeProblem(4)
    print(f"{As=}")
    logN = round(math.log2(n))
    for i in range(logN + 1):
        print(f"{i}段目: ", end="")
        for j in range(2**i):
            print(
                f"{math.prod(As[(2**(logN-i)) * j : (2**(logN-i)) * (j + 1)]):>3}",
                end="-" * (3 * ((2 ** (logN - i) - 1))),
            )
        print()


def main():
    for _ in range(10):
        n, As = makeProblem(1)
        print(f"{n=}, {As=}")
        check(n, As, solve1)
    for _ in range(10):
        n, As = makeProblem(2)
        print(f"{n=}, {As=}")
        check(n, As, solve2)
    for _ in range(10):
        n, As = makeProblem(3)
        print(f"{n=}, {As=}")
        check(n, As, solve3)
    vis4()


if __name__ == "__main__":
    main()
