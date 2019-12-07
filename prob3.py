import numpy as np

def prob3(f):
    for n in range(len(f)):
        p = np.polyfit(f[:, 0], f[:, 1], n)
        e = np.linalg.norm(f[:, 1] - np.polyval(p, f[:, 0]))
        x = [n, e]
        if n == 0:
            y = x
        if y[1] >= x[1]:
            z = x[0]
    p = np.polyfit(f[:, 0], f[:, 1], z)
    return p