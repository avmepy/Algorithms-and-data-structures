#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/26/18


class TreeNode:
    """
    auxiliary class
    implements the node of tree
    """
    def __init__(self, key=None):
        """
        constructor
        :param key: the key of the node
        """
        self.key = key

    def empty(self):
        """
        check for emptiness
        :return:
        """
        return self.key is None

    def setkey(self, newKey):
        """
        sets the node key
        :param newKey: new key
        :return:
        """
        self.key = newKey

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
