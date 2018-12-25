#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/25/18


class NodeForQueue:
    """
    auxiliary class
    implement node of queue
    """
    def __init__(self, item=None):
        self.item = item  # load (value) element
        self.next = None  # link to next item in queue


class Queue:
    """
    class Queue
    """
    def __init__(self):
        """
        constructor
        """
        self.m_front = None  # the first item
        self.m_back = None  # the last item
        self.size = 0  # length of queue

    def empty(self):
        """
        :return: True - if queue is empty / False - otherwise
        """
        return self.m_front is None and self.m_back is None

    def push(self, item):
        """
        add item to queue
        :param item: item
        :return:
        """
        self.size += 1
        new_node = NodeForQueue(item)
        if self.empty():
            self.m_front = new_node
        else:
            self.m_back.next = new_node
        self.m_back = new_node

    def pop(self):
        """
        extract item from queue
        :return: the first item
        """
        assert not self.empty(), 'Queue is empty!'
        current_front = self.m_front
        item = current_front.item
        self.m_front = self.m_front.next
        del current_front
        self.size -= 1
        if self.m_front is None:
            self.m_back = None
        return item

    def front(self):
        """
        return the first item without extraction
        :return: the first item
        """
        assert not self.empty(), 'Queue is empty!'
        return self.m_front.item

    def __len__(self):
        """
        :return: size of queue
        """
        return self.size
