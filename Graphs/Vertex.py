# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/29/18


class Vertex:
    """for the graph given by adjacency list"""
    def __init__(self, key=None, data=None):
        """
        constructor
        :param key: key
        :param data: data
        """
        self.key = key
        self.data = data
        self.neighbours = []

    def addNeighbor(self, neighbor):
        """
        adds the neighbor to the neighbours list
        :param neighbor: neighbor
        :return: None
        """
        self.neighbours.append(neighbor)

    def __str__(self):
        """for pretty print"""
        return 'key: ' + str(self.key) + ' ' + 'data: ' + str(self.data)

    def __repr__(self):
        """for pretty print"""
        return 'key: ' + str(self.key) + ' ' + 'data: ' + str(self.data)
