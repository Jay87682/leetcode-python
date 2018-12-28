class Node(object):
    def __init__(self, data):
        if type(data) is not int:
            raise TypeError("data should be integer")
        self.val = data
        self.next = None

    def printVale(self):
        print(self.val)


"""Test code"""
# n = Node(1)
# n.next = Node(2)
#
# current = n
# while current is not None:
#     print(str(current.val))
#     current = current.next
