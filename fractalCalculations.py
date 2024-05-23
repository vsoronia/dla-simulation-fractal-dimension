import numpy as np
import random
import matplotlib.pyplot as plt

grid = np.loadtxt("fractal_output.txt")
M = np.empty((0, 10))
N = 20
for h in range(N):
    centers = random.sample(range(215, 236), 10)
    M_new = []

    for k in range(5, 51, 5):
        count = 0
        counts = []
        for t in range(len(centers)):
            for i in range(2*k):
                for j in range(2*k):
                    x = grid[centers[t] - k + i, centers[t] - k + j]
                    if x == 1:
                        count += 1
            counts.append(count)
        av = np.mean(counts)
        M_new.append(av)
    M = np.append(M, [M_new], axis=0)

M_avg = np.mean(M, axis=0)
L = list(range(5, 51, 5))
M_log = np.log10(M_avg)
L_log = np.log10(L)
plt.scatter(L_log, M_log)
fit = np.polyfit(L_log, M_log, 1)
fit_fn = np.poly1d(fit)
print("Slope of the line of best fit:", fit[0])
plt.plot(L_log, fit_fn(L_log), '--k')
plt.xlabel('log(L)')
plt.ylabel('log(M)')
plt.show()
