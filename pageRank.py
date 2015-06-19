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
G = nx.barabasi_albert_graph(1000, 1)
#G = nx.powerlaw_cluster_graph(1000,1,.4)
#G = nx.random_regular_graph(10, 1000)

#G = nx.Graph()
#G.add_edges_from(nx.scale_free_graph(1000).edges())

#G = nx.erdos_renyi_graph(1000,.05)
#G = nx.watts_strogatz_graph(1000, 5, .25)
#G = nx.newman_watts_strogatz_graph(1000, 3, .25)

#G = nx.watts_strogatz_graph(20, 4, 0)
#G.add_edge(0, int(G.number_of_nodes() / 2))

import community

dendo = community.generate_dendrogram(G, None)
com = community.partition_at_level(dendo, len(dendo) - 1)


#gm = nx.google_matrix(G)

f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)

#plt.imshow(gm,
#           interpolation='nearest', origin='lower')
#plt.show()

x = np.zeros(G.number_of_edges() * 2)
y = np.zeros(G.number_of_edges() * 2)
z = np.zeros(G.number_of_edges() * 2)

#pr = nx.pagerank(G, max_iter=55)
pr = nx.pagerank(G, max_iter=255, tol=1e-16)
maxPR = max(pr.values())
flip = dict(zip(sorted(G.nodes(), key=lambda node: pr[node], reverse=True), range(0, G.number_of_nodes()) ))

### Plot 1
i=0
for edge in G.edges():
  x[i] = y[i + 1] = (1 - (pr[edge[0]] / maxPR))
  y[i] = x[i + 1] = (1 - (pr[edge[1]] / maxPR))
  z[i] = z[i + 1] = 1
  i += 2
ax1.scatter(x,y, c=z, s=z*20, alpha=0.2, cmap='seismic', vmin=z.min(), vmax=z.max(), linewidths=0)
ax1.set_xlabel('PR of Source Node')
ax1.set_ylabel('PR of Target Node')
ax1.set_title('Page Rank Value')

### Plot 2
i=0
for edge in G.edges():
    x[i] = y[i + 1] = flip[edge[0]]
    y[i] = x[i + 1] = flip[edge[1]]
    z[i] = com[edge[0]]
    z[i + 1] = com[edge[1]]
    i += 2
ax2.scatter(x,y, c=z, s=20, alpha=0.5, vmin=z.min(), vmax=z.max(), linewidths=0)
ax2.set_xlabel('Source Node')
ax2.set_ylabel('Target Node')
ax2.set_title('Adjacency Matrix ordered by Page Rank Value')

### Plot 3
i=0
for edge in G.edges():
  y[i] = (1 - (pr[edge[0]] / maxPR))
  x[i] = flip[edge[1]]
  y[i + 1] = (1 - (pr[edge[1]] / maxPR))
  x[i + 1] = flip[edge[0]]
  z[i] = z[i + 1] = 1
  i += 2
ax3.scatter(x,y, c=z, s=20, alpha=0.5, vmin=z.min(), vmax=z.max(), linewidths=0)
ax3.set_xlabel('Source Node Ordered by Page Rank Value')
ax3.set_ylabel('Target Node Page Rank Values')
ax3.set_title('Page Rank Order vs. Value')

evc = nx.eigenvector_centrality(G, max_iter=500, tol=.01)
maxEVC = max(evc.values())
flip = dict(zip(sorted(G.nodes(), key=lambda node: evc[node], reverse=True), range(0, G.number_of_nodes()) ))

### Plot 4
i=0
for edge in G.edges():
  x[i] = y[i + 1] = (1 - (evc[edge[0]] / maxEVC))
  y[i] = x[i + 1] = (1 - (evc[edge[1]] / maxEVC))
  z[i] = z[i + 1] = 1
  i += 2
ax4.scatter(x,y, c=z, s=z*20, alpha=0.2, cmap='seismic', vmin=z.min(), vmax=z.max(), linewidths=0)
ax4.set_xlabel('Eigenvector Centrality of Source Node')
ax4.set_ylabel('Eigenvector Centrality of Target Node')
ax4.set_title('Eigenvector Centrality Values')

### Plot 5
i=0
for edge in G.edges():
    x[i] = y[i + 1] = flip[edge[0]]
    y[i] = x[i + 1] = flip[edge[1]]
    z[i] = com[edge[0]]
    z[i + 1] = com[edge[1]]
    i += 2
ax5.scatter(x,y, c=z, s=20, alpha=0.5, vmin=z.min(), vmax=z.max(), linewidths=0)
ax5.set_xlabel('Source Node')
ax5.set_ylabel('Target Node')
ax5.set_title('Adjacency Matrix ordered by Eigenvector Centrality Value')

### Plot 6
i=0
for edge in G.edges():
  y[i] = (1 - (evc[edge[0]] / maxEVC))
  x[i] = flip[edge[1]]
  y[i + 1] = (1 - (evc[edge[1]] / maxEVC))
  x[i + 1] = flip[edge[0]]
  z[i] = z[i + 1] = 1
  i += 2
ax6.scatter(x,y, c=z, s=20, alpha=0.5, vmin=z.min(), vmax=z.max(), linewidths=0)
ax6.set_xlabel('Source Node Ordered by Eigenvector Centrality Value')
ax6.set_ylabel('Target Node Eigenvector Centrality Values')
ax6.set_title('Eigenvector Centrality Order vs. Value')

plt.show()
