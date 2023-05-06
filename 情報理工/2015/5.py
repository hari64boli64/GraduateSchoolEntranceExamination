import math
import random
from collections import defaultdict

random.seed(0)


def makeProblem(size):
    sigma = random.randint(1, size)
    n = random.randint(1, size)
    A = list(range(1, sigma + 1))
    S = [random.choice(A) for _ in range(n)]
    k = len(set(S))
    return sigma, n, S, k


def problem1(sigma, n, S):
    # 問題(1)の解答

    # 1. max(D_i)を求めるのに必要な、
    #    各Aの要素に関して最後の出現位置を記録する配列を用意する
    #    空間 O(sigma) 時間 O(sigma)
    last = [0 for _ in range(sigma)]

    # 2. 各iについて、d(i)を計算する
    #    空間 O(1) 時間 O(n)
    for i in range(n):
        yield (i + 1) - last[S[i] - 1]
        last[S[i] - 1] = i + 1


def problem2(sigma, n, S):
    # 問題(2)の解答

    # 1. max(D_i)を求めるのに必要な、
    #    各Aの要素に関して最後の出現位置を記録する配列を辞書で持つ
    #    空間 O(k) 時間 O(1)
    last = defaultdict(int)

    # 2. 各iについて、d(i)を計算する
    #    空間 O(1) 時間 O(n logk)
    for i in range(n):
        # ここの計算量が O(logk) になる
        yield (i + 1) - last[S[i] - 1]
        last[S[i] - 1] = i + 1


def problem3(sigma, n, S):
    # 問題(3)の解答

    # ならし計算量の解析に近い
    # Sに現れる要素それぞれに注目して見ると、
    # 総計で見る回数は必ずnで抑えられる
    # よって、全体でO(nk)

    for i in range(n):
        for j in range(i - 1, -1, -1):
            if S[j] == S[i]:
                yield i - j
                break
        else:
            yield i + 1


def trial():
    sigma, n, S, k = makeProblem(size=10)
    print(f"{sigma=}, {n=}, {k=}")
    print(f"{S=}")

    Ds = [[j + 1 for j in range(i) if S[j] == S[i]] for i in range(n)]
    ds = [i - max(D) if D else i for i, D in enumerate(Ds, start=1)]

    print(f"{Ds=}")
    print(f"{ds=}")

    ans1 = list(problem1(sigma, n, S))
    ans2 = list(problem2(sigma, n, S))
    ans3 = list(problem3(sigma, n, S))

    assert ds == ans1, ans1
    assert ds == ans2, ans2
    assert ds == ans3, ans3


def computeSumOfd():
    # 問題(4)の解答

    #   \sum d <= kn
    # ⇒ 1/n \su d <= k
    # logの凸性より、
    #   1/n \sum log d <= log (1/n \sum d) <= log k
    # ⇒ \sum log d <= n log k


    sigma, n, S, k = makeProblem(size=10000)
    print(f"{sigma=}, {n=}, {k=}")

    ds = list(problem1(sigma, n, S))

    print(f"{sum(math.log(d) for d in ds)=}")
    print(f"{n*math.log(k)=}")


def main():
    for i in range(5):
        trial()
        if i != 4:
            print("-" * 10)

    print("=" * 10)

    for i in range(5):
        computeSumOfd()
        if i != 4:
            print("-" * 10)


if __name__ == "__main__":
    main()
