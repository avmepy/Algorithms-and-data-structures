# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/28/18

""" There are some hash functions """

N = 100  # size


def hash_num(item) -> int:
    """
    for numbers only
    :param item: item
    :return: hash
    """
    return item % N


def has_str(item: str) -> int:
    """
    for strings
    :param item: item
    :return: hash
    """
    return sum([ord(item[i]) * 2 ** i for i in range(len(item))]) % N
