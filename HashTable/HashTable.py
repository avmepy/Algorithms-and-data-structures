# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/28/18


class HashTable:
    def __init__(self, size=100, hash=None):
        """
        constructor
        :param size: the size of the table
        :param hash: the hash function
        """
        if hash is None:
            hash = lambda _: _ % size
        self.table = [[] for _ in range(size)]
        self.size = size
        self.hash = hash

    def __str__(self):
        """
        for pretty print
        :return: table (list)
        """
        return str(self.table)

    def push(self, item):
        """
        adds the item into the table
        :param item: new item
        :return: None
        """
        index = self.hash(item)
        self.table[index].append(item)

    def __contains__(self, item):
        """
        method __in__
        check
        does the element belong to the table
        :param item: item
        :return: True / False
        """
        index = self.hash(item)
        return item in self.table[index]

    def remove(self, item):
        """
        removes the item from the table
        :param item: item
        :return: None
        """
        assert item in self, 'table doesn\'t contain the item'
        index = self.hash(item)
        self.table[index].remove(item)


if __name__ == '__main__':
    # for test
    table1 = HashTable(10)
    table1.push(5487)
    table1.push(208374)
    table1.push(387298)
    table1.push(1)
    table1.push(3847)
    table1.push(37620504)
    table1.push(498)
    table1.push(387)
    table1.push(56)
    table1.push(70)
    table1.remove(498)
    print(table1)
    print(70 in table1, 5487 in table1, 1 in table1, 0 in table1)
