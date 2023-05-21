import os
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm
from typing import List
from itertools import product

os.chdir("情報理工/2012")


def isConnected(adj: List[List[int]]):
    seen = [False] * len(adj)

    def dfs(v):
        seen[v] = True
        for nv in adj[v]:
            if not seen[nv]:
                dfs(nv)

    dfs(0)
    return all(seen)


def makeGraph(N_: int = -1, M_: int = -1, notDupli: bool = False):
    # print("now making...")
    N = random.randint(2, 30) if N_ == -1 else N_
    M = random.randint(1, N * (N - 1) // 2) if M_ == -1 else M_
    adj = [[] for _ in range(N)]
    A = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(M):
        u, v = random.sample(range(N), 2)
        assert u != v
        adj[u].append(v)
        adj[v].append(u)
        A[v][j] = 1
        A[u][j] = 1
    if not isConnected(adj):
        return makeGraph(N_, M_, notDupli)
    if notDupli and any(len(adj[v]) != len(set(adj[v])) for v in range(N)):
        return makeGraph(N_, M_, notDupli)
    return N, M, adj, A


def makeCycle():
    # print("now making...")
    N = random.randint(2, 30)
    M = N
    adj = [[] for _ in range(N)]
    A = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(M):
        u = j
        v = (j + 1) % N
        adj[u].append(v)
        adj[v].append(u)
        A[v][j] = 1
        A[u][j] = 1
    assert isConnected(adj)
    return N, M, adj, A


def visualizeGraph(
    N: int, M: int, adj: List[List[int]], title: str, circular: bool = False
):
    g = nx.Graph()
    g.add_nodes_from(range(N))
    for u in range(N):
        for v in adj[u]:
            g.add_edge(u, v)
    plt.figure(figsize=(8, 8))
    plt.title(f"{title} ({N=}, {M=})")
    nx.draw(g, pos=nx.circular_layout(g) if circular else None, with_labels=True)
    plt.savefig(f"img_5/{title}.png")
    plt.close()


def problem1():
    for i in range(100 + 1):
        N, M, adj, A = makeCycle()
        assert N == M
        if i == 100:
            visualizeGraph(N, M, adj, "problem1")
        det = np.linalg.det(A)
        print(f"{N=} {det=}")
        assert det == (2 if N % 2 == 1 else 0)


def problem2():
    cnt = 0
    while True:
        N, M, adj, A = makeGraph()
        if M <= 3:  # trivial case
            continue
        rank = np.linalg.matrix_rank(A)
        if rank == M:
            print(f"{N=} {M=} {rank=}")
            visualizeGraph(N, M, adj, f"problem2_{cnt}")
            cnt += 1
            if cnt >= 15:
                break


def problem4():
    N, M, adj, A = makeGraph(N_=7, M_=12, notDupli=True)
    print(adj)
    A = np.array(A)
    visualizeGraph(N, M, adj, f"problem4_original", circular=True)
    for id, Xs in tqdm(enumerate(product([0, 1 / 2, 1], repeat=M)), total=3**M):
        if np.allclose(A @ np.array(Xs), np.ones(N)):
            print(f"{id=}")
            NVis = N
            MVis = M - Xs.count(0)
            adjVis = [[] for _ in range(NVis)]
            for j, x in enumerate(Xs):
                if x != 0:
                    u, v = np.where(A[:, j] == 1)[0]
                    adjVis[u].append(v)
                    adjVis[v].append(u)
            visualizeGraph(NVis, MVis, adjVis, f"problem4_{id}", circular=True)


def main():
    random.seed(64)
    np.random.seed(64)

    problem1()
    problem2()
    problem4()


if __name__ == "__main__":
    main()
