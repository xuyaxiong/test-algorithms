from graphviz import Digraph

ids = [6, 2, 6, 4, 4, 6, 6, 2, 4, 4, ]

g = Digraph('test', filename='test.gv')
for index, id in enumerate(ids):
    g.node(f'{index}', label=f'{index}')

for index, id in enumerate(ids):
    if index == id:
        continue
    g.edge(f'{index}', f'{id}')

g.view()
