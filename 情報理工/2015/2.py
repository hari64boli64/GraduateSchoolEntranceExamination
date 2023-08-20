import numpy as np

for n in range(2, 10 + 1):
    for seed in range(1000):
        np.random.seed(seed)
        print(f"{n=} {seed=}")

        # random variables
        Xs = np.random.random() * np.random.random(n) + np.random.random()
        Ys = np.random.random() * np.random.random(n) + np.random.random()
        Zs = np.random.random() * np.random.random(n) + np.random.random()

        # normalization (mean=0, var=1)
        Xs /= np.std(Xs)
        Ys /= np.std(Ys)
        Zs /= np.std(Zs)
        assert np.isclose(np.var(Xs), 1)
        assert np.isclose(np.var(Ys), 1)
        assert np.isclose(np.var(Zs), 1)

        # correlation coefficients
        rXY = np.corrcoef(Xs, Ys)[0, 1]
        rYZ = np.corrcoef(Ys, Zs)[0, 1]
        rXZ = np.corrcoef(Xs, Zs)[0, 1]

        print(f"{rXY=} {rYZ=} {rXZ=}")

        print(f"{np.arccos(rXY)=} {np.arccos(rYZ)=} {np.arccos(rXZ)=}")

        # the following assertion is true only when n = 2
        if n == 2:
            assert np.isclose(
                rXZ, rXY * rYZ - np.sqrt(1 - rXY**2) * np.sqrt(1 - rYZ**2)
            )

        # the following assertion is always true
        EPS = 1e-6
        thetaMin = np.arccos(rYZ) - np.arccos(rXY)
        thetaMax = np.arccos(rYZ) + np.arccos(rXY)
        assert thetaMin - EPS <= np.arccos(rXZ) <= thetaMax + EPS
