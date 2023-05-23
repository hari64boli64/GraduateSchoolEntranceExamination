import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

squared_errors = []
answers = []
for _ in tqdm(range(1000)):
    n = np.random.randint(1, 100)
    p = np.random.randint(1, 10)
    X = np.random.random((n, p))
    beta = np.random.random(p)
    sigma = np.random.random()
    epsilon = np.random.normal(0, sigma, n)
    y = X.dot(beta) + epsilon
    if np.linalg.matrix_rank(X) != p:
        continue
    beta_hat = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    mse = 0
    for _ in range(100):
        x_np1 = np.random.random(p)
        y_np1 = x_np1.T.dot(beta) + np.random.normal(0, sigma)
        squared_error = (y_np1 - x_np1.T.dot(beta_hat)) ** 2
        mse += squared_error
    mse /= 100
    squared_errors.append(mse)
    answers.append(
        (sigma**2) * (1 + x_np1.T.dot(np.linalg.inv(X.T.dot(X)).dot(x_np1)))
    )

plt.figure(figsize=(6, 6))
plt.scatter(answers, squared_errors)
plt.title("Simulated Squared Error vs. Theoretical Squared Error")
plt.xlabel("Theoretical Squared Error")
plt.ylabel("Simulated Squared Error")
plt.xscale("log")
plt.yscale("log")
plt.xlim(min(answers + squared_errors), max(answers + squared_errors))
plt.ylim(min(answers + squared_errors), max(answers + squared_errors))
plt.minorticks_on()
plt.grid(which="major", linestyle="-", linewidth="0.5", color="black")
plt.grid(which="minor", linestyle="-", linewidth="0.5", color="black")
plt.savefig("2.png")
