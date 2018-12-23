#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/23/18


class NodeForStack:
    """
    Вспомогательный класс
    узел стека
    """
    def __init__(self, item=None):
        self.item = item  # нагрузка (значение)
        self.next = None  # ссылка на следующий элемент


class Stack:
    """
    Стек
    """
    def __init__(self):
        """
        конструктор
        """
        self.top_node = None  # верхний элемент
        self.size = 0  # кол-во элементов в стеке (размер стека)

    def empty(self):
        """
        проверка на пустоту
        :return: True - если стек пуст / False в противном случае
        """
        return self.top_node is None

    def push(self, item):
        """
        Добавить элемент в стек
        :param item: элемент
        :return:
        """
        self.size += 1
        new_node = NodeForStack(item)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        """
        Извлечь элемент из стека
        (забирается верхний элемент)
        :return: искомый элемент
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
        возвращает верхний элемент, но не извлекает его
        :return: верхинй элемент
        """
        assert not self.empty(), 'Stack is empty!'
        return self.top_node.item

    def __len__(self):
        """
        :return: длина (размер стека)
        """
        return self.size
