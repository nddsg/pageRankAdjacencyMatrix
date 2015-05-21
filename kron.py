import product
import networkx as nx
from PIL import Image, ImageDraw
import random

k = 7
P = [[1,1,0],[0,1,0],[0,1,1]]
G = product.kronecker_random_graph(k,P)
for u,v in G.selfloop_edges():
  G.remove_edge(u,v)

pr = nx.pagerank(G)
maxPR = max(pr.values())

filename = 'kronecker'

size = 1000
rectWidth = 10

im = Image.new("RGB", (size, size), "white")
draw = ImageDraw.Draw(im)

for edge in G.edges():
  x = (1 - (pr[edge[0]] / maxPR)) * (size - rectWidth - rectWidth) + rectWidth
  y = (1 - (pr[edge[1]] / maxPR)) * (size - rectWidth - rectWidth) + rectWidth
  draw.rectangle([x, y, x + rectWidth, y + rectWidth], fill='black')
  draw.rectangle([y, x, y + rectWidth, x + rectWidth], fill='black')
im.save('/var/www/html/graphlab-doc/' + filename + '.scale.png')

nodes = G.nodes()
random.shuffle(nodes)
order = sorted(nodes, key = lambda node: pr[node], reverse = True)
flipped = [0] * len(order)
for index in range(len(order)):
  flipped[order[index]] = index

size = len(order)
im = Image.new("RGB", (size,size), "white")
im2 = Image.new("RGB", (size,size), "white")
draw = ImageDraw.Draw(im)
draw2 = ImageDraw.Draw(im2)
for edge in G.edges():
  draw.point((flipped[edge[0]], flipped[edge[1]]), fill="black")
  draw.point((flipped[edge[1]], flipped[edge[0]]), fill="black")
  draw2.point((edge[0], edge[1]), fill="black")
  draw2.point((edge[1], edge[0]), fill="black")
im.save('/var/www/html/graphlab-doc/' + filename + '.adj.png')
im2.save('/var/www/html/graphlab-doc/' + filename + '.kron.png')
