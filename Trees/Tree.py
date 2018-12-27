# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/26/18

from Trees.TreeNode import TreeNode


class Tree:
    """ class Tree """
    def __init__(self, root=None):
        """
        constructor
        :param root: the root of the tree
        """
        self.root = root
        self.nodes = []

    def setRoot(self, root: TreeNode):
        """
        sets the root
        :param root: new root
        :return: None
        """
        self.root = root


# for test
def createSampleTree() -> Tree:
    vertices = [TreeNode(key=i) for i in range(6)]  # initialize 6 vertices
    vertices[0].addChild(vertices[1])
    vertices[0].addChild(vertices[2])
    vertices[2].addChild(vertices[3])
    vertices[2].addChild(vertices[4])
    vertices[3].addChild(vertices[5])
    # got the next tree
    #   0
    #  / \
    # 1   2
    #    / \
    #   3   4
    #   |
    #   5
    tree = Tree(vertices[0])  # initialize vertex 0 as root
    return tree
