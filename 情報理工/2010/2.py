import random


def random_walk():
    x = 0
    cnt = 0
    while True:
        cnt += 1
        if random.random() < 0.1:
            x += 1
        else:
            x -= 1
        if abs(x) >= 2:
            # print(cnt)
            return cnt


def main():
    num_of_trial = 100000
    sum = 0
    for _ in range(num_of_trial):
        sum += random_walk()
    print("average:", sum / num_of_trial)


if __name__ == "__main__":
    main()
