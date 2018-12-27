# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/27/18

from Trees.BinaryTreeNode import BinaryTreeNode


class BinaryTree:
    """class Binary Tree"""
    def __init__(self, root=None):
        self.root = root
        self.nodes = []

    def addNode(self, node: BinaryTreeNode):
        self.nodes.append(node)

    def setRoot(self, root: BinaryTreeNode):
        """
        sets the root
        :param root: new root
        :return: None
        """
        self.root = root
