import numpy as np
import json
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


all_vectors = {}
counter = 0
with open("time.json", 'r') as time_file:
	time_data = json.load(time_file)

for each in time_data:
	if(counter == 10):
		break
	all_vectors[each] = np.array([time_data[each]-1900])
	counter = counter +1

# counter = 0
# with open("employees.json", 'r') as employees_file:
# 	emp_data = json.load(employees_file)

# for each in emp_data:
# 	if(counter == 10):
# 		break
# 	all_vectors[each].append(emp_data[each])
# 	counter = counter +1

print(all_vectors)