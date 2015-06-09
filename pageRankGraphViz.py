import networkx as nx
import pygraphviz as pgv
import math

def drawViz( nodes, neighbors, alpha, name):
    G = nx.watts_strogatz_graph(nodes, neighbors, alpha)
    G.add_edge(0, int(G.number_of_nodes() / 2))
    #G.add_edge(1, int(G.number_of_nodes() / 2) + 1)
    #G.add_edge(int(G.number_of_nodes() / 4), int(G.number_of_nodes() * 3 / 4))
    pr = nx.pagerank(G)
    A = pgv.AGraph()
    radius = 550
    tau = 2 * math.pi
    rotate = math.pi / 2
    for id in G.nodes():
      position = nodes - id
      A.add_node(id, label= str(id) + "\n" + ("%.17f" % pr[id]), pos="%f, %f" % (radius * math.cos(rotate + (tau * position / nodes)), radius * math.sin(rotate + (tau * position / nodes))))
    A.add_edges_from(G.edges());
    A.draw(name, prog="neato", args="-n")

drawViz(15, 4, 0, 'graph-15-4.png')
drawViz(16, 4, 0, 'graph-16-4.png')
drawViz(24, 4, 0, 'graph-20-4.png')

print "Done"
