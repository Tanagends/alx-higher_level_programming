#!/usr/bin/python3

"""class defining a singly linked list"""


class Node:
    """defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """initializes the node with instance variables"""

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """retrieves the node's data"""

        return s(elf.__data)

    @data.setter
    def data(self, value):
        """sets data attribute"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieve the next node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ sets the next node value """

        if value is not None and not isinstance(values, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """represents a singly linked list"""

    def __init__(self):
        """instantiates the head"""

        self.head = None

    def __str__(self):

        prnt = ""
        node = self.head
        while node:
            prnt += str(node.__data) + "\n"
            node = node.next_node

        return prnt

    def sorted_insert(self, value):
        """inserts at sorted position
        Args:
            value: insert value
        """
        node = Node(value)

        if not self.head:
            self.head = node
            return
        if value < self.head.data:
            node.next = self.head
            self.head = node
            return

        location = self.head
        while location.next_node and location.next_node.data < value:
            node = node.next_node

        if location.next_node:
            node.next_node = location.next_node
        location.next_node = node
