# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/31/18

from Graphs.Vertex import Vertex
from LinearStructure.Queue import Queue


def wave(start: Vertex) -> dict:
    """
    Wave algorithm using an array
    distances from the starting point to the current one
    to determine if the peak has already been visited
    :param start: start vertex
    :return: dictionary of distances
    """
    q = Queue()
    q.push(start)
    distances = {start: 0}

    while not q.empty():
        current = q.pop()
        for neighbour in current.neighbors:
            if neighbour not in distances:
                q.push(neighbour)
                distances[neighbour] = distances[current] + 1
    return distances
