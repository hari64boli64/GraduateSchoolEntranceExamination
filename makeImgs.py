import glob
import os

# pathToFolder = r"./"
# paths = glob.glob(pathToFolder + "*.png")

paths = glob.glob(r"./情報理工/2012/img_5/problem4_*.png", recursive=True)

print(f"{paths=}")

print("Is this ok? (y/n)")
if input() != "y":
    print("Aborted")
    exit()


while len(paths) % 3 != 0:
    paths.append("X" * 10)

with open("resultOfMakeImgs.log", "w") as f:
    for i in range(len(paths) // 3):
        path1, path2, path3 = paths[3 * i : 3 * i + 3]
        cap1, cap2, cap3 = path1[2:-4], path2[2:-4], path3[2:-4]
        code = (
            r"""\begin{figure}[htbp]
        \begin{minipage}{0.33\hsize}
        \begin{center}
            \includegraphics[width=40mm]{"""
            + path1
            + r"""}
        \end{center}
        \caption{"""
            + cap1
            + r"""}
        \end{minipage}
        \begin{minipage}{0.33\hsize}
        \begin{center}
            \includegraphics[width=40mm]{"""
            + path2
            + r"""}
        \end{center}
        \caption{"""
            + cap2
            + r"""}
        \end{minipage}
        \begin{minipage}{0.33\hsize}
        \begin{center}
            \includegraphics[width=40mm]{"""
            + path3
            + r"""}
        \end{center}
        \caption{"""
            + cap3
            + r"""}
        \end{minipage}
    \end{figure}"""
            + "\n"
        )
        print(code, file=f)
