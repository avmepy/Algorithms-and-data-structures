# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/27/18

from LinearStructure.Queue import Queue
from Trees.Tree import Tree, createSampleTree


def BFS(tree: Tree):
    """
    bfs in the tree
    :param tree: tree
    :return: None
    """
    q = Queue()  # use queue for bfs
    q.push(tree.root)  # first add the root

    while not q.empty():
        current = q.pop()
        print('{} -> '.format(current), end='')  # print key

        for child in current.children:  # then add children
            q.push(child)


if __name__ == '__main__':
    # for test
    tree = createSampleTree()
    BFS(tree)
