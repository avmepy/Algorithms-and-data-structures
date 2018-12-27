# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/27/18


from Trees.TreeNode import TreeNode
from Trees.Tree import createSampleTree, Tree


def _dfsHelper(current: TreeNode):
    """
    auxiliary function for dfs
    :param current: current tree vertex
    :return: None
    """
    print('{} -> '.format(current), end='')  # print current vertex
    for child in current.children:  # run _dfsHelper for every child
        _dfsHelper(child)


def DFS(tree: Tree):
    """
    dfs in the tree
    :param tree: tree
    :return: None
    """
    root = tree.root
    _dfsHelper(root)  # starting from the root


if __name__ == '__main__':
    # for test
    tree = createSampleTree()
    DFS(tree)
