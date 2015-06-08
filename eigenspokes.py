import re
import sys
import networkx as nx
import product
import numpy as np
import matplotlib.pyplot as plt
import math


gml = ('adjnoun.gml',
'celegansneural.gml',
'football.gml',
'dolphins.gml',
'hep-th.gml',
'karate.gml',
'lesmis.gml',
'netscience.gml',
'polblogs.gml',
'polbooks.gml',
'power.gml')

#for filename in gml:
#  G = nx.read_gml(filename)
#  print filename + str(G.number_of_nodes()) + ", " + str(G.number_of_edges())

#filename = "CA-GrQc.txt"
#G = nx.read_edgelist(filename,create_using=nx.DiGraph())

#k = 11
#P = [[.902,.253],[.221,.582]]
#G = product.kronecker_random_graph(k,P)
#for u,v in G.selfloop_edges():
#  G.remove_edge(u,v)

#G = nx.read_edgelist("C:\\Users\\tweninge\\Downloads\\CA-HepTh.txt")
#G = nx.barabasi_albert_graph(500, 1)
#G = nx.powerlaw_cluster_graph(1000,1,.1)
#G = nx.random_regular_graph(10, 1000)
#G = nx.scale_free_graph(1000)
#G = nx.erdos_renyi_graph(1000,.05)
#G = nx.watts_strogatz_graph(3000, 6, .35)
G = nx.newman_watts_strogatz_graph(250, 4, .05)
#G = nx.newman_watts_strogatz_graph(1000, 5, .25)

G = nx.Graph(G)
A = nx.to_numpy_matrix(G)

u, s, v = np.linalg.svd(A)

f, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3,  sharex='col', sharey='row', figsize=(8,8), dpi=80)

ax1.scatter(u[0],u[1])
ax2.scatter(u[1],u[2])
ax3.scatter(u[2],u[3])
ax4.scatter(u[3],u[4])
ax5.scatter(u[4],u[5])
ax6.scatter(u[5],u[6])
ax7.scatter(u[6],u[7])
ax8.scatter(u[7],u[8])
ax9.scatter(u[8],u[9])

plt.show()