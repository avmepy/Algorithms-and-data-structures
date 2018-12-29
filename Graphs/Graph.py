# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/29/18

from Graphs.Vertex import Vertex


class GraphByMatrix:
    """ graph defined by adjacency matrix """
    def __init__(self, n=0, m=None, oriented=False):
        """
        constructor
        :param n: number if vertices in the graph
        :param m: adjacency matrix
        :param oriented: True if the graph is oriented / False - otherwise
        """
        if m is None:
            m = [[0 for _ in range(n)]for _ in range(n)]
        self.matrix = m
        self.size = n
        self.oriented = oriented

    def setMatrix(self, matrix):
        """
        sets the adjacency matrix
        :param matrix: adjacency matrix
        :return: None
        """
        self.matrix = matrix

    def addEdge(self, v1, v2, data=1):
        """
        adds the edge to the graph
        :param v1: start vertex
        :param v2: end vertex
        :param data: the data
        :return: None
        """
        self.matrix[v1][v2] = data
        if not self.oriented:
            self.matrix[v2][v1] = data

    def removeEdge(self, v1, v2):
        """
        removes the edge from the graph
        :param v1: start vetrex
        :param v2: end vertex
        :return: None
        """
        self.matrix[v1][v2] = 0
        if not self.oriented:
            self.matrix[v2][v1] = 0

    def __str__(self):
        """for pretty print"""
        res = ''
        for row in self.matrix:
            res += str(row) + '\n'
        res.rstrip('\n')
        return res


class Graph:
    """ graph defined by adjacency list """
    def __init__(self, oriented=False):
        """
        constructor
        :param oriented: True if the graph is oriented / False - otherwise
        """
        self.oriented = oriented
        self.vertices = []

    def addVertex(self, vertex: Vertex):
        """
        adds the vertex to the graph
        :param vertex: vertex
        :return: None
        """
        self.vertices.append(vertex)

    def addEdge(self, v1: Vertex, v2: Vertex):
        """
        adds the edge to the graph
        :param v1: start vertex
        :param v2: end vertex
        :return: None
        """
        v1.addNeighbor(v2)
        if not self.oriented:
            v2.addNeighbor(v1)


if __name__ == '__main__':
    # for test
    #  # 1
    G = GraphByMatrix(4)
    G.addEdge(0, 1)
    G.addEdge(1, 2)
    G.addEdge(2, 3)
    G.addEdge(0, 3)
    G.addEdge(0, 2)
    G.addEdge(3, 1)
    G.removeEdge(3, 1)
    # got the next graph
    #  0 - 1
    #  | \ |
    #  3 - 2
    print(G)

    #  # 2
    # the same graph
    H = Graph()
    vertices = [Vertex(i) for i in range(4)]
    for vertex in vertices:
        H.addVertex(vertex)
    H.addEdge(vertices[0], vertices[1])
    H.addEdge(vertices[1], vertices[2])
    H.addEdge(vertices[2], vertices[3])
    H.addEdge(vertices[0], vertices[3])
    H.addEdge(vertices[0], vertices[2])
    print([i for i in H.vertices])
