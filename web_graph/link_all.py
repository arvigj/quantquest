import json
from pprint import pprint
import sys
import numpy as np
from graph import Node, Graph

matrix = []

try:
    num = int(sys.argv[2])
except IndexError:
    num = 504

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

print(len(data))
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

mat = np.array(matrix,dtype=float)
print mat


for i in xrange(0,num):
    for j in xrange(0,num):
        if i!=j:
            mat[i][j] /= mat[i][i]

#normalize
def norm(array, identity_index, arr_len):
    length = 0
    for i in xrange(0,arr_len):
        if i == identity_index:
            continue
        length += array[i]
    for i in xrange(0,arr_len):
        if i == identity_index:
            continue
        array[i] = array[i]/length
    return array

#insert 1's after normalization
for i in xrange(0,num):
    mat[i][i] = 1
    mat[i] = norm(mat[i],i,num)

print(np.round(mat,3))

