import numpy as np

for n in [2, 5, 10]:
    for seed in range(10):
        np.random.seed(seed)
        print(f"{n=} {seed=}")

        # 確率変数
        Xs = np.random.random() * np.random.random(n) + np.random.random()
        Ys = np.random.random() * np.random.random(n) + np.random.random()
        Zs = np.random.random() * np.random.random(n) + np.random.random()

        # 正規化(分散を1に)
        Xs /= np.std(Xs)
        Ys /= np.std(Ys)
        Zs /= np.std(Zs)
        assert np.isclose(np.var(Xs), 1)
        assert np.isclose(np.var(Ys), 1)
        assert np.isclose(np.var(Zs), 1)

        # 相関係数
        rXY = np.corrcoef(Xs, Ys)[0, 1]
        rYZ = np.corrcoef(Ys, Zs)[0, 1]
        rXZ = np.corrcoef(Xs, Zs)[0, 1]

        print(f"{rXY=} {rYZ=} {rXZ=}")

        print(f"{np.arccos(rXY)=} {np.arccos(rYZ)=} {np.arccos(rXZ)=}")

        # 以下はn=2では一致する
        assert np.isclose(
            rXZ, rXY * rYZ - np.sqrt(1 - rXY**2) * np.sqrt(1 - rYZ**2)
        ), (rXY, rXY * rYZ - np.sqrt(1 - rXY**2) * np.sqrt(1 - rYZ**2))
