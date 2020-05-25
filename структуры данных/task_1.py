"""
1. Реализовать односвязный список (описание операций в слайдах)
"""


class LinkedList():

    def __init__(self):
        self.head = node(None, None)

    def insert_at_end(self, data):
        """ InsertAtEnd – вставка в конец.
        """
        a = self.head
        while True:
            if a.pointer is None:
                a.pointer = node(data, None)
                break
            else:
                a = a.pointer

    def InsertAtHead(self, data):
        """  InsertAtHead – вставка в начало. """

    def Delete(self):
        """ Delete– удаление указанного элемента."""

    pass

    def DeleteAtHead(self):
        """DeleteAtHead – удаление первого элемента. """

    pass

    def Search(self, index):
        """ Search– получение указанного элемента."""
        return

    def isEmpty(self):
        """– возвращает true, если связный список пуст."""

    pass


class node():

    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

    def __str__(self):
        return f"Node({self.data}, {self.pointer})"


if __name__ == "__main__":
    a = LinkedList()
    a.insert_at_end("qwerty")
    a.insert_at_end("qwerty1")
    a.insert_at_end("qwerty2")
    a.insert_at_end("qwerty3")
    print(a.head)
