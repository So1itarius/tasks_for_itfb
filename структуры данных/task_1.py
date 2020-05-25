"""
1. Реализовать односвязный список (описание операций в слайдах)
"""


class LinkedList:

    def __init__(self):
        self.head = Node(None, None)

    def insert_at_end(self, data):
        """ InsertAtEnd – вставка в конец.
            (добавляем к начальному узлу)
        """
        a = self.head
        while True:
            if a.pointer is None:
                a.pointer = Node(data, None)
                break
            else:
                a = a.pointer

    def insert_at_head(self, data):
        """  InsertAtHead – вставка в начало.
             (заменяем начальный узел)
        """
        self.head = Node(data, self.head.pointer)

    def delete(self, data):
        """ Delete– удаление указанного элемента."""
        a = self.head
        b = self.head
        while True:
            if a is None:
                return False
            if a.data == data:
                b.pointer = a.pointer
                break
            else:
                b = a
                a = a.pointer



    def delete_at_head(self):
        """ DeleteAtHead – удаление первого элемента. """
        self.head = self.head.pointer

    def search(self, data):
        """ Search– получение указанного элемента."""
        a = self.head
        while True:
            if a is None:
                return False
            if a.data == data:
                return a
            else:
                a = a.pointer

    def is_empty(self):
        """– возвращает true, если связный список пуст."""
        if self.head.data is None and self.head.pointer is None:
            return True
        else:
            return False


class Node:

    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

    def __str__(self):
        return f"Node({self.data}, {self.pointer})"


if __name__ == "__main__":
    a = LinkedList()
    print(a.is_empty())
    a.insert_at_end("qwerty")
    a.insert_at_end("qwerty1")
    a.insert_at_end("qwerty2")
    a.insert_at_end("qwerty3")
    a.insert_at_head("qwerty0")
    print(a.head)
    a.delete("qwerty3")
    print(a.head)
    print(a.search("qwerty2"))
