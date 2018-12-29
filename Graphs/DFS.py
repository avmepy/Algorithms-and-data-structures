# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/29/18

from Graphs.Graph import Graph
from Graphs.Vertex import Vertex


def _dfsHelper(graph: Graph, visited: set, start: Vertex):
    """
    auxiliary function to DFS
    :param graph: graph
    :param visited: set visited vertices
    :param start: start vertx
    :return: None
    """
    visited.add(start)
    for neighbour in start.neighbours:
        if neighbour not in visited:
            _dfsHelper(graph, visited, neighbour)


def DFS(graph: Graph, start: Vertex) -> set:
    """
    DFS for graph
    :param graph: graph
    :param start: start vertex
    :return: all vertices have passed
    """
    visited = set()
    _dfsHelper(graph, visited, start)
    return visited
