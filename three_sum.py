import numpy as np
import matplotlib.pyplot as plt
import util

xs = [4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000]
ys = [3.099, 4.192, 5.576, 7.196, 9.257, 11.574, 14.095, 17.116, 20.597, 24.476]

plt.subplot(1, 2, 1)
plt.plot(xs, ys)
plt.scatter(xs, ys)

xs_lg = np.log10(xs)
ys_lg = np.log10(ys)
plt.subplot(1, 2, 2)
plt.scatter(xs_lg, ys_lg)

k, b = util.myleastsq(xs_lg, ys_lg)
print(f"k = {k}, b = {b}")

x = np.linspace(3.5, 4.5, 1000)
y = k * x + b
plt.plot(x, y)

def predict(N):
    return 10**b * N**k

print(predict(10000))

plt.show()
