import json
from pprint import pprint
import sys

from graph import Node, Graph

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

g = Graph()

for company in data.keys()[0:10]:
    g.add_nodes(company,data[company])

g.link_all_nodes()



for i in xrange(0,int(sys.argv[2])):
    for j in xrange(i,int(sys.argv[2])):
        print data.keys()[i]
        print data.keys()[j]
        pprint(g.return_links(data.keys()[i],data.keys()[j]))
