# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/27/18


class BinaryTreeNode:
    """
    auxiliary class
    implements the node of the binary tree
    """
    def __init__(self, key=None, left=None, right=None, father=None):
        """
        constructor
        :param key: key
        :param left: leftChild
        :param right: rightChild
        :param father: father
        """
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.father = father

    @property
    def children(self):
        """for bfs and dfs"""
        return self.leftChild, self.rightChild

    def setFather(self, father):
        self.father = father

    def setLeftChild(self, child):
        self.leftChild = child

    def setRightChild(self, child):
        self.rightChild = child

    def setKey(self, new):
        self.key = new
