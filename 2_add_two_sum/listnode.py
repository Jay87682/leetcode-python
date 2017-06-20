from node import Node

class ListNode():
    """ Create a list of none-negative integer.
    Each node should contain a value with one digital (<10)

    Attributes:
        start: Star node of the list
        end: End node of the list

    """
    def __init__(self):
        """ Init ListNode """
        self.start = None
        self.end = None

    def addNode(self, value):
        """ Add the node to the end of the list"""
        if self.start is not None:
            self.end.next = Node(value)
            self.end = self.end.next
        else:
            self.start = Node(value)
            self.end = self.start

    def getStartNode(self):
        """ Return the start node """
        return self.start

    def __str__(self):
        """ Print the list. For Debug """
        current = self.start
        listStr = ""
        while current is not None:
            listStr += " " + str(current.val)
            current = current.next
        return listStr

"""Test code"""
# ls = ListNode()
# ls.addNode(1)
# ls.addNode(2)
# print(ls)
