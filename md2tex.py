import os


def BEGIN_DOCUMENT(text):
    return (
        r"""\documentclass[a4paper, 10pt, dvipdfmx]{jlreq}

\usepackage{amsmath,amsfonts,amssymb}
\usepackage{bm}
\usepackage{mathtools}
\usepackage{siunitx}
\usepackage[dvipdfmx]{graphicx}
\usepackage[dvipdfmx]{color}
\usepackage[dvipdfmx, colorlinks=true, allcolors=blue]{hyperref}
\usepackage{listings}
\usepackage{tikz}
\usepackage{physics}
\usepackage{url}

\Urlmuskip=0mu plus 10mu
\allowdisplaybreaks[4]
\frenchspacing
\definecolor{OliveGreen}{rgb}{0.0,0.6,0.0}
\definecolor{Orenge}{rgb}{0.89,0.55,0}
\definecolor{SkyBlue}{rgb}{0.28, 0.28, 0.95}
\lstset{
  language={c++},
  basicstyle={\ttfamily},
  identifierstyle={\small},
  ndkeywordstyle={\small},
  frame=single,
  breaklines=true,
  numbers=left,
  xrightmargin=0zw,
  xleftmargin=3zw,
  numberstyle={\scriptsize},
  lineskip=-0.9ex,
  keywordstyle={\small\bfseries\color{SkyBlue}},  
  commentstyle={\color{OliveGreen}}, 
  stringstyle={\small\ttfamily\color{Orenge}}    
}

\begin{document}

\title{"""
        + text
        + r"""}
\author{hari64boli64 (hari64boli64@gmail.com)}
\date{\today}
\maketitle
"""
    )


def HEAD2(text):
    return r"\section{" + text + "}"


def HEAD3(text):
    return r"\subsection*{" + text + "}"


def HEAD4(text):
    return r"\subsubsection*{" + text + "}"


def THEBIBLIOGRAPHY(texts):
    return (
        r"\begin{thebibliography}{9}"
        + "\n"
        + "\n".join(
            [
                r"  \bibitem{site:" + str(i + 1) + "}\n    " + text
                for i, text in enumerate(texts)
            ]
        )
        + "\n"
        + r"\end{thebibliography}"
    )


def END_DOCUMENT():
    return r"\end{document}"


def main():
    inPath = "情報理工/2020_5.md"
    outPath = inPath.replace(".md", ".tex")

    assert os.path.exists(inPath) and not os.path.exists(outPath)

    bal_cnt = 0
    isBibliography = False
    Bibliographys = []

    with open(inPath, "r", encoding="utf-8") as r:
        with open(outPath, "w", encoding="utf-8") as w:
            lines = r.readlines()
            for i, line in enumerate(lines):
                FIRST_SECTION = line.split(" ")[0].strip()
                if FIRST_SECTION == "#":
                    assert i == 0
                    TITLE = line[line.find("#") + 1 :].strip()
                    print(BEGIN_DOCUMENT(TITLE), file=w)
                elif FIRST_SECTION == "##":
                    if line[line.find("##") + 2 :].strip() == "参考文献":
                        isBibliography = True
                    print(HEAD2(line[line.find("##") + 2 :].strip()), file=w)
                elif FIRST_SECTION == "###":
                    print(HEAD3(line[line.find("###") + 3 :].strip()), file=w)
                elif FIRST_SECTION == "####":
                    print(HEAD4(line[line.find("####") + 4 :].strip()), file=w)
                elif FIRST_SECTION == "#####":
                    raise NotImplementedError
                elif FIRST_SECTION == "######":
                    raise
                elif FIRST_SECTION == "$$":
                    if bal_cnt == 0:
                        print(r"\begin{align*}", file=w)
                        bal_cnt += 1
                    elif bal_cnt == 1:
                        print(r"\end{align*}", file=w)
                        bal_cnt -= 1
                    else:
                        assert False
                elif FIRST_SECTION in [r"\begin{align*}", r"\begin{aligned}"]:
                    if bal_cnt == 0:
                        print(r"\begin{align*}", file=w)
                        bal_cnt += 1
                elif FIRST_SECTION in [r"\end{align*}", r"\end{aligned}"]:
                    if bal_cnt == 0:
                        print(r"\end{align*}", file=w)
                        bal_cnt -= 1
                elif isBibliography:
                    if line.strip() != "":
                        assert line.count("<") == 1 and line.count(">") == 1
                        line = line.replace("<", r"\url{").replace(">", "}")
                        Bibliographys.append(line.strip())
                else:
                    print(line, file=w, end="")

            print(THEBIBLIOGRAPHY(Bibliographys), file=w)
            print(END_DOCUMENT(), file=w)


if __name__ == "__main__":
    main()
