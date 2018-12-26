#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/25/18


class NodeForDeque:
    """
    auxiliary class
    implements a node of deque
    """
    def __init__(self, item):
        """
        constructor
        :param item: item
        """
        self.item = item
        self.next = None
        self.prev = None


class Deque:
    """
    class deque
    """

    def __init__(self):
        """
        constructor
        creates an empty deque
        """
        self.size = 0
        self.mFront = None  # link to the first item in deque
        self.mBack = None   # link to the last item in deque

    def empty(self):
        """
        check for emptiness
        :return: True - if deque is empty / False - otherwise
        """
        return self.mFront is None and self.mBack is None

    def pushFront(self, item):
        """
        add the item to the top of deque
        :param item: item hat is being added
        :return: None
        """
        self.size += 1
        node = NodeForDeque(item)
        node.next = self.mFront
        if not self.empty():
            self.mFront.prev = node
        else:
            self.mBack = node
        self.mFront = node

    def popFront(self):
        """
        returns the item from the top of deque
        :return: the top item
        """
        if self.empty():
            raise Exception('popFront: Deque is empty')
        self.size -= 1
        node = self.mFront
        item = node.item
        self.mFront = node.next
        if self.mFront is None:
            self.mBack = None
        else:
            self.mFront.prev = None
        del node
        return item

    # methods pushFront and popFront are symmetric pushBack and popBack respectively
    def pushBack(self, item):
        """
        add the item to the back of deque
        :param item: item hat is being added
        :return: None
        """
        self.size += 1
        elem = NodeForDeque(item)
        elem.prev = self.mBack
        if not self.empty():
            self.mBack.next = elem
        else:
            self.mFront = elem
        self.mBack = elem

    def popBack(self):
        """
        returns the item from the back of deque
        :return: the top item
        """
        self.size -= 1
        if self.empty():
            raise Exception('popBack: Deque is empty')
        node = self.mBack
        item = node.item
        self.mBack = node.prev
        if self.mBack is None:
            self.mFront = None
        else:
            self.mBack.next = None
        del node
        return item

    def front(self):
        if self.empty():
            return 'error'
        tmp = self.popFront()
        self.pushFront(tmp)
        return tmp

    def back(self):
        if self.empty():
            return 'error'
        tmp = self.popBack()
        self.pushBack(tmp)
        return tmp

    def __len__(self):
        """
        :return: size of deque 
        """
        return self.size
