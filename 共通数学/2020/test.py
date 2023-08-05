import random

import matplotlib.pyplot as plt


def trial(M: int, q: float):
    cnt = 0
    ans = 0
    while cnt < M:
        x = random.random()
        ans += 1
        if x < q:
            cnt += 1
        else:
            cnt = 0
    return ans


def main():
    for M in [1, 2, 3]:
        for q in [0.1, 0.2, 0.3, 0.4, 0.5]:
            answers = []
            for _ in range(10000):
                answers.append(trial(M, q))
            avg = sum(answers) / len(answers)
            # plt.title()
            # plt.hist(answers)
            # plt.show()
            print("=" * 10)
            print(f"{M=}, {q=}")
            print(f"{avg=}")
            print(f"{(1 - q**M) / ((1 - q) * (q**M))=}")


if __name__ == "__main__":
    main()
