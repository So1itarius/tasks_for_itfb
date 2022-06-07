class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.nextcat = None

    def __str__(self):
        return f"Node({self.cat}, {self.nextcat})"


class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, cat):
        lastbox = self.head
        while (lastbox):
            if cat == lastbox.cat:
                return True
            else:
                lastbox = lastbox.nextcat
        return False

    def addToEnd(self, newcat):
        newbox = Box(newcat)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while (lastbox.nextcat):
            lastbox = lastbox.nextcat
        lastbox.nextcat = newbox

if __name__ == "__main__":
    a = LinkedList()
    a.addToEnd("qwerty")
    a.addToEnd("qwerty1")
    a.addToEnd("qwerty2")
    a.addToEnd("qwerty3")
    a.head.nextcat.nextcat.nextcat.nextcat = 1
    print(a.head)
