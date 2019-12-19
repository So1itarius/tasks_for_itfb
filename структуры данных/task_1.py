"""
1. Реализовать односвязный список (описание операций в слайдах)
"""


class linked_list(object):
    pass

    def __init__(self):
        self.head = None

    def InsertAtEnd(self):
        """ InsertAtEnd – вставка в конец. """

    pass

    def InsertAtHead(self):
        """  InsertAtHead– вставка в начало. """

    pass

    def Delete(self):
        """ Delete– удаление указанного элемента."""

    pass

    def DeleteAtHead(self):
        """DeleteAtHead – удаление первого элемента. """

    pass

    def Search(self):
        """ Search– получение указанного элемента."""

    pass

    def isEmpty(self):
        """– возвращает true, если связный список пуст."""

    pass


class node(object):

    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer


if __name__ == "__main__":
    a = linked_list().head
    print(a)

    pass
