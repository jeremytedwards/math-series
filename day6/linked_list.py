class Node(object):
    data = None
    point = None

    def __init__(self, data=None, point=None):
        self.data = data
        self.point = point


class LinkedList():
        def __init__(self, data=None, point=None):
            self.head = Node()
            self.head.point = self.head
            self.length = 0

        def insert(self):
            pass

        def pop(self):
            pass

        def size(self):
            return self.length

        def search(self, value):
            pass

        def remove(self, node):
            pass

        def display(self):
            pass


# TODO: insert(val) will insert the value ‘val’ at the head of the list
# TODO: pop() will pop the first value off the head of the list and return it.
# TODO: size() will return the length of the list
# TODO: search(val) will return the node containing ‘val’ in the list, if present, else None
# TODO: remove(node) will remove the given node from the list, wherever it might be (node must be an item in the list)
# TODO: display() will print the list represented as a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”