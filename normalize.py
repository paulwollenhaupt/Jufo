import numpy as np


def norm(x):
    pm25 = list(x[:, 0])
    pm10 = list(x[:, 1])
    print(len(pm25), len(pm10))
    for c, (p25, p10) in enumerate(zip(pm25, pm10)):
        if p25 > 999.9 or p10 > 1999.9 or p25 < 1.:
            del pm25[c]
            del pm10[c]
    pm25 = np.array(pm25)[:, np.newaxis]
    pm10 = np.array(pm10)[:, np.newaxis]
    return np.concatenate([pm25, pm10], -1)
