import numpy as np
import matplotlib.pyplot as plt
import util
import math


def vis(xs, ys):
    plt.subplot(1, 2, 1)
    plt.plot(xs, ys)
    plt.scatter(xs, ys)

    xs_lg = np.log10(xs)
    ys_lg = np.log10(ys)
    plt.subplot(1, 2, 2)
    plt.scatter(xs_lg, ys_lg)

    k, b = util.myleastsq(xs_lg, ys_lg)
    print(f"k = {k}, b = {b}")

    x = np.linspace(5.5, 7, 1000)
    y = k * x + b
    plt.plot(x, y)

    def predict(N):
        return 10**b * N**k

    print(predict(10000))

    plt.show()


def vis_opt(xs, ys):
    plt.subplot(1, 2, 1)
    plt.plot(xs, ys)
    plt.scatter(xs, ys)

    xs_lg = np.array(xs) * np.log2(xs)
    ys_lg = np.array(ys)
    plt.subplot(1, 2, 2)
    plt.scatter(xs_lg, ys_lg)

    k, b = util.myleastsq(xs_lg, ys_lg)
    print(f"k = {k}, b = {b}")

    x = np.linspace(2, 9, 1000)
    y = k * x + b
    plt.plot(x, y)

    def predict(N):
        return N * math.log2(N) * k + b

    print(predict(5000000))

    plt.show()


xs = [40000, 50000, 60000, 70000, 80000, 90000, 100000,
      110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000, 200000, ]
ys = [0.12, 0.19, 0.272, 0.387, 0.465, 0.589, 0.72,
      0.886, 1.055, 1.28, 1.431, 1.622, 1.843, 2.076, 2.345, 2.643, 2.904, ]

xs1 = [1300000, 1400000, 1500000, 1600000, 1700000, 1800000, 1900000, 2000000, 2100000, 2200000, 2300000, 2400000, 2500000, 2600000, 2700000, 2800000,
       2900000, 3000000, 3100000, 3200000, 3300000, 3400000, 3500000, 3600000, 3700000, 3800000, 3900000, 4000000, 4100000, 4200000, 4300000, 4400000, 4500000, ]
ys1 = [0.132, 0.142, 0.154, 0.164, 0.171, 0.183, 0.191, 0.203, 0.212, 0.224, 0.233, 0.242, 0.254, 0.266, 0.275, 0.285,
       0.294, 0.301, 0.314, 0.325, 0.332, 0.352, 0.355, 0.361, 0.37, 0.388, 0.399, 0.406, 0.413, 0.42, 0.425, 0.442, 0.453, ]
vis_opt(xs1, ys1)
