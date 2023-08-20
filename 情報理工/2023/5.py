import math
from collections import defaultdict

from numba import jit
from tqdm import tqdm


@jit(cache=True)
def toSparseTernaryRepresentation(S: str):
    ret = ""
    i = 0
    while i < len(S):
        if S[i] == "0":
            ret += "0,"
            i += 1
        elif S[i] == "1":
            cnt = 0
            while i < len(S) and S[i] == "1":
                cnt += 1
                i += 1
            if cnt == 1:
                ret += "1,"
            else:
                ret += "-1," + "0," * (cnt - 1)
                # originally, the following
                # must be inplace operation
                # for the sake of efficiency
                S = S[:i] + "1" + S[i + 1 :]
    return ret[:-1]


def anotherSolution(n: int):
    def L(i):
        if i <= 0:
            return 0
        if i % 2 == 1:
            return (2 ** (i + 1) - 1) // 3
        else:
            return 2 * (2**i - 1) // 3

    d = []
    for i in range(math.ceil(math.log2(n)) + 3)[::-1]:
        if abs(n - (2**i)) <= L(i - 1):
            n -= 2**i
            d.append(1)
        elif abs(n + (2**i)) <= L(i - 1):
            n += 2**i
            d.append(-1)
        else:
            d.append(0)

    d = d[::-1]
    while d[-1] == 0:
        d.pop()
    return ",".join(map(str, d))


def problem5():
    maxN = 16
    zeroCnt = 0
    cntPer3 = defaultdict(int)
    for n in tqdm(range(1, (1 << maxN) + 1)):
        S = bin(n)[2:][::-1]
        T = toSparseTernaryRepresentation(S)
        S += "0" * (maxN - len(S))
        listT = list(map(int, T.split(",")))
        listT += [0] * (maxN - len(listT))
        if listT[maxN // 2] == 0:
            zeroCnt += 1
            cntPer3[tuple(S[maxN // 2 - 1 : maxN // 2 + 2][::-1])] += 1
    print(f"result: {zeroCnt/(1<<maxN)}")
    print(f"cntPer3: {sorted(cntPer3.items())}")


def main():
    maxIntPerDigit = defaultdict(int)
    for n in range(1, 1000 + 1):
        S = bin(n)[2:][::-1]

        # ternary representation
        T = toSparseTernaryRepresentation(S)
        print(f"binary: {S} | ternary: {T}")

        # another solution
        T2 = anotherSolution(n)
        assert T == T2, f"{T} != {T2}"

        # assertion
        TasInt = sum([c * (2**i) for i, c in enumerate(list(map(int, T.split(","))))])
        assert TasInt == n

        # count
        maxIntPerDigit[len(T.split(","))] = max(maxIntPerDigit[len(T.split(","))], n)

    print(f"maxIntPerDigit: {maxIntPerDigit}")


if __name__ == "__main__":
    main()
    # problem5()
