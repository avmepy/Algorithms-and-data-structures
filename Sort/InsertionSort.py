#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/25/18


def InsertionSort(items, key=lambda _: _, reverse=False):
    """
    insertion sorting implementation
    :param items:  item to sort (must be iterable)
    :param key: sort key (function)
    :param reverse: return reverse if True
    :return: sorted item
    """
    n = len(items)
    for i in range(1, n):
        curVal = items[i]
        curPos = i
        while curPos > 0:
            if key(items[curPos-1]) > key(curVal):
                items[curPos] = items[curPos-1]
            else:
                break
            curPos -= 1
        items[curPos] = curVal
    if reverse:
        items = items[::-1]
    return items


if __name__ == '__main__':
    # for test
    t1 = [5, 3, 0, 6, 3, 8, 4, 7, 1, 8, 0, -7, 4, -19, 56, 322, 5, 78, -0.9, 0.75]
    print(InsertionSort(t1))
    t2 = ['lkg', 'skdjs', 'kdfjgdfkfgd', '128412', 'dkjgkdjskgjkjdfgld', '-40kdsjsje']
    print(InsertionSort(t2, key=lambda string: len(string)))  # sort by line length
    # sort by the sum of the numeric representations of the characters in a string
    print(InsertionSort(t2, key=lambda string: sum([ord(i) for i in string])))
