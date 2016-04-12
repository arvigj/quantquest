import json
from pprint import pprint
import sys
import numpy as np

from tsne import tsne
import matplotlib.pyplot as plt

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

mat = np.array(matrix,dtype=float)

#print type(mat)
#print type(mat[0])
#print type(mat[0][0])

for i in xrange(0,num):
    for j in xrange(0,num):
        if i!=j:
            mat[i][j] /= mat[i][i]

#remove 1's before normalization
#for i in xrange(0,num):
#    mat[i,i] = 0


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



# print(np.round(mat,3))


for i in xrange(0,num):
    mat[i,i] = 0


Y = tsne(mat, 2, num, 5)
print len(Y[:,0])
print len(Y[:,1])
plt.scatter(Y[:,0], Y[:,1])
plt.show()
#Plot.show()


# import matplotlib.pyplot as plt
# import numpy as np
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)

# N = num
# x = mat[:,0]
# print(x)
# y = mat[:,1]
# points = mat[:,:]
# # color is the length of each vector in `points`
# color = np.sqrt((points**2).sum(axis = 1))/np.sqrt(2.0)
# rgb = plt.get_cmap('jet')(color)

# ax.scatter(x, y, color = rgb)
# plt.show()

