# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/30/18

from LinearStructure.Queue import Queue
from Graphs.Vertex import Vertex


def BFS(start: Vertex):
    """
    BFS for graph
    :param start: start vertex
    :return: all vertices have passed
    """
    q = Queue()
    q.push(start)
    visited = set()
    visited.add(start)

    while not q.empty():
        current = q.pop()
        print('{} -> '.format(current))

        for neighbour in current.neighbors:
            if neighbour not in visited:
                q.push(neighbour)
                visited.add(neighbour)
    return visited
