import os
import ast
import graphviz

# graphviz路径
os.environ["PATH"] += os.pathsep + 'D:/All/creat/Graphviz/bin/'


def visit(node, nodes, pindex, g):
    name = str(type(node).__name__)
    index = len(nodes)
    nodes.append(index)
    g.node(str(index), name)
    if index != pindex:
        g.edge(str(index), str(pindex))
    for n in ast.iter_child_nodes(node):
        visit(n, nodes, index, g)


def export_png(tree, export_path):
    graph = graphviz.Digraph(format="png")
    visit(tree, [], 0, graph)
    graph.render(export_path)


