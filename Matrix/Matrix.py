#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/23/18

import random


class Matrix:
    """
    class for matrix
    """
    def __init__(self, q=list()):
        """
        constructor
        the matrix must be given by a list (vector) or a list of lists (matrix)
        :param q: list
        """
        if not isinstance(q[0], list):
            for i in range(len(q)):
                q[i] = [q[i]]
        self.m = q

    def __getitem__(self, index):
        """
        returns item by index
        :param index: index
        :return: desired item
        """
        return self.m[index]

    def __setitem__(self, key, value):
        """
        sets item by index
        :param key: index
        :param value: new value (new item)
        """
        self.m[key] = value

    def __contains__(self, item):
        """
        redefinition method 'in'
        :param item:
        :return: True if item is in matrix / False otherwise
        """
        return item in self.m

    def __str__(self):
        """
        for pretty print
        :return:
        """
        res = ''
        for row in self:
            res += '{}\n'.format(row)
        res.rstrip('\n')
        return res

    def __repr__(self):
        """
        for pretty print
        :return:
        """
        res = ''
        for row in self:
            res += '{}\n'.format(row)
        res.rstrip('\n')
        return res

    def shape(self):
        """
        returns the sizes of matrix
        :return: tuple (n, k) sizes of matrix
        """
        n = len(self.m)
        k = 1
        if isinstance(self.m[0], list):
            k = len(self.m[0])
        return n, k

    @staticmethod
    def eye(n):
        """
        creates unit matrix nxn
        :param n: size
        :return: unit ,atrix
        """
        new = Matrix([[0 for _ in range(n)] for _ in range(n)])
        for i in range(n):
            for j in range(n):
                if i == j:
                    new[i][j] = 1
        return new

    @staticmethod
    def zeros(n, k):
        """
        creates zeros matrix nxk
        :param n: size, number of rows
        :param k: size, number of columns
        :return: zeros matrix
        """
        return Matrix([[0 for _ in range(k)] for _ in range(n)])

    def __add__(self, other):
        """
        matrix addition
        :param other: other matrix
        :return: result of addition
        """
        n, k = self.shape()
        n2, k2 = other.shape()
        assert n == n2 and k == k2, 'INVALID matrix size'
        new = Matrix.zeros(n, k)
        for i in range(n):
            for j in range(k):
                new[i][j] = self[i][j] + other[i][j]
        return new

    def __sub__(self, other):
        """
        matrix subtraction
        :param other: other matrix
        :return: result of subtraction
        """
        n, k = self.shape()
        n2, k2 = other.shape()
        assert n == n2 and k == k2, 'INVALID matrix size'
        new = Matrix.zeros(n, k)
        for i in range(n):
            for j in range(k):
                new[i][j] = self[i][j] - other[i][j]
        return new

    def transpose(self):
        """
        :return: transposed matrix
        """
        n, k = self.shape()
        new = Matrix.zeros(k, n)
        for i in range(n):
            for j in range(k):
                new[j][i] = self[i][j]
        return new

    def __eq__(self, other):
        """
        redefinition method '=='
        :param other: other matrix
        :return: True if matrices are equal/ False otherwise
        """
        n, k = self.shape()
        n2, k2 = other.shape()
        assert n == n2 and k == k2, 'INVALID matrix size'
        success = True
        for i in range(n):
            for j in range(k):
                if self[i][j] != other[i][j]:
                    success = False
                    break
        return success

    def __mul__(self, other):
        """
        matrix multiplication
        :param other: other matrix
        :return: result of multiplication
        """
        n1, k1 = self.shape()
        k2, m2 = other.shape()
        assert k1 == k2, 'INVALID matrix size'
        new = Matrix.zeros(n1, m2)
        for i in range(n1):
            for j in range(k1):
                for k in range(m2):
                    new[i][k] += self[i][j] * other[j][k]
        return new

    def __pow__(self, power):
        """
        matrix exponentiation
        :param power: power
        :return: result of exponentiation
        """
        new = Matrix(self.m)
        for i in range(power-1):
            new *= self
        return new

    def __hash__(self):
        """
        to get hash
        :return: hash code
        """
        return str.__hash__(str(self.m))

    @staticmethod
    def getRandomMatrix(n=None, m=None):
        """
        create random matrix nxm
        :param n: random if not given
        :param m: random if not given
        :return: random matrix
        """
        if not n or not m:
            n = random.randint(1, 30)
            m = random.randint(1, 30)
        new = Matrix.zeros(n, m)
        for i in range(n):
            for j in range(m):
                new[i][j] = random.randint(-100, 100)
        return new
