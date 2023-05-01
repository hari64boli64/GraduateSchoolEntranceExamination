import numpy as np
import random
from itertools import product


def makeProblem(problem: str):
    if problem == "P":
        N = 5
        S = 5
        Ps = [2, 3, 2, 1, 3]
        Ss = [2, 3, 1, 2, 1]
        return N, S, Ps, Ss
    elif problem == "Q":
        N = random.randint(1, 5)
        S = random.randint(1, 10)
        Ps = [random.randint(1, 10) for _ in range(N)]
        Ss = [random.randint(1, 10) for _ in range(N)]
        return N, S, Ps, Ss
    elif problem == "R":
        N = random.randint(1, 5)
        S = random.randint(1, 10)
        W = random.randint(1, 10)
        Ps = [random.randint(1, 10) for _ in range(N)]
        Ss = [random.randint(1, 10) for _ in range(N)]
        Ws = [random.randint(1, 10) for _ in range(N)]
        return N, S, W, Ps, Ss, Ws
    else:
        raise ValueError("problem must be P, Q or R")


def slowP(N, S, Ps, Ss):
    """
    bit全探索による(P)の解法

    解法を説明すると、
    1. 0~2^N-1までのbitを生成する これは、各x_iが1かどうかを表す
    2. そのbitに対応するxについての制約条件を計算する
    3. 制約条件を満たすならば、そのbitに対応するxについての目的関数の値を計算する
    4. 3.で計算した値の最大値を答えとする
    というものである。

    これは、bit全探索の計算量がO(2^N)であり、指数時間アルゴリズムとなっている。
    """
    ans = -np.inf
    for bit in range(1 << N):
        constraint = sum([Ss[i] * bool(bit & (1 << i)) for i in range(N)])
        if constraint <= S:
            obj = sum([Ps[i] * bool(bit & (1 << i)) for i in range(N)])
            ans = max(ans, obj)
    return ans


def slowQ(N, S, Ps, Ss):
    """
    全探索による(Q)の解法

    上とほぼ同様
    """
    ans = -np.inf
    for Xs in product(range(0, 10 + 1), repeat=N):
        constraint = sum([Ss[i] * Xs[i] for i in range(N)])
        if constraint <= S:
            obj = sum([Ps[i] * Xs[i] for i in range(N)])
            ans = max(ans, obj)
    return ans


def slowR(N, S, W, Ps, Ss, Ws):
    """
    全探索による(R)の解法

    上とほぼ同様
    """
    ans = -np.inf
    for bit in range(1 << N):
        constraint1 = sum([Ss[i] * bool(bit & (1 << i)) for i in range(N)])
        constraint2 = sum([Ws[i] * bool(bit & (1 << i)) for i in range(N)])
        if constraint1 <= S and constraint2 <= W:
            obj = sum([Ps[i] * bool(bit & (1 << i)) for i in range(N)])
            ans = max(ans, obj)
    return ans


def solveP():
    """
    (1),(2)の解答
    これは p1,…,pn, s1,…,sn について多項式時間，S について指数時間アルゴリズムである。
    """
    N, S, Ps, Ss = makeProblem("P")
    print(f"{N=},{S=},{Ps=},{Ss=}")
    print(f"{slowP(N, S, Ps, Ss)=}")

    As = [[None for _ in range(S + 1)] for _ in range(N + 1)]
    for s in range(1, S + 1):
        As[0][s] = -np.inf
    As[0][0] = 0

    for j in range(1, N + 1):
        for s in range(S + 1):
            if s < Ss[j - 1]:
                As[j][s] = As[j - 1][s]
            else:
                As[j][s] = max(As[j - 1][s], Ps[j - 1] + As[j - 1][s - Ss[j - 1]])

    print("As=", *As, sep="\n")
    print("ans=", max(max(a) for a in As))


def solveQ():
    """
    (3)の解答
    これは p1,…,pn, s1,…,sn について多項式時間，S について指数時間アルゴリズムである。
    """
    N, S, Ps, Ss = makeProblem("Q")
    print(f"{N=},{S=},{Ps=},{Ss=}")
    print(f"{slowQ(N, S, Ps, Ss)=}")

    As = [[None for _ in range(S + 1)] for _ in range(N + 1)]
    for s in range(1, S + 1):
        As[0][s] = -np.inf
    As[0][0] = 0

    for j in range(1, N + 1):
        for s in range(S + 1):
            # ここが漸化式
            if s < Ss[j - 1]:
                As[j][s] = As[j - 1][s]
            else:
                As[j][s] = max(
                    As[j - 1][s],
                    # 以下が増えた これは、x_iを1~10の範囲内で変化させている
                    max(
                        Ps[j - 1] * x + As[j - 1][s - Ss[j - 1] * x]
                        for x in range(1, 10 + 1)
                        if s - Ss[j - 1] * x >= 0
                    ),
                )

    # print("As=", *As, sep="\n")
    print("ans=", max(max(a) for a in As))


def solveR():
    """
    (4)の解答
    これは p1,…,pn, s1,…,sn, w1,…,wn について多項式時間，S について指数時間アルゴリズムである。
    """
    N, S, W, Ps, Ss, Ws = makeProblem("R")
    print(f"{N=},{S=},{W=},{Ps=},{Ss=},{Ws=}")
    print(f"{slowR(N, S, W, Ps, Ss, Ws)=}")

    As = [[[None for _ in range(W + 1)] for _ in range(S + 1)] for _ in range(N + 1)]
    for s in range(S + 1):
        for w in range(W + 1):
            if s != 0 or w != 0:
                As[0][s][w] = -np.inf
    As[0][0][0] = 0

    for j in range(1, N + 1):
        for s in range(S + 1):
            for w in range(W + 1):
                if s < Ss[j - 1] or w < Ws[j - 1]:
                    As[j][s][w] = As[j - 1][s][w]
                else:
                    As[j][s][w] = max(
                        As[j - 1][s][w],
                        Ps[j - 1] + As[j - 1][s - Ss[j - 1]][w - Ws[j - 1]],
                    )

    # print("As=", *As, sep="\n")
    print("ans=", max(max(max(a) for a in aa) for aa in As))


def main():
    solveP()
    print("=" * 10)
    solveQ()
    print("=" * 10)
    solveR()


if __name__ == "__main__":
    main()
