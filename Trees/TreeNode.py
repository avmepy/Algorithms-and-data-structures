#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/26/18


class TreeNode:
    """
    auxiliary class
    implements the node of the tree
    """
    def __init__(self, key=None, father=None):
        """
        constructor
        :param key: the key of the node
        :param father: the father of the node (link)
        """
        self.key = key
        self.father = father
        self.children = []

    def empty(self):
        """
        check for emptiness
        :return: True / False
        """
        return self.key is None

    def setkey(self, newKey):
        """
        sets the node key
        :param newKey: new key
        :return: None
        """
        self.key = newKey

    def addChild(self, child):
        """
        adds child
        :param child: child (type: TreeNode)
        :return: None
        """
        self.children.append(child)

    def __str__(self):
        """
        for pretty print
        :return: the node key
        """
        return str(self.key)

    def __repr__(self):
        """
        for pretty print
        :return: the node key
        """
        return str(self.key)

    def hasChildren(self):
        """
        :return: True if node has children / False otherwise
        """
        return self.children != []
