import json
from pprint import pprint
import sys
import numpy as np
from graph import Node, Graph

def get_industry_matrix(nameOfFile, size):
	matrix = []
	try:
	    num = size
	except IndexError:
	    num = 504

	with open(nameOfFile) as data_file:
	    data = json.load(data_file)

	g = Graph()
	for company in data.keys()[0:num]:
		g.add_nodes(company,data[company])

	g.link_all_industry()


	for i in xrange(0,num):
	    matrix.append([])
	    print(str(i)+"\t"+data.keys()[i])
	    for j in xrange(0,num):
	        a = g.return_links(data.keys()[i],data.keys()[j])
	        if a is None:
	            a = []
	        matrix[i].append(len(a))


	mat = np.array(matrix,dtype=float)
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
	        if length != 0:
	            array[i] = array[i]/length
	    return array

	for i in xrange(0,num):
	    mat[i][i]=1
	    mat[i] = norm(mat[i],i,num)

	mat = (np.round(mat,3))
	mat = np.multiply(mat, 0.4)
	return mat

def get_linkage_matrix(nameOfFile, size):
	matrix = []

	try:
	    num = size
	except IndexError:
	    num = 504

	with open(nameOfFile) as data_file:
	    data = json.load(data_file)

	g = Graph()

	for company in data.keys()[0:num]:
	    g.add_nodes(company,data[company])

	g.link_all_nodes()


	for i in xrange(0,num):
	    matrix.append([])
	    # print(str(i)+"\t"+data.keys()[i])
	    for j in xrange(0,num):
	        a = g.return_links(data.keys()[i],data.keys()[j])
	        if a is None:
	            a = []
	        matrix[i].append(len(a))

	mat = np.array(matrix,dtype=float)
	# print mat


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

	mat = np.round(mat,3)
	mat = np.multiply(mat, 0.6)
	return mat

def add_matrices(matrix1, matrix2):
	return np.add(matrix1, matrix2)


print("INDUSTRY MATRIX")
mat1 = get_industry_matrix(sys.argv[1], int(sys.argv[3]))
print(mat1)

print("LINKAGE MATRIX")
mat2 = get_linkage_matrix(sys.argv[2], int(sys.argv[3]))
print(mat2)

print("FINAL MATRIX")
fin_mat = add_matrices(mat1, mat2)
print(fin_mat)

import csv
with open("matrix.csv", "w") as f:
	for i in fin_mat:
	    for j in i:
	        f.write(str(j)+",")
	    f.write("\n")
