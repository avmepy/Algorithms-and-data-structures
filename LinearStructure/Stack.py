#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/23/18


class NodeForStack:
    """
    auxiliary class
    implements node of stack
    """
    def __init__(self, item=None):
        self.item = item  # load (value)
        self.next = None  # link to the next item in stack


class Stack:
    """
    class Stack
    """
    def __init__(self):
        """
        constructor
        """
        self.top_node = None  # the top item
        self.size = 0  # number of items in stack

    def empty(self):
        """
        chekc for emptiness
        :return: True - if stack is empty / False otherwise
        """
        return self.top_node is None

    def push(self, item):
        """
        add item to stack
        :param item: item
        :return:
        """
        self.size += 1
        new_node = NodeForStack(item)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        """
        extract item from stack
        (extracts the top item)
        :return: the top item
        """
        assert not self.empty(), 'Stack is empty!'
        current_top = self.top_node
        res_item = current_top.item
        self.top_node = self.top_node.next
        del current_top
        self.size -= 1
        return res_item

    def top(self):
        """
        return the top item without extraction
        :return: the top item
        """
        assert not self.empty(), 'Stack is empty!'
        return self.top_node.item

    def __len__(self):
        """
        :return: length (size of stack)
        """
        return self.size
