#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node
       
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        x_node = Node(value)

        if self.__head is None:
            self.__head = x_node
            return

        cur_node = self.__head

        if self.__head.data > value:
            x_node.next_node = self.__head
            self.__head = x_node
            return
        else:
            while cur_node.next_node:
                if cur_node.next_node.data >= value:
                    break
                cur_node = cur_node.next_node
                
            x_node.next_node = cur_node.next_node
            cur_node.next_node = x_node


    def __str__(self):
        s =""
        while self.__head:
            s += str(self.__head.data) + '\n'
            self.__head = self.__head.next_node
        s = s[:-1]
        return s