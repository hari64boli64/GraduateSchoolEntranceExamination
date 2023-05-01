import os
from md2tex import BEGIN_DOCUMENT, HEAD2, HEAD3, THEBIBLIOGRAPHY, END_DOCUMENT


def colorizeOutput(s: str, color: int):
    return f"\033[3{color}m{s}\033[0m"


def makeFile(year: int, number: int):
    folder = f"情報理工/{year}/"
    path = folder + f"{year}_{number}.tex"
    if os.path.exists(path):
        print(colorizeOutput(f"File {path} already exists.", 1))
        yesno = input(colorizeOutput("Overwrite?(y/n):", 2))
        if not (yesno == "y" or yesno == "Y"):
            assert False

    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(path, "w", encoding="utf-8") as f:
        print(BEGIN_DOCUMENT(f"{year}年度 大問{number}"), file=f)
        print(HEAD2("問題"), end="\n\n", file=f)
        print(HEAD2("解答"), end="\n\n", file=f)
        print(HEAD3("(1)"), end="\n\n", file=f)
        print(HEAD3("(2)"), end="\n\n", file=f)
        print(HEAD3("(3)"), end="\n\n", file=f)
        print(HEAD2("知識"), end="\n\n", file=f)
        print(THEBIBLIOGRAPHY([]), end="\n\n", file=f)
        print(END_DOCUMENT(), file=f)


def main():
    year = int(input(colorizeOutput("Year:", 3)))
    assert 2010 <= year <= 2023
    number = int(input(colorizeOutput("Number(-1 to all):", 4)))
    assert number == -1 or 1 <= number <= 5

    if number == -1:
        for i in range(1, 5 + 1):
            makeFile(year, i)
    else:
        makeFile(year, number)


if __name__ == "__main__":
    main()
