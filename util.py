from scipy.optimize import leastsq
from graphviz import Digraph


def err(p, x, y):
    return p[0] * x + p[1] - y


def myleastsq(xs, ys):
    p0 = [1, 1]
    ret = leastsq(err, p0, args=(xs, ys))
    return ret[0]


def show_graph(ids):
    g = Digraph("test", filename="test.gv")
    g.graph_attr.update({"rankdir": "BT"})
    for index, id in enumerate(ids):
        g.node(f"{index}", label=f"{index}")

    for index, id in enumerate(ids):
        if index == id:
            continue
        g.edge(f"{index}", f"{id}")

    g.view()
