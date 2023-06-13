import random

theta_A = None
theta_B = None


def isHead(whichCoin: str):
    if whichCoin == "A":
        return random.random() < theta_A
    else:
        return random.random() < theta_B


def trial(n: int):
    whichCoin = ["A", "B"][random.randint(0, 1)]
    headCount = 0
    for _ in range(n):
        if isHead(whichCoin):
            headCount += 1
        else:
            whichCoin = "A" if whichCoin == "B" else "B"
    return whichCoin, headCount + int(isHead(whichCoin))


def problem1(n):
    return ((1 / 2) - ((1 - theta_B) / (2 - theta_A - theta_B))) * (
        (-1 + theta_A + theta_B) ** (n - 1)
    ) + ((1 - theta_B) / (2 - theta_A - theta_B))


def problem2():
    return (theta_A + theta_B - 2 * theta_A * theta_B) / (2 - theta_A - theta_B)


def main():
    global theta_A, theta_B

    for _theta_A in [0.3, 0.5, 0.7]:
        for _theta_B in [0.3, 0.5, 0.7]:
            theta_A = _theta_A
            theta_B = _theta_B
            NUM_OF_TRIAL = 10000
            n = 100
            NthCoinIsA = 0
            Hn = 0
            for _ in range(NUM_OF_TRIAL):
                whichCoin, headCount = trial(n)
                NthCoinIsA += int(whichCoin == "A")
                Hn += headCount
            NthCoinIsA /= NUM_OF_TRIAL
            Hn /= NUM_OF_TRIAL
            Hn /= n
            print(f"{theta_A=}, {theta_B=}")
            print(f"{problem1(n)=}, {NthCoinIsA=}")
            print(f"{problem2()=}, {Hn=}")


if __name__ == "__main__":
    main()
