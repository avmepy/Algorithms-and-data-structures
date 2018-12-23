#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/23/18

import random


class Matrix:
    """
    класс для матриц
    """
    def __init__(self, q=list()):
        """
        коснтруктор
        матрица задается списком (вектор) или списком списков (матрица)
        :param q:
        """
        if not isinstance(q[0], list):
            for i in range(len(q)):
                q[i] = [q[i]]
        self.m = q

    def __getitem__(self, item):
        """
        возвращает элемент по индексу
        :param item: индекс
        :return:
        """
        return self.m[item]

    def __setitem__(self, key, value):
        """
        устанавливает элемент по индексу
        :param key: индекс
        :param value: новое значение
        :return:
        """
        self.m[key] = value

    def __contains__(self, item):
        """
        переопределение метода 'in'
        :param item:
        :return:
        """
        return item in self.m

    def __str__(self):
        """
        метод ля вывода
        :return:
        """
        res = ''
        for row in self:
            res += '{}\n'.format(row)
        res.rstrip('\n')
        return res

    def __repr__(self):
        """
        метод для вывода
        :return:
        """
        res = ''
        for row in self:
            res += '{}\n'.format(row)
        res.rstrip('\n')
        return res

    def shape(self):
        """
        возвращает размер матрицы
        :return: кортеж (n, k) матрицы nxk
        """
        n = len(self.m)
        k = 1
        if isinstance(self.m[0], list):
            k = len(self.m[0])
        return n, k

    @staticmethod
    def eye(n):
        """
        возвращает единичную матрицу nxn
        :param n: размер матрицы
        :return:
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
        возвращает матрицу nxk заполненную нулями
        :param n:
        :param k:
        :return:
        """
        return Matrix([[0 for _ in range(k)] for _ in range(n)])

    def __add__(self, other):
        """
        сложение матриц
        :param other:
        :return: результат матричного сложения
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
        вычитание матриц
        :param other:
        :return:
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
        возвращает транспонированную матрицу
        :return:
        """
        n, k = self.shape()
        new = Matrix.zeros(k, n)
        for i in range(n):
            for j in range(k):
                new[j][i] = self[i][j]
        return new

    def __eq__(self, other):
        """
        переопределение метода '=='
        :param other:
        :return: True, если две матрицы равны (поэлементно) / False, в противном случае
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
        умножение матриц
        :param other:
        :return:
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
        возведение матрицы в степень
        :param power: степень
        :return:
        """
        new = Matrix(self.m)
        for i in range(power-1):
            new *= self
        return new

    def __hash__(self):
        return str.__hash__(str(self.m))

    @staticmethod
    def getRandomMatrix(n=None, m=None):
        """
        возвращает рандомную матрицу
        n и m размеры
        :param n: если не задано, то случайное
        :param m: если не задано, то случайное
        :return:
        """
        if not n or not m:
            n = random.randint(1, 30)
            m = random.randint(1, 30)
        new = Matrix.zeros(n, m)
        for i in range(n):
            for j in range(m):
                new[i][j] = random.randint(-100, 100)
        return new
