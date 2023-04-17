# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 21:29:04 2023

@author: cesl
"""

class grafo:
    def __init__(self, directed=False, weighted=True):
        self.nodes = {}
        self.directed = directed
        self.weighted = weighted

    def addNode_byValue(self, node):
        if node not in self.nodes:
            self.nodes[node] = {}
    

    def addEdge_byValue(self, node1, node2, weight=None):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        if self.weighted:
            self.nodes[node1][node2] = weight
            if not self.directed:
                self.nodes[node2][node1] = weight
        else:
            self.nodes[node1][node2] = 1
            if not self.directed:
                self.nodes[node2][node1] = 1

    def deleteNode_byValue(self, node):
        if node in self.nodes:
            del self.nodes[node]
            for adj_nodes in self.nodes.values():
                if node in adj_nodes:
                    del adj_nodes[node]

    def getNodeValues(self):
        return list(self.nodes.keys())

    def isNodeValue(self, node):
        return node in self.nodes

    def findAdjacentNode(self, node):
        if node in self.nodes:
            return list(self.nodes[node].keys())
        return []
    
    def algorithms(self, algoritmo, infoNodo=None):
        return False
    
    def getEdgeValues(self):
        edge_values = []
        for node1 in self.nodes:
            for node2 in self.nodes[node1]:
                if self.weighted:
                    edge_values.append((node1, node2, self.nodes[node1][node2]))
                else:
                    edge_values.append((node1, node2, self.nodes[node1][node2]))
        return edge_values
