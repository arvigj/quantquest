import json
from pprint import pprint
import sys
import numpy as np

from graph import Node, Graph

matrix = []

try:
    num = int(sys.argv[2])
except IndexError:
    num = 500

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

g = Graph()

for company in data.keys()[0:num]:
    g.add_nodes(company,data[company])

g.link_all_nodes()


for i in xrange(0,num):
    matrix.append([])
    print(str(i)+"\t"+data.keys()[i])
    for j in xrange(0,num):
        a = g.return_links(data.keys()[i],data.keys()[j])
        if a is None:
            a = []
        matrix[i].append(len(a))

mat = np.matrix(matrix)

#print type(mat)
#print type(mat[0])
#print type(mat[0][0])

#for i in xrange(0,num):
#    for j in xrange(0,num):
#        mat[i][0][j] = mat[i][0][j] / mat[i][0][i]

print mat
