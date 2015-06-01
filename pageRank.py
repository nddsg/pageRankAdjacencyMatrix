import re
import sys
import networkx as nx
import product
import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image, ImageDraw

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

#G = nx.read_gml(filename)

#filename = "CA-GrQc.txt"
#G = nx.read_edgelist(filename,create_using=nx.DiGraph())

#k = 11
#P = [[.902,.253],[.221,.582]]
#G = product.kronecker_random_graph(k,P)
#for u,v in G.selfloop_edges():
#  G.remove_edge(u,v)

#G = nx.read_edgelist("C:\\Users\\tweninge\\Downloads\\CA-HepTh.txt")
#G = nx.barabasi_albert_graph(1000, 1)
#G = nx.powerlaw_cluster_graph(1000,1,.4)
#G = nx.random_regular_graph(10, 1000)
#G = nx.scale_free_graph(1000)
#G = nx.erdos_renyi_graph(1000,.05)
#G = nx.watts_strogatz_graph(1000, 5, .25)
G = nx.newman_watts_strogatz_graph(1000, 3, .25)

#G = nx.watts_strogatz_graph(16, 4, 0)
#G.add_edge(0, int(G.number_of_nodes() / 2))

pr = nx.pagerank(G, max_iter=55)
#pr = nx.pagerank(G, max_iter=255, tol=1e-16)

import community

dendo = community.generate_dendrogram(G, None)
com = community.partition_at_level(dendo, len(dendo)-1 )


#gm = nx.google_matrix(G)
maxPR = max(pr.values())

f, (ax1, ax2, ax3) = plt.subplots(1,3)

#plt.imshow(gm,
#           interpolation='nearest', origin='lower')
#plt.show()


x = np.zeros(G.number_of_edges())
y = np.zeros(G.number_of_edges())
z = np.zeros(G.number_of_edges())

i=0
for edge in G.edges():
  x[i] = (1 - (pr[edge[0]] / maxPR))
  y[i] = (1 - (pr[edge[1]] / maxPR))
  if com[edge[0]] == com[edge[1]]:
    z[i] = 1
  else:
    z[i] = 0
  #z[i] = (1 - (pr[edge[1]] / maxPR)) + (1 - (pr[edge[0]] / maxPR))
  i=i+1


ax1.scatter(x,y, c=z, s=z*20, alpha=0.2, cmap='seismic', vmin=z.min(), vmax=z.max(), linewidths=0)

## order by PR

x = np.zeros(G.number_of_edges() * 2)
y = np.zeros(G.number_of_edges() * 2)
z = np.zeros(G.number_of_edges() * 2)

ordered = dict(zip( range(0,G.number_of_nodes()), sorted(G.nodes(), key = lambda node: pr[node], reverse = True) ))
flip =    dict(zip( sorted(G.nodes(), key = lambda node: pr[node], reverse = True), range(0,G.number_of_nodes()) ))

i=0
for o in ordered.keys():
  for e in G.edges(ordered[o]):
    x[i] = o
    y[i] = flip[e[1]]
    z[i] = com[e[0]]
    i=i+1

ax2.scatter(x,y, c=z, s=20, alpha=0.5, vmin=z.min(), vmax=z.max(), linewidths=0)

x = np.zeros(G.number_of_edges() * 2)
y = np.zeros(G.number_of_edges() * 2)
z = np.zeros(G.number_of_edges() * 2)

i=0
for o in ordered.keys():
  for e in G.edges(ordered[o]):
    x[i] = o
    y[i] = flip[e[1]]
    if com[ordered[o]] == com[e[1]]:
      z[i] = 1
    i=i+1

ax3.scatter(x,y, c=z, s=20, alpha=0.5, vmin=z.min(), vmax=z.max(), linewidths=0)

plt.show()
