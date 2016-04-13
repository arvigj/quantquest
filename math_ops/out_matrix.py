import numpy as np

def add_matrices(matrix_list, weight_list):
    matrix = []
    for i in matrix_list[0]:
        matrix.append([])
        for j in matrix_list[0][i]:
            matrix[i].append(weight_list[0]*j)

    ##insert into csv file
    with open("matrix.csv", "w") as f:
        for i in matrix:
            for j in i:
                f.write(str(j)+",")
            f.write("\n")

def length(u):
    leng = 0
    for i in u:
        leng+=i*i
    return np.sqrt(leng)

def cosines(u ,v):
    dot = np.dot(u,v)
    angle = dot/(length(u)*length(v))
    angle = np.arccos(angle)
    angle = angle * (180./np.pi)
    return angle

