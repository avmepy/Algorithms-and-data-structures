#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/25/18


class NodeForQueue:
    def __init__(self, item):
        self.key = item
        self.next = None


class Queue:
    def __init__(self):
        self.mFront = None
        self.mBack = None
        self.size = 0

    def empty(self):
        return self.size == 0

    def push(self, item):
        pass

    def __len__(self):
        return self.size
