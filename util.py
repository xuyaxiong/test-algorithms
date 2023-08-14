from scipy.optimize import leastsq


def err(p, x, y):
    return p[0] * x + p[1] - y


def myleastsq(xs, ys):
    p0 = [1, 1]
    ret = leastsq(err, p0, args=(xs, ys))
    return ret[0]
