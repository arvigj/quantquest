#graph template file
# from spacy.en import *

class Node:
    #nlp = English()
    def __init__(self,name):
        self.name = name
        self.link_list = {}
        self.neighbors = {}
    def add_link(self,link):
        try:
            self.link_list[link] += 1
        except KeyError:
            self.link_list[link] = 1
    def add_neighbor(self,neighbor,neighbor_list):
        if neighbor in self.neighbors:
            return
        self.neighbors[neighbor] = []
        for i in self.link_list.keys():
            for j in neighbor.link_list.keys():
                if i==j:
                    self.neighbors[neighbor].append(i)

    # def add_neighbor_industry(self,neighbor,neighbor_list):
    #     if neighbor in self.neighbors:
    #         return
    #     self.neighbors[neighbor] = []
    #     for i in self.link_list.keys():
    #         for j in neighbor.link_list.keys():
    #             c1 = self.nlp(unicode(i))
    #             c2 = self.nlp(unicode(j))
    #             if (c1.similarity(c2)) > 0.5:
    #                 self.neighbors[neighbor].append(i)
    
    def get_neighbor_links(self,neighbor):
        return self.neighbors[neighbor]

class Graph:
    def __init__(self):
        self.comp_list = []
    def add_nodes(self,node,links):
        self.comp_list.append(Node(node))
        for link in links:
            self.comp_list[-1].add_link(link)
    def link_all_nodes(self):
        for i in self.comp_list:
            for j in self.comp_list:
                if i==j:
                    continue
                else:
                    i.add_neighbor(j,j.link_list)
    def link_all_industry(self):
        for i in self.comp_list:
            for j in self.comp_list:
                if i==j:
                    continue
                else:
                    i.add_neighbor_industry(j,j.link_list)

    def return_links(self,node_1, node_2):
        n2 = 0
        for i in self.comp_list:
            if node_1 == i.name:
                n1 = i
                continue
            if node_2 == i.name:
                n2 = i
        if node_1 == node_2:
            return n1.link_list.keys()
        return n1.get_neighbor_links(n2)



