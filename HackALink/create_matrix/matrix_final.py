import json
from pprint import pprint
import sys
import numpy as np
from graph import Node, Graph

'''
CREATING THE INDUSTRY MATRIX
The industry matrix essentially creates a graph that links companies
in accordance to their industries. We use nlp techniques in order to
create the links between similar industries and weigh them according
to the logic dicussed in our write up.
'''
def get_industry_matrix(nameOfFile, size):
	matrix = []
	try:
	    num = size
	except IndexError:
	    num = 504

	#Collecting data from the industry.json. This file 
	#gives the details of the industry
	with open(nameOfFile) as data_file:
	    data = json.load(data_file)

	g = Graph()

	#Creating nodes
	for company in data.keys()[0:num]:
		g.add_nodes(company,data[company])

	#Adding these nodes in a graph by considering
	#the links. In order to create the links and do significant
	#comparisons we take into consideration semantic analysis using NLP (spacy).
	#We compare the different descriptions about a particular company's industry
	#to other companies and check for the linkages in accordance to those values.
	g.link_all_industry()


	#Creating teh matrix
	for i in xrange(0,num):
	    matrix.append([])
	    print(str(i)+"\t"+data.keys()[i])
	    for j in xrange(0,num):
	        a = g.return_links(data.keys()[i],data.keys()[j])
	        if a is None:
	            a = []
	        matrix[i].append(len(a))


	#Alloting the scores in accordance to the number of links to a given
	#company
	mat = np.array(matrix,dtype=float)
	for i in xrange(0,num):
	    for j in xrange(0,num):
	        if i!=j:
				if(mat[i][i] != 0):
					mat[i][j] /= mat[i][i]

	#normalize to get the value to be a perfect 100%
	def norm(array, identity_index, arr_len):
	    length = 0
	    for i in xrange(0,arr_len):
	        if i == identity_index:
	            continue
	        length += array[i]
		if length == 0:
			return array
	    for i in xrange(0,arr_len):
	        if i == identity_index:
	            continue
	        if length != 0:
	            array[i] = array[i]/length
	    return array

	for i in xrange(0,num):
	    mat[i][i]=1
	    mat[i] = norm(mat[i],i,num)

	#mat = (np.round(mat,3))

	#Giving the value a 40% percent for the final matrix
	mat = np.multiply(mat, 0.4)
	return mat


'''
CREATING THE LINKAGE MATRIX
"Page Rank" is possibly one of the most important algorithms that was developed
and implemented to make our search engines the way they are. Applying the logic
of the "links" pointing out of a page we try to observe which companies have
similar links going out. 
'''
def get_linkage_matrix(nameOfFile, size):
	matrix = []

	try:
	    num = size
	except IndexError:
	    num = 504

	#Collecting data from the links.json. This file essentially has all
	#the wikipedia links coming out of a particular company's page.
	with open(nameOfFile) as data_file:
	    data = json.load(data_file)

	g = Graph()

	#Creating nodes
	for company in data.keys()[0:num]:
	    g.add_nodes(company,data[company])

	#Adding these nodes in a graph by considering
	#the common links. Here we check for direct equivalence. Unlike
	#the industry graph where we take into consideration semantics and using
	#NLP techniques
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

	#Alloting the scores in accordance to the number of links to a given
	#company
	for i in xrange(0,num):
	    for j in xrange(0,num):
	        if i!=j:
				if mat[i][i] != 0:
					mat[i][j] /= mat[i][i]

	#normalize
	def norm(array, identity_index, arr_len):
	    length = 0
	    for i in xrange(0,arr_len):
	        if i == identity_index:
	            continue
	        length += array[i]
            if length == 0:
                return array
	    for i in xrange(0,arr_len):
	        if i == identity_index:
	            continue
	        array[i] = array[i]/length
	    return array

	#insert 1's after normalization
	for i in xrange(0,num):
	    mat[i][i] = 1
	    mat[i] = norm(mat[i],i,num)

	#mat = np.round(mat,3)
	mat = np.multiply(mat, 0.6)
	return mat

def add_matrices(matrix1, matrix2):
	return np.add(matrix1, matrix2)


try:
	file1 = sys.argv[1]
except:
	file1 = "industry.json"
try:
	file2 = sys.argv[2]
except:
	file2 = "links.json"
try:
	size = int(sys.argv[3])
except:
	size = 504

print("INDUSTRY MATRIX")
mat1 = get_industry_matrix(file1, size)
print(mat1)

print("LINKAGE MATRIX")
mat2 = get_linkage_matrix(file2, size)
print(mat2)


'''
The final matrix essentially combines the industry and linkage matrix
to produce a final result. 60 per cent weight is given to the linkage
matrix and 40 per cent weight is given to the industry matrix.

We decided this weighing scale because of the amount and quality data that we had
for the respective paramters.
'''

print("FINAL MATRIX")
fin_mat = add_matrices(mat1, mat2)
print(fin_mat)

import csv
with open("matrix.csv", "w") as f:
	for i in fin_mat:
	    for j in i:
	        f.write(str(j)+",")
	    f.write("\n")
